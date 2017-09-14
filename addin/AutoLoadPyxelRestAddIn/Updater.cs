using log4net;
using System.Diagnostics;
using System.IO;
using System;

namespace AutoLoadPyxelRestAddIn
{
    class Updater
    {
        private static readonly ILog Log = LogManager.GetLogger("Updater");

        private readonly string pipPath;
        private readonly string pythonPath;
        private readonly string update_script;
        private readonly string path_to_up_to_date_configurations;

        internal Updater()
        {
            pythonPath = ThisAddIn.GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                throw new Exception(string.Format("Path to Python '{0}' cannot be found.", pythonPath));

            update_script = ThisAddIn.GetSetting("PathToUpdateScript");
            if (!File.Exists(update_script))
                throw new Exception(string.Format("PyxelRest auto update script '{0}' cannot be found.", update_script));

            path_to_up_to_date_configurations = ThisAddIn.GetSetting("PathToUpToDateConfigurations");
        }

        internal void CheckUpdate()
        {
            string commandLine = update_script;
            if (!string.IsNullOrEmpty(path_to_up_to_date_configurations))
                commandLine += string.Format(" --path_to_up_to_date_configurations {0}", path_to_up_to_date_configurations);

            Log.Debug("Check for PyxelRest update.");
            Process updateScript = new Process();
            updateScript.StartInfo.FileName = pythonPath;
            updateScript.StartInfo.Arguments = commandLine;
            updateScript.StartInfo.UseShellExecute = false;
            updateScript.StartInfo.CreateNoWindow = true;
            updateScript.Start();
        }
    }
}
