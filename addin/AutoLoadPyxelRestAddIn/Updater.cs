using log4net;
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
            pipPath = ThisAddIn.GetSetting("PathToPIP");
            if (!File.Exists(pipPath))
                throw new FileNotFoundException("Path to PIP cannot be found.", pipPath);

            pythonPath = ThisAddIn.GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                throw new FileNotFoundException("Path to Python cannot be found.", pythonPath);

            update_script = ThisAddIn.GetSetting("PathToUpdateScript");
            if (!File.Exists(update_script))
                throw new FileNotFoundException("PyxelRest auto update script cannot be found.", update_script);
        }

        internal void CheckUpdate()
        {
            Log.Debug("Check for PyxelRest update.");
            Process updateScript = new Process();
            updateScript.StartInfo.FileName = pythonPath;
            updateScript.StartInfo.Arguments = string.Format("{0} {1}", update_script, pipPath);
            updateScript.StartInfo.UseShellExecute = false;
            updateScript.StartInfo.CreateNoWindow = true;
            updateScript.Start();
        }
    }
}
