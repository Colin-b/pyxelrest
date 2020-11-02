using System;
using Excel = Microsoft.Office.Interop.Excel;
using Microsoft.Vbe.Interop;
using log4net;
using Microsoft.Win32;
using System.Windows.Forms;
using System.Reflection;
using System.Diagnostics;
using System.Configuration;
using System.IO;
using System.Collections.Generic;

namespace PyxelRestAddIn
{
    public partial class ThisAddIn
    {
        private static readonly ILog Log = LogManager.GetLogger("PyxelRestAddIn");

        private static readonly string XLWINGS_MODULE_NAME = "xlwings";
        private static readonly string GENERATED_UDFS_MODULE_NAME = "xlwings_udfs";
        private static readonly string PYXELREST_VB_PROJECT_FILE_NAME = "pyxelrest.xlam";
        private static readonly string VBA_OBJ_MODEL_FAILURE_MSG = 
            "Please 'Trust access to the VBA object model'.\n" +
            "> File > Options > Trust Center > Trust Center Settings > Macro Settings\n";

        private static System.Configuration.Configuration Config = LoadConfig();

        internal static string GetSetting(string key)
        {
            if (Config.AppSettings.Settings[key] == null)
                return string.Empty;
            return Config.AppSettings.Settings[key].Value;
        }

        internal static void SetSetting(string key, string value)
        {
            var settings = Config.AppSettings.Settings;
            if (settings[key] == null)
                settings.Add(key, value);
            else
                settings[key].Value = value;
            Config.Save(ConfigurationSaveMode.Modified);
            ConfigurationManager.RefreshSection(Config.AppSettings.SectionInformation.Name);
        }

        private void ThisAddIn_Startup(object sender, EventArgs e)
        {
            Config = LoadConfig();
            log4net.Config.XmlConfigurator.Configure(new FileInfo(Config.FilePath));
            Log.InfoFormat("Starting PyxelRest Addin {0}", GetVersion());
            Log.DebugFormat("Configuration loaded from {0}", Config.FilePath);
            Application.WorkbookOpen += OnOpenWorkBook;
            Application.WorkbookActivate += OnActivateWorkBook;
            try
            {
                OnExcelStart();
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while loading PyxelRest on Microsoft Excel start.", ex);
            }
        }

        // Hack to load configuration from external configuration file instead of embedded one.
        private static System.Configuration.Configuration LoadConfig()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if (appDataFolder != null)
            {
                var configMap = new ExeConfigurationFileMap
                {
                    ExeConfigFilename = Path.Combine(appDataFolder, "pyxelrest", "excel_addin", "PyxelRestAddIn.dll.config")
                };

                return ConfigurationManager.OpenMappedExeConfiguration(configMap, ConfigurationUserLevel.None);
            }
            // If custom configuration cannot be found, load internal one (default)
            return ConfigurationManager.OpenExeConfiguration(ConfigurationUserLevel.None);
        }

        private void ThisAddIn_Shutdown(object sender, EventArgs e)
        {
            Log.Debug("Stopping PyxelRest Addin...");
            try
            {
                // Do not read configuration to perform the action requested by the user even if saving it in configuration failed.
                var autoUpdateButton = Globals.Ribbons.PyxelRestRibbon.autoUpdateButton;
                if (autoUpdateButton.Enabled && autoUpdateButton.Checked)
                    new Updater().CheckUpdate();
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while checking for PyxelRest update on Microsoft Excel shutdown.", ex);
            }
        }

        internal string GetVersion()
        {
            Assembly assembly = Assembly.GetExecutingAssembly();
            FileVersionInfo fileVersionInfo = FileVersionInfo.GetVersionInfo(assembly.Location);
            return string.Format("{0}.{1}.{2}", fileVersionInfo.FileMajorPart, fileVersionInfo.FileMinorPart, fileVersionInfo.FileBuildPart);
        }

        internal string GetPyxelRestVersion()
        {
            string pythonPath = GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                return string.Empty;

            string pythonScriptPath = Path.GetTempFileName();
            File.WriteAllLines(pythonScriptPath, new string[] {
                "import pyxelrest",
                "print(pyxelrest.__version__)"
            });

            Process pyxelrestVersion = new Process();
            pyxelrestVersion.StartInfo.FileName = pythonPath;
            pyxelrestVersion.StartInfo.Arguments = pythonScriptPath;
            pyxelrestVersion.StartInfo.UseShellExecute = false;
            pyxelrestVersion.StartInfo.RedirectStandardOutput = true;
            pyxelrestVersion.StartInfo.CreateNoWindow = true;
            pyxelrestVersion.Start();
            return pyxelrestVersion.StandardOutput.ReadLine();
        }

