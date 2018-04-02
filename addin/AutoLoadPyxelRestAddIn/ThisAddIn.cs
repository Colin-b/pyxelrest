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

namespace AutoLoadPyxelRestAddIn
{
    public partial class ThisAddIn
    {
        private static readonly ILog Log = LogManager.GetLogger("AutoLoadPyxelRestAddIn");

        private static readonly string XLWINGS_VB_COMPONENT_NAME = "xlwings";
        private static readonly string PYXELREST_VB_PROJECT_NAME = "PyxelRest";
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
            Log.DebugFormat("Starting Auto Load PyxelRest Addin {0}", GetVersion());
            Log.DebugFormat("Configuration loaded from {0}", Config.FilePath);
            Application.WorkbookOpen += OnOpenWorkBook;
            Application.WorkbookActivate += OnActivateWorkBook;
            try
            {
                OnExcelStart();
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while activating PyxelRest on Microsoft Excel start.", ex);
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
                    ExeConfigFilename = Path.Combine(appDataFolder, "pyxelrest", "configuration", "addin.config")
                };

                return ConfigurationManager.OpenMappedExeConfiguration(configMap, ConfigurationUserLevel.None);
            }
            // If custom configuration cannot be found, load internal one (default)
            return ConfigurationManager.OpenExeConfiguration(ConfigurationUserLevel.None);
        }

        private void ThisAddIn_Shutdown(object sender, EventArgs e)
        {
            Log.Debug("Stop Auto Load PyxelRest Addin...");
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
            string pythonPath = ThisAddIn.GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                return string.Empty;

            string pythonScriptPath = Path.GetTempFileName();
            File.WriteAllLines(pythonScriptPath, new string[] {
                "import pyxelrest._version",
                "print(pyxelrest._version.__version__)"
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

        internal bool ImportUserDefinedFunctions()
        {
            try
            {
                if (Application.ActiveWorkbook == null)
                {
                    Log.Info("User Defined Functions cannot be imported while workbook is inactive.");
                    return false;
                }
                if (!TrustAccessToTheVBAObjectModel())
                    return false;
                if (!TryToLoadXlWingsModule())
                    return false;
                Application.Run("pyxelrest.xlam!ImportPythonUDFs");
                Log.Debug("User Defined Functions imported.");
                return true;
            }
            catch (Exception ex)
            {
                Log.Error("Unable to import User Defined Functions.", ex);
                return false;
            }
        }

        private bool TrustAccessToTheVBAObjectModel()
        {
            int? accessVBOM = Registry.GetValue(
                "HKEY_CURRENT_USER\\Software\\Microsoft\\Office\\" + Application.Version + "\\Excel\\Security",
                "AccessVBOM", 
                null) as int?;
            if(!accessVBOM.HasValue || accessVBOM.Value != 1)
            {
                Log.Error("'Trust access to the VBA project object model' is not enabled.");
                MessageBox.Show(
                    VBA_OBJ_MODEL_FAILURE_MSG,
                    "Access to VBA object model is not enabled",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation);
                return false;
            }
            Log.Debug("'Trust access to the VBA project object model' is enabled.");
            return true;
        }

        private void OnActivateWorkBook(Excel.Workbook Wb)
        {
            if (ContainsXlWingsModule())
            {
                Log.DebugFormat("Activating '{0}' workbook. PyxelRest already activated. Do nothing.", Wb.Name);
            }
            else
            {
                Log.DebugFormat("Activating '{0}' workbook. Activating PyxelRest...", Wb.Name);
                ActivatePyxelRest();
            }
        }

        private void OnOpenWorkBook(Excel.Workbook Wb)
        {
            try
            {
                if (ContainsXlWingsModule())
                {
                    Log.DebugFormat("Opening '{0}' workbook. PyxelRest already activated. Do nothing.", Wb.Name);
                }
                else if(Application.ActiveWorkbook == null)
                {
                    Log.DebugFormat("Opening Inactive '{0}' workbook. Waiting for workbook activation...", Wb.Name);
                }
                else
                {
                    Log.DebugFormat("Opening '{0}' workbook. Activating PyxelRest...", Wb.Name);
                    ActivatePyxelRest();
                }
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while activating PyxelRest on opening workbook.", ex);
            }
        }

        private void OnExcelStart()
        {
            if (Application.ActiveWorkbook == null)
            {
                Log.Debug("Microsoft Excel started with an already existing document. Expecting workbook opening event to activate PyxelRest.");
            }
            else
            {
                Log.Debug("Microsoft Excel started with a blank document. Activating PyxelRest...");
                ServiceConfigurationForm.UpdateServices();
                ActivatePyxelRest();
            }
        }

        private bool GenerateUDFAtStartup()
        {
            string generateUDFAtStartup = GetSetting("GenerateUDFAtStartup");
            return string.IsNullOrEmpty(generateUDFAtStartup) || "True".Equals(generateUDFAtStartup);
        }

        private bool ContainsXlWingsModule()
        {
            return GetXlWingsModule() != null;
        }

        private bool TryToLoadXlWingsModule()
        {
            if (!ContainsXlWingsModule())
                return ImportXlWingsBasFile();
            return true;
        }

        private void ActivatePyxelRest()
        {
            if (ImportXlWingsBasFile())
                if (GenerateUDFAtStartup())
                    ImportUserDefinedFunctions();
                else
                    Log.Info("Do not generate user defined functions (as configured).");
        }

        private bool ImportXlWingsBasFile()
        {
            try
            {
                if (!TrustAccessToTheVBAObjectModel())
                    return false;
                VBProject vbProject = GetPyxelRestVBProject();
                if (vbProject == null)
                {
                    Log.Error("PyxelRest VB Project cannot be found.");
                    return false;
                }
                if(RemoveXlWingsModule(vbProject))
                {
                    string pathToBasFile = GetPathToXlWingsBasFile();
                    if (pathToBasFile == null)
                        return false;

                    vbProject.VBComponents.Import(pathToBasFile);
                    Log.Debug("XLWings module imported.");
                }
                else
                {
                    Log.Warn("XLWings module was not reloaded.");
                }
                return true;
            }
            catch (Exception ex)
            {
                Log.Error("XlWings module could not be imported.", ex);
                return false;
            };
        }

        private string GetPathToXlWingsBasFile()
        {
            string pathToBasFile = GetSetting("PathToXlWingsBasFile");
            if (!File.Exists(pathToBasFile))
            {
                Log.WarnFormat("No XLWings module can be found to load in '{0}'.", pathToBasFile);
                return null;
            }
            return pathToBasFile;
        }

        private VBProject GetPyxelRestVBProject()
        {
            foreach (VBProject vb in Application.VBE.VBProjects)
            {
                if (PYXELREST_VB_PROJECT_NAME.Equals(vb.Name))
                    return vb;
            }
            return null;
        }

        private VBComponent GetXlWingsModule()
        {
            VBProject vbProject = GetPyxelRestVBProject();
            if (vbProject == null)
                return null;
            return GetXlWingsModule(vbProject);
        }

        private VBComponent GetXlWingsModule(VBProject pyxelRest)
        {
            foreach (VBComponent vbComponent in pyxelRest.VBComponents)
            {
                if (XLWINGS_VB_COMPONENT_NAME.Equals(vbComponent.Name))
                    return vbComponent;
            }
            return null;
        }

        private bool RemoveXlWingsModule(VBProject vbProject)
        {
            VBComponent xlWingsModule = GetXlWingsModule(vbProject);
            if (xlWingsModule == null)
                return true;
            try
            {
                vbProject.VBComponents.Remove(xlWingsModule);
                Log.Debug("XlWings module removed.");
            }
            catch (Exception ex)
            {
                Log.Error("XlWings module could not be removed.", ex);
                return false;
            };
            return true;
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
