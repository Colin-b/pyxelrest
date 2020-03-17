using log4net;
using System.Diagnostics;
using System.IO;
using System;

namespace AutoLoadPyxelRestAddIn
{
    internal class Updater
    {
        private static readonly ILog Log = LogManager.GetLogger("Updater");
        
        private readonly string updateScriptPath;
        private readonly string pathToUpToDateConfigurations;
        private readonly bool checkPreReleases;

        internal Updater()
        {
            string pythonPath = ThisAddIn.GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                throw new Exception(string.Format("Path to Python '{0}' cannot be found.", pythonPath));

            updateScriptPath = Path.Combine(Path.GetDirectoryName(pythonPath), "pyxelrest_auto_update.exe");
            if (!File.Exists(updateScriptPath))
                throw new Exception(string.Format("PyxelRest auto update script '{0}' cannot be found.", updateScriptPath));

            pathToUpToDateConfigurations = ThisAddIn.GetSetting("PathToUpToDateConfigurations");
            if (!bool.TryParse(ThisAddIn.GetSetting("CheckPreReleases"), out checkPreReleases))
                checkPreReleases = false; // Do not check for pre-releases by default
        }

        internal void CheckUpdate()
        {
            string commandLine = string.Empty;
            if (!string.IsNullOrEmpty(pathToUpToDateConfigurations))
                commandLine += string.Format(" --path_to_up_to_date_configurations {0}", pathToUpToDateConfigurations);
            if (checkPreReleases)
                commandLine += " --check_pre_releases";

            Log.Debug("Check for PyxelRest update.");
            Process updateScript = new Process();
            updateScript.StartInfo.FileName = updateScriptPath;
            updateScript.StartInfo.Arguments = commandLine;
            updateScript.StartInfo.UseShellExecute = false;
            updateScript.StartInfo.CreateNoWindow = true;
            updateScript.Start();
        }
    }
}
