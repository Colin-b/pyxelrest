using log4net;
using System.Configuration;
using System.Diagnostics;
using System.IO;

namespace AutoLoadPyxelRestAddIn
{
    class Updater
    {
        private static readonly ILog Log = LogManager.GetLogger("Updater");

        private readonly string pipPath;
        private readonly string pythonPath;
        private readonly string update_script;

        internal Updater()
        {
            pipPath = ConfigurationManager.AppSettings["PathToPIP"];
            if (pipPath == null || !File.Exists(pipPath))
                throw new FileNotFoundException("Path to PIP cannot be found.");

            pythonPath = ConfigurationManager.AppSettings["PathToPython"];
            if (pythonPath == null || !File.Exists(pythonPath))
                throw new FileNotFoundException("Path to Python cannot be found.");

            update_script = ConfigurationManager.AppSettings["PathToUpdateScript"];
            if (update_script == null || !File.Exists(update_script))
                throw new FileNotFoundException("PyxelRest auto update script cannot be found.");
        }

        internal void CheckUpdate()
        {
            Log.Debug("Check for PyxelRest update.");
            Process updateScript = new Process();
            updateScript.StartInfo.FileName = pythonPath;
            updateScript.StartInfo.Arguments = string.Format("{0} --path_to_pip {1}", update_script, pipPath);
            updateScript.StartInfo.UseShellExecute = false;
            updateScript.StartInfo.CreateNoWindow = true;
            updateScript.Start();
        }
    }
}
