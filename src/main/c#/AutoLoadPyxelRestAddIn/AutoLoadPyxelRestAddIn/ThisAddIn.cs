using System;
using Excel = Microsoft.Office.Interop.Excel;
using Microsoft.Vbe.Interop;

namespace AutoLoadPyxelRestAddIn
{
    public partial class ThisAddIn
    {
        private static readonly string XLWINGS_VB_COMPONENT_NAME = "xlwings";
        private static readonly string PATH_TO_XLWINGS_BAS_ENV_VAR = "PathToXlWingsBasFile";

        private void ThisAddIn_Startup(object sender, EventArgs e)
        {
            Application.WorkbookOpen += ImportXlWingsBasFile;
        }

        private void ImportXlWingsBasFile(Excel.Workbook Wb)
        {
            string pathToBasFile = Environment.GetEnvironmentVariable(PATH_TO_XLWINGS_BAS_ENV_VAR);
            if (pathToBasFile != null && pathToBasFile.Length > 0)
            {
                if (CanImportXlWingsBasFile(Wb))
                    Wb.VBProject.VBComponents.Import(pathToBasFile);
            }
        }

        private bool CanImportXlWingsBasFile(Excel.Workbook Wb)
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
            return true;
        }

        private bool RemoveXlWingsModule(Excel.Workbook Wb, VBComponent vbComponent)
        {
            try
            {
                Wb.VBProject.VBComponents.Remove(vbComponent);
            }
            catch
            {
                // TODO Log the fact that module could not be removed and the reason
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