        internal bool ImportUserDefinedFunctions(bool reload=false)
        {
            try
            {
                if (Application.ActiveWorkbook == null)
                {
                    Log.Info("User defined functions cannot be generated while workbook is inactive.");
                    return false;
                }
                if (!TrustAccessToTheVBAObjectModel())
                    return false;
                VBProject vbProject = GetPyxelRestVBProject();
                if (vbProject == null)
                    return false;  // This should never happen but still user can manually remove/update the xlam file
                if (XlWingsIsNotLoaded(vbProject))
                    LoadXlWings(pyxelRest:vbProject);  // It can happen if UDFs were not supposed to be loaded at startup
                if (reload)
                {
                    KillPython();
                }
                dynamic errorCode = Application.Run(string.Format("{0}!ImportPythonUDFs", PYXELREST_VB_PROJECT_FILE_NAME));
                if (errorCode != null)
                    Log.DebugFormat("User defined functions were not generated (return code {0})", errorCode);
                else
                    Log.Debug("User defined functions generated.");
                return true;
            }
            catch (Exception ex)
            {
                Log.Error("Unable to generate user defined functions.", ex);
                return false;
            }
        }

        private void KillPython()
        {
            Process[] pythonProcesses = Process.GetProcessesByName("pythonw");
            if (pythonProcesses.Length == 0)
            {
                Log.Debug("No need to kill Python as no Python process is running.");
                return;
            }

            Log.DebugFormat("{0} Python processes runnning. Killing Python process...", pythonProcesses.Length);
            dynamic returnCode = Application.Run(string.Format("{0}!KillPy", PYXELREST_VB_PROJECT_FILE_NAME));
            if (returnCode != null)
                Log.DebugFormat("Killing request failed (return code {0}).", returnCode);

            // As Python process is not killed instantly, ensure it is killed before trying to launch it again.
            // Check 10 times at max every 100ms for one Python process to be killed
            for (int check = 0; check < 10; check++)
            {
                Log.Debug("Waiting 100ms for Python process to be killed.");
                System.Threading.Thread.Sleep(100);
                foreach (Process pythonProcess in pythonProcesses)
                {
                    if (pythonProcess.HasExited)
                    {
                        Log.DebugFormat("Python process {0} killed.", pythonProcess.Id);
                        return;
                    }
                }
            }
            Log.Debug("Considering Python process as killed even if it might not be (time out).");
        }

        private bool TrustAccessToTheVBAObjectModel()
        {
            var accessVBOMs = new Dictionary<string, string>() {
                { "HKEY_CURRENT_USER\\Software\\Microsoft\\Office\\" + Application.Version + "\\Excel\\Security", "AccessVBOM" },
                { "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Office\\" + Application.Version + "\\Excel\\Security", "AccessVBOM" },
                { "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Office\\" + Application.Version + "\\excel\\security", "accessvbom" },
            };

            foreach (var accessVBOMItem in accessVBOMs)
            {
                int? accessVBOM = Registry.GetValue(accessVBOMItem.Key, accessVBOMItem.Value, null) as int?;
                if (IsValidAccessVBOM(accessVBOM))
                {
                    Log.Debug("'Trust access to the VBA project object model' is enabled.");
                    return true;
                }
            }

            Log.Error("'Trust access to the VBA project object model' is not enabled.");
            MessageBox.Show(
                VBA_OBJ_MODEL_FAILURE_MSG,
                "Access to VBA object model is not enabled",
                MessageBoxButtons.OK,
                MessageBoxIcon.Exclamation);
            return false;
        }

        private bool IsValidAccessVBOM(int? accessVBOM)
        {
            return accessVBOM.HasValue && accessVBOM.Value == 1;
        }

        private void OnActivateWorkBook(Excel.Workbook Wb)
        {
            try
            {
                if (!GenerateUDFAtStartup())
                {
                    Log.Debug("Do not generate user defined functions on workbook activation (as configured).");
                }
                else if (HasGeneratedUDFs())
                {
                    Log.DebugFormat("Activating '{0}' workbook. User defined functions have already been generated. Do nothing.", Wb.Name);
                }
                else
                {
                    Log.DebugFormat("Activating '{0}' workbook. Generating user defined functions...", Wb.Name);
                    ServiceConfigurationForm.UpdateServices();
                    LoadXlWings();
                    ImportUserDefinedFunctions();
                }
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while loading PyxelRest on workbook activation.", ex);
            }
        }

