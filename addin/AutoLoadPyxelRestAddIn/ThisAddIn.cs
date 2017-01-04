using System;
using Excel = Microsoft.Office.Interop.Excel;
using Microsoft.Vbe.Interop;
using log4net;
using System.Runtime.InteropServices;

namespace AutoLoadPyxelRestAddIn
{
    static class NativeMethods
    {
        [DllImport("kernel32.dll")]
        public static extern IntPtr LoadLibrary(string dllToLoad);

        [DllImport("kernel32.dll")]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procedureName);
        
        [DllImport("kernel32.dll")]
        public static extern bool FreeLibrary(IntPtr hModule);
    }


    public partial class ThisAddIn
    {
        private static readonly ILog Log = LogManager.GetLogger("AutoLoadPyxelRestAddIn");

        private static readonly string XLWINGS_VB_COMPONENT_NAME = "xlwings";

        private void ThisAddIn_Startup(object sender, EventArgs e)
        {
            log4net.Config.XmlConfigurator.Configure();
            Application.WorkbookOpen += OnOpenWorkBook;
            try
            {
                OnExcelStart();
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while activating PyxelRest.", ex);
            }
        }

        internal bool ImportUserDefinedFunctions()
        {
            try
            {
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

        private void OnOpenWorkBook(Excel.Workbook Wb)
        {
            ActivatePyxelRest();
        }

        private void OnExcelStart()
        {
            if (Application.ActiveWorkbook == null)
                return; // Do nothing on opening of already existing document. Opening event will handle it properly once everything is opened.
            ActivatePyxelRest();
        }

        private void ActivatePyxelRest()
        {
            string pathToBasFile = GetPathToXlWingsBasFile();
            if (pathToBasFile != null)
            {
                ReloadXlWingsBasFile(pathToBasFile);
                ImportUserDefinedFunctions();
            }
            else
                Log.WarnFormat("No XLWings module can be found to load.");
        }

        private void ReloadXlWingsBasFile(string pathToBasFile)
        {
            VBComponent xlwingsModule = GetXlWingsModule();
            if (xlwingsModule == null || RemoveXlWingsModule(xlwingsModule))
                ImportXlWingsBasFile(pathToBasFile);
            else
                Log.Error("Previous XLWings module cannot be removed.");
        }

        private void ImportXlWingsBasFile(string pathToBasFile)
        {
            try
            {
                VBProject vbProject = GetPyxelRestVBProject();
                if (vbProject == null)
                {
                    Log.Error("PyxelRest VB Project cannot be found.");
                    return;
                }
                vbProject.VBComponents.Import(pathToBasFile);
                Log.Info("XLWings module imported.");
            }
            catch (Exception ex)
            {
                Log.Error("XlWings module could not be imported.", ex);
            };
        }

        private VBProject GetPyxelRestVBProject()
        {
            foreach (VBProject vb in Application.VBE.VBProjects)
            {
                if ("PyxelRest".Equals(vb.Name))
                    return vb;
            }
            return null;
        }

        private string GetPathToXlWingsBasFile()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if(appDataFolder != null)
                return System.IO.Path.Combine(appDataFolder, "pyxelrest", "xlwings.bas");
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

        private bool RemoveXlWingsModule(VBComponent vbComponent)
        {
            try
            {
                VBProject vbProject = GetPyxelRestVBProject();
                if(vbProject == null)
                {
                    Log.Error("PyxelRest VB Project cannot be found.");
                    return false;
                }
                vbProject.VBComponents.Remove(vbComponent);
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
