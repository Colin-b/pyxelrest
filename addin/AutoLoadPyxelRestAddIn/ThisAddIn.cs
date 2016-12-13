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
            ((Excel.AppEvents_Event)Application).NewWorkbook += InsertXlWingsBasFile;
            Application.WorkbookOpen += UpdateXlWingsBasFile;
        }

        private void LoadXlWingsBasFile(Action<Excel.Workbook, string> loadAction, Excel.Workbook Wb)
        {
            string pathToBasFile = GetPathToXlWingsBasFile();
            if (pathToBasFile != null && pathToBasFile.Length > 0)
                loadAction.Invoke(Wb, pathToBasFile);
            else
                Log.Warn("No configuration can be found to load.");
        }

        private void InsertXlWingsBasFile(Excel.Workbook Wb)
        {
            LoadXlWingsBasFile(InsertXlWingsBasFile, Wb);
        }

        private void InsertXlWingsBasFile(Excel.Workbook Wb, string pathToBasFile)
        {
            Wb.VBProject.VBComponents.Import(pathToBasFile);
            Log.Info("XLWings module inserted.");
        }

        private void UpdateXlWingsBasFile(Excel.Workbook Wb)
        {
            LoadXlWingsBasFile(UpdateXlWingsBasFile, Wb);
        }

        private void UpdateXlWingsBasFile(Excel.Workbook Wb, string pathToBasFile)
        {
            if (RemoveXlWingsModule(Wb))
            {
                Wb.VBProject.VBComponents.Import(pathToBasFile);
                Log.Info("XLWings module updated.");
            }
            else
            {
                Log.Error("Previous XLWings module cannot be removed.");
            }
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

        private bool RemoveXlWingsModule(Excel.Workbook Wb)
        {
            if(Wb.HasVBProject)
            {
                foreach (VBComponent vbComponent in Wb.VBProject.VBComponents)
                {
                    if (XLWINGS_VB_COMPONENT_NAME.Equals(vbComponent.Name))
                    {
                        if (RemoveXlWingsModule(Wb, vbComponent))
                            break;
                        return false;
                    }
                }
            }
            return true;
        }

        private bool RemoveXlWingsModule(Excel.Workbook Wb, VBComponent vbComponent)
        {
            try
            {
                Wb.VBProject.VBComponents.Remove(vbComponent);
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
