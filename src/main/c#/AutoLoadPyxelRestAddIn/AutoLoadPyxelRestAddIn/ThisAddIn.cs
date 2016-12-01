using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using Excel = Microsoft.Office.Interop.Excel;
using Office = Microsoft.Office.Core;
using Microsoft.Office.Tools.Excel;

namespace AutoLoadPyxelRestAddIn
{
    public partial class ThisAddIn
    {
        private void ThisAddIn_Startup(object sender, System.EventArgs e)
        {
            ((Excel.AppEvents_Event)Application).NewWorkbook += OnNewWorkBook;
            // TODO Handle Opening of books without module already imported
        }

        private void OnNewWorkBook(Excel.Workbook Wb)
        {
            string pathToBasFile = Environment.GetEnvironmentVariable("PathToXlWingsBasFile");
            if (pathToBasFile != null && pathToBasFile.Length > 0)
            {
                Wb.VBProject.VBComponents.Import(pathToBasFile);
            }
        }

        private void ThisAddIn_Shutdown(object sender, System.EventArgs e)
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
