using System;
using Excel = Microsoft.Office.Interop.Excel;
using Microsoft.Vbe.Interop;
using log4net;

namespace AutoLoadPyxelRestAddIn
{
    public partial class ThisAddIn
    {
        private static readonly ILog Log = LogManager.GetLogger("AutoLoadPyxelRestAddIn");

        private static readonly string XLWINGS_VB_COMPONENT_NAME = "xlwings";
        private static readonly string PYXELREST_VB_PROJECT_NAME = "PyxelRest";

        private void ThisAddIn_Startup(object sender, EventArgs e)
        {
            log4net.Config.XmlConfigurator.Configure();
            Log.Info("Starting Auto Load PyxelRest Addin...");
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
                if (!TryToLoadXlWingsModule())
                    return false;
                Application.Run("pyxelrest.xlam!ImportPythonUDFs");
                Log.InfoFormat("User Defined Functions imported.");
                return true;
            }
            catch (Exception ex)
            {
                Log.Error("Unable to import User Defined Functions.", ex);
                return false;
            }
        }

        private void OnActivateWorkBook(Excel.Workbook Wb)
        {
            if (ContainsXlWingsModule())
            {
                Log.InfoFormat("Activating '{0}' workbook. PyxelRest already activated. Do nothing.", Wb.Name);
            }
            else
            {
                Log.InfoFormat("Activating '{0}' workbook. Activating PyxelRest...", Wb.Name);
                ActivatePyxelRest();
            }
        }

        private void OnOpenWorkBook(Excel.Workbook Wb)
        {
            try
            {
                if(ContainsXlWingsModule())
                {
                    Log.InfoFormat("Opening '{0}' workbook. PyxelRest already activated. Do nothing.", Wb.Name);
                }
                else if(Application.ActiveWorkbook == null)
                {
                    Log.InfoFormat("Opening Inactive '{0}' workbook. Waiting for workbook activation...", Wb.Name);
                }
                else
                {
                    Log.InfoFormat("Opening '{0}' workbook. Activating PyxelRest...", Wb.Name);
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
                Log.Info("Excel started with an already existing document. Expecting workbook opening event to activate PyxelRest.");
            }
            else
            {
                Log.Info("Excel started with a blank document. Activating PyxelRest...");
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
                    Log.WarnFormat("No XLWings module can be found to load.");
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
                Log.WarnFormat("No XLWings module can be found to load.");
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
                VBProject vbProject = GetPyxelRestVBProject();
                if (vbProject == null)
                {
                    Log.Error("PyxelRest VB Project cannot be found.");
                    return false;
                }
                vbProject.VBComponents.Import(pathToBasFile);
                Log.Info("XLWings module imported.");
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
            if (vbProject != null)
            {
                foreach (VBComponent vbComponent in vbProject.VBComponents)
                {
                    if (XLWINGS_VB_COMPONENT_NAME.Equals(vbComponent.Name))
                        return vbComponent;
                }
            }
            return null;
        }

        private void ThisAddIn_Shutdown(object sender, EventArgs e)
        {
            Log.Info("Stop Auto Load PyxelRest Addin...");
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
