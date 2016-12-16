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

        private void ThisAddIn_Startup(object sender, EventArgs e)
        {
            log4net.Config.XmlConfigurator.Configure();
            ((Excel.AppEvents_Event)Application).NewWorkbook += OnNewWorkBook;
            Application.WorkbookOpen += OnOpenWorkBook;
            ActivatePyxelRest(OnExcelStart, Application.ActiveWorkbook);
        }

        private void OnNewWorkBook(Excel.Workbook Wb)
        {
            ActivatePyxelRest(OnNewWorkBook, Wb);
        }

        private void OnOpenWorkBook(Excel.Workbook Wb)
        {
            ActivatePyxelRest(OnOpenWorkBook, Wb);
        }
         
        internal bool ImportUserDefinedFunctions()
        {
            return ImportUserDefinedFunctions(Application.ActiveWorkbook);
        }

        private bool ImportUserDefinedFunctions(Excel.Workbook Wb)
        {
            try
            {
                Application.Run("'" + Wb.Name + "'!ImportPythonUDFs");
                Log.InfoFormat("{0}: User Defined Functions imported.", Wb.Name);
                return true;
            }
            catch (Exception ex)
            {
                Log.Error(string.Format("{0}: Unable to import User Defined Functions.", Wb.Name), ex);
                return false;
            }
        }

        private void ActivatePyxelRest(Action<Excel.Workbook, string> loadAction, Excel.Workbook Wb)
        {
            string pathToBasFile = GetPathToXlWingsBasFile();
            if (pathToBasFile != null)
                loadAction.Invoke(Wb, pathToBasFile);
            else
                Log.WarnFormat("{0}: No XLWings module can be found to load.", Wb.Name);
        }

        private void OnNewWorkBook(Excel.Workbook Wb, string pathToBasFile)
        {
            ImportXlWingsBasFile(Wb, pathToBasFile);
            ImportUserDefinedFunctions(Wb);
        }

        private void OnOpenWorkBook(Excel.Workbook Wb, string pathToBasFile)
        {
            VBComponent xlwingsModule = GetXlWingsModule(Wb);
            if (xlwingsModule == null || RemoveXlWingsModule(Wb, xlwingsModule))
                ImportXlWingsBasFile(Wb, pathToBasFile);
            else
                Log.ErrorFormat("{0}: Previous XLWings module cannot be removed.", Wb.Name);
            ImportUserDefinedFunctions(Wb);
        }
        
        private void OnExcelStart(Excel.Workbook Wb, string pathToBasFile)
        {
            if (IsBlankWorkBook(Wb))
            {
                ImportXlWingsBasFile(Wb, pathToBasFile);
                ImportUserDefinedFunctions(Wb);
            }
            else
            {
                OnOpenWorkBook(Wb, pathToBasFile);
            }
        }

        private bool IsBlankWorkBook(Excel.Workbook Wb)
        {
            return "" == Wb.CodeName;
        }

        private void ImportXlWingsBasFile(Excel.Workbook Wb, string pathToBasFile)
        {
            try {
                Wb.VBProject.VBComponents.Import(pathToBasFile);
                Log.InfoFormat("{0}: XLWings module imported.", Wb.Name);
            }
            catch (Exception ex)
            {
                Log.Error(string.Format("{0}: XlWings module could not be imported.", Wb.Name), ex);
            };
        }

        private string GetPathToXlWingsBasFile()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if(appDataFolder != null)
                return System.IO.Path.Combine(appDataFolder, "pyxelrest", "xlwings.bas");
            return null;
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
                Log.InfoFormat("{0}: XlWings module removed.", Wb.Name);
            }
            catch(Exception ex)
            {
                Log.Error(string.Format("{0}: XlWings module could not be removed.", Wb.Name), ex);
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
