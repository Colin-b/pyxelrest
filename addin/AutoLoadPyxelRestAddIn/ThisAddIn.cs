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
        private static readonly string PATH_TO_XLWINGS_BAS_ENV_VAR = "PathToXlWingsBasFile";

        private void ThisAddIn_Startup(object sender, EventArgs e)
        {
            log4net.Config.XmlConfigurator.Configure();
            Log.Info("AddIn Startup.");
            ((Excel.AppEvents_Event)Application).NewWorkbook += OnNewWorkBook;
            Application.WorkbookOpen += OnOpenWorkBook;
            Application.WorkbookBeforeSave += OnSaveWorkBook;
        }

        private void OnNewWorkBook(Excel.Workbook Wb)
        {
            ActivatePyxelRest(OnNewWorkBook, Wb);
        }

        private void OnOpenWorkBook(Excel.Workbook Wb)
        {
            ActivatePyxelRest(OnOpenWorkBook, Wb);
        }

        private void OnSaveWorkBook(Excel.Workbook Wb, bool SaveAsUI, ref bool Cancel)
        {
            ActivatePyxelRest(OnSaveWorkBook, Wb);
        }

        internal bool ImportUserDefinedFunctions()
        {
            try
            {
                Application.Run("'" + Application.ActiveWorkbook.Name + "'!ImportPythonUDFs");
                Log.Info("User Defined Functions imported.");
                return true;
            }
            catch (Exception ex)
            {
                Log.Error("Unable to import User Defined Functions.", ex);
                return false;
            }
        }

        private void ActivatePyxelRest(Action<Excel.Workbook, string> loadAction, Excel.Workbook Wb)
        {
            string pathToBasFile = GetPathToXlWingsBasFile();
            if (pathToBasFile != null && pathToBasFile.Length > 0)
                loadAction.Invoke(Wb, pathToBasFile);
            else
                Log.Warn("No configuration can be found to load.");
        }

        private void OnNewWorkBook(Excel.Workbook Wb, string pathToBasFile)
        {
            ImportXlWingsBasFile(Wb, pathToBasFile);
            ImportUserDefinedFunctions();
        }

        private void OnOpenWorkBook(Excel.Workbook Wb, string pathToBasFile)
        {
            VBComponent xlwingsModule = GetXlWingsModule(Wb);
            if (xlwingsModule == null || RemoveXlWingsModule(Wb, xlwingsModule))
                ImportXlWingsBasFile(Wb, pathToBasFile);
            else
                Log.Error("Previous XLWings module cannot be removed.");
            ImportUserDefinedFunctions();
        }

        private void OnSaveWorkBook(Excel.Workbook Wb, string pathToBasFile)
        {
            VBComponent xlwingsModule = GetXlWingsModule(Wb);
            if(xlwingsModule == null)
            {
                if (RemoveXlWingsModule(Wb, xlwingsModule))
                    ImportXlWingsBasFile(Wb, pathToBasFile);
                else
                    Log.Error("Previous XLWings module cannot be removed.");
                ImportUserDefinedFunctions();
            }
            else
            {
                Log.Info("Do nothing on save.");
            }
        }

        private void ImportXlWingsBasFile(Excel.Workbook Wb, string pathToBasFile)
        {
            try {
                Wb.VBProject.VBComponents.Import(pathToBasFile);
                Log.Info("XLWings module imported.");
            }
            catch (Exception ex)
            {
                Log.Error("XlWings module could not be imported.", ex);
            };
        }

        private string GetPathToXlWingsBasFile()
        {
            string filePath = Environment.GetEnvironmentVariable(PATH_TO_XLWINGS_BAS_ENV_VAR, EnvironmentVariableTarget.User);
            if(filePath == null)
                filePath = Environment.GetEnvironmentVariable(PATH_TO_XLWINGS_BAS_ENV_VAR, EnvironmentVariableTarget.Machine);
            if (filePath == null)
                Log.WarnFormat("Environment variable ({0}) providing path to PyxelRest XlWings configuration file cannot be found.", PATH_TO_XLWINGS_BAS_ENV_VAR);
            return filePath;
        }

        private VBComponent GetXlWingsModule(Excel.Workbook Wb)
        {
            if (Wb.HasVBProject)
            {
                foreach (VBComponent vbComponent in Wb.VBProject.VBComponents)
                {
                    if (XLWINGS_VB_COMPONENT_NAME.Equals(vbComponent.Name))
                        return vbComponent;
                }
            }
            return null;
        }

        private bool RemoveXlWingsModule(Excel.Workbook Wb, VBComponent vbComponent)
        {
            try
            {
                Wb.VBProject.VBComponents.Remove(vbComponent);
                Log.Info("XlWings module removed.");
            }
            catch(Exception ex)
            {
                Log.Error("XlWings module could not be removed.", ex);
                return false;
            };
            return true;
        }

        private void ThisAddIn_Shutdown(object sender, EventArgs e)
        {
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
