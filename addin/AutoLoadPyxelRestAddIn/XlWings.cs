using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using Microsoft.Office.Interop.Excel;
using log4net;

namespace AutoLoadPyxelRestAddIn
{
    // TODO Rename all XLWings naming into understandable code
    class XlWings64Dll
    {
        [DllImport("xlwings64.dll", EntryPoint = "XLPyDLLActivateAuto", SetLastError = true)]
        public static extern IntPtr XLPyDLLActivateAuto(object result, string Config, long mode);
    }

    class XlWings32Dll
    {
        [DllImport("xlwings32.dll", EntryPoint = "XLPyDLLActivateAuto", SetLastError = true)]
        public static extern IntPtr XLPyDLLActivateAuto(object result, string Config, int mode);
    }

    class XlWingsInterface
    {
        internal void Call(object p1, string v, object p2)
        {
            // TODO
        }

        internal object Module(string v)
        {
            // TODO
            return null;
        }

        internal object Tuple(string v, Workbook activeWorkbook)
        {
            // TODO
            return null;
        }
    }

    class XlWings
    {
        private static readonly ILog Log = LogManager.GetLogger("XlWings");

        // TODO If not working try LoadLibrary
        [DllImport("kernel32.dll", EntryPoint = "LoadLibraryA", SetLastError = true)]
        public static extern IntPtr LoadLibrary(string lpFileName);

        private static readonly bool Win64 = IntPtr.Size == 8;
        private static readonly string XLPyDLLName = Win64 ? "xlwings64.dll" : "xlwings32.dll";
        

        private string PYTHON_WIN = @"c:\users\js5391\PycharmProjects\pyxelrest\env\scripts\pythonw.exe";
        private string PYTHONPATH = @"c:\users\js5391\PycharmProjects\pyxelrest\pyxelrest";
        private bool DEBUG_UDFS = false;
        private string UDF_MODULES = "pyxelrestgenerator";
        

        private void LoadConfig(Microsoft.Office.Interop.Excel.Workbook ActiveWorkbook)
        {
            PYTHON_WIN = GetConfig("INTERPRETER", "pythonw");
            PYTHONPATH = ActiveWorkbook.Path + ";" + GetConfig("PYTHONPATH", "");
            DEBUG_UDFS = bool.Parse(GetConfig("DEBUG UDFS", "false"));
            UDF_MODULES = GetConfig("UDF MODULES", "");
        }

        private string ParentFolder(string path)
        {
            return Directory.GetParent(path).FullName;
        }

        private void XLPyLoadDLL()
        {
            // Standard Installation
            if (LoadLibrary(ParentFolder(PYTHON_WIN) + "\\" + XLPyDLLName) == IntPtr.Zero)
            {
                // Virtual Environment
                if (LoadLibrary(ParentFolder(ParentFolder(PYTHON_WIN)) + "\\" + XLPyDLLName) == IntPtr.Zero)
                    throw new Exception(string.Format("'{0}' cannot be found within {1} parent folders.", XLPyDLLName, PYTHON_WIN));
            }
            Log.DebugFormat("'{0}' successfully loaded.");
        }

        private void XLPyDLLActivateAuto(object result, string Config, int mode)
        {
            if (Win64)
            {
                if (XlWings64Dll.XLPyDLLActivateAuto(result, Config, mode) == IntPtr.Zero)
                {
                    // TODO Log and display error }
                }
            }
            else
            {
                if (XlWings32Dll.XLPyDLLActivateAuto(result, Config, mode) == IntPtr.Zero)
                {
                    // TODO Log and display error }
                }
            }
        }

        private XlWingsInterface Py()
        {
            XLPyLoadDLL();
            XlWingsInterface xlwings = new XlWingsInterface();
            XLPyDLLActivateAuto(xlwings, XLPyCommand(), 1);
            return xlwings;
        }

        private void KillPy()
        {
            XLPyLoadDLL();
            XLPyDLLActivateAuto(null, XLPyCommand(), -1);
        }

        private string XLPyCommand()
        {
            if (DEBUG_UDFS)
                return "{506e67c3-55b5-48c3-a035-eed5deea7d6d}";

            string tail = " -B -c \"\"import sys, os;sys.path.extend(os.path.normcase(os.path.expandvars(r'" + PYTHONPATH + "')).split(';'));import xlwings.server; xlwings.server.serve('$(CLSID)')\"\"";
            return PYTHON_WIN + tail;
        }

        private string GetUdfModules(Microsoft.Office.Interop.Excel.Workbook ActiveWorkbook)
        {
            if (string.IsNullOrEmpty(UDF_MODULES))
                // TODO it assume that it ends in .xlsm ...
                return ActiveWorkbook.Name.Substring(0, ActiveWorkbook.Name.Length - 5);
            return UDF_MODULES;
        }

        public void ImportPythonUDFs(Microsoft.Office.Interop.Excel.Workbook ActiveWorkbook)
        {
            try
            {
                // KillPy();
                XlWingsInterface xlwings = Py();
                xlwings.Call(xlwings.Module("xlwings"), "import_udfs", xlwings.Tuple(GetUdfModules(ActiveWorkbook), ActiveWorkbook));
            }
            catch (Exception e)
            {
                // TODO Log and display error
                Log.Error("Unable to import User Defined Functions.", e);
            }
        }

        private string GetConfig(string key, string defaultValue)
        {
            // TODO Load from conf
            return defaultValue;
        }
    }
}
