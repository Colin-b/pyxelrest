using System;
using Excel = Microsoft.Office.Interop.Excel;
using Microsoft.Vbe.Interop;
using log4net;
using Microsoft.Win32;
using System.Windows.Forms;

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

        private void ThisAddIn_Startup(object sender, EventArgs e)
        {
            log4net.Config.XmlConfigurator.Configure();
            Log.Debug("Starting Auto Load PyxelRest Addin...");
            Application.WorkbookOpen += OnOpenWorkBook;
            Application.WorkbookActivate += OnActivateWorkBook;
            try
            {
                OnExcelStart();
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while activating PyxelRest on Excel start.", ex);
            }
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
                if(ContainsXlWingsModule())
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
                Log.Debug("Excel started with an already existing document. Expecting workbook opening event to activate PyxelRest.");
            }
            else
            {
                Log.Debug("Excel started with a blank document. Activating PyxelRest...");
                ActivatePyxelRest();
            }
        }

        private bool ContainsXlWingsModule()
        {
            return GetXlWingsModule() != null;
        }

        private bool TryToLoadXlWingsModule()
        {
            if (!ContainsXlWingsModule())
            {
                string pathToBasFile = GetPathToXlWingsBasFile();
                if (pathToBasFile == null)
                {
                    Log.Warn("No XLWings module can be found to load.");
                    return false;
                }
                return ImportXlWingsBasFile(pathToBasFile);
            }
            return true;
        }

        private void ActivatePyxelRest()
        {
            string pathToBasFile = GetPathToXlWingsBasFile();
            if (pathToBasFile == null)
            {
                Log.Warn("No XLWings module can be found to load.");
                return;
            }

            if(ImportXlWingsBasFile(pathToBasFile))
                ImportUserDefinedFunctions();
        }

        private string GetPathToXlWingsBasFile()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if (appDataFolder != null)
                return System.IO.Path.Combine(appDataFolder, "pyxelrest", "xlwings.bas");
            return null;
        }

        private bool ImportXlWingsBasFile(string pathToBasFile)
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

        private void ThisAddIn_Shutdown(object sender, EventArgs e)
        {
            Log.Debug("Stop Auto Load PyxelRest Addin...");
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