        private void OnOpenWorkBook(Excel.Workbook Wb)
        {
            try
            {
                if (!GenerateUDFAtStartup())
                {
                    Log.Debug("Do not generate user defined functions on workbook opening (as configured).");
                }
                else if(HasGeneratedUDFs())
                {
                    Log.DebugFormat("Opening '{0}' workbook. User defined functions have already been generated. Do nothing.", Wb.Name);
                }
                else if(Application.ActiveWorkbook == null)
                {
                    Log.DebugFormat("Opening Inactive '{0}' workbook. Waiting for workbook activation...", Wb.Name);
                }
                else
                {
                    Log.DebugFormat("Opening '{0}' workbook. Generating user defined functions...", Wb.Name);
                    ServiceConfigurationForm.UpdateServices();
                    LoadXlWings();
                    ImportUserDefinedFunctions();
                }
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while loading PyxelRest on workbook opening.", ex);
            }
        }

        private void OnExcelStart()
        {
            if (!GenerateUDFAtStartup())
            {
                Log.Debug("Do not generate user defined functions at Microsoft Excel start (as configured).");
            }
            else if (Application.ActiveWorkbook == null)
            {
                Log.Debug("Microsoft Excel started with an already existing document. Wait for workbook opening event to generate user defined functions.");
            }
            else
            {
                Log.Debug("Microsoft Excel started with a blank document. Generating user defined functions...");
                ServiceConfigurationForm.UpdateServices();
                LoadXlWings();
                ImportUserDefinedFunctions();
            }
        }

        internal static bool GenerateUDFAtStartup()
        {
            string generateUDFAtStartup = GetSetting("GenerateUDFAtStartup");
            return string.IsNullOrEmpty(generateUDFAtStartup) || "True".Equals(generateUDFAtStartup);
        }

        private bool HasGeneratedUDFs()
        {
            VBProject vbProject = GetPyxelRestVBProject();
            if (vbProject == null)
                return false;
            return HasGeneratedUDFs(vbProject);
        }

        private bool HasGeneratedUDFs(VBProject pyxelRest)
        {
            foreach (VBComponent vbComponent in pyxelRest.VBComponents)
            {
                if (GENERATED_UDFS_MODULE_NAME.Equals(vbComponent.Name))
                    return true;
            }
            return false;
        }

        private bool XlWingsIsNotLoaded(VBProject pyxelRest)
        {
            foreach (VBComponent vbComponent in pyxelRest.VBComponents)
            {
                if (XLWINGS_MODULE_NAME.Equals(vbComponent.Name))
                    return false;
            }
            return true;
        }

        private bool LoadXlWings(VBProject pyxelRest=null)
        {
            try
            {
                if (!TrustAccessToTheVBAObjectModel())
                    return false;
                VBProject vbProject = pyxelRest == null ? GetPyxelRestVBProject() : pyxelRest;
                if (vbProject == null)
                {
                    Log.Error("PyxelRest VB Project cannot be found.");
                    return false;
                }
                string pathToBasFile = GetSetting("PathToXlWingsBasFile");
                if (!File.Exists(pathToBasFile))
                {
                    Log.WarnFormat("No XLWings module can be found to load in '{0}'.", pathToBasFile);
                    return false;
                }

                vbProject.VBComponents.Import(pathToBasFile);
                Log.Debug("XLWings module imported.");
                return true;
            }
            catch (Exception ex)
            {
                Log.Error("XlWings module could not be imported.", ex);
                return false;
            };
        }

        private VBProject GetPyxelRestVBProject()
        {
            foreach (VBProject vb in Application.VBE.VBProjects)
            {
                try
                {
                    // TODO Check the entire file name instead of the end of the path
                    if (vb.FileName.EndsWith(PYXELREST_VB_PROJECT_FILE_NAME))
                        return vb;
                }
                catch (DirectoryNotFoundException)
                {
                    // This exception is sometimes thrown by Microsoft.Vbe.Interop._VBProject.get_FileName()
                    Log.Warn("Unable to retrieve the file name of a VB project.");
                }
            }
            Log.ErrorFormat("'{0}' project was not loaded. Installation seems corrupt.", PYXELREST_VB_PROJECT_FILE_NAME);
            return null;
        }

        #region VSTO generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InternalStartup()
        {
            this.Startup += new System.EventHandler(ThisAddIn_Startup);
            this.Shutdown += new System.EventHandler(ThisAddIn_Shutdown);
        }
        
        #endregion
    }
}
