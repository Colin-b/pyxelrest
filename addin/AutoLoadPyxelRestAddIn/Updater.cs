using log4net;
using System.Diagnostics;
using System.IO;
using System;

namespace AutoLoadPyxelRestAddIn
{
    internal class Updater
    {
        private static readonly ILog Log = LogManager.GetLogger("Updater");
        
        private readonly string pythonPath;
        private readonly string pathToUpdateScript;
        private readonly string pathToUpToDateConfigurations;
        private readonly bool checkPreReleases;

        internal Updater()
        {
            pythonPath = ThisAddIn.GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                throw new Exception(string.Format("Path to Python '{0}' cannot be found.", pythonPath));

            pathToUpdateScript = ThisAddIn.GetSetting("PathToUpdateScript");
            if (!File.Exists(pathToUpdateScript))
                throw new Exception(string.Format("PyxelRest auto update script '{0}' cannot be found.", pathToUpdateScript));

            pathToUpToDateConfigurations = ThisAddIn.GetSetting("PathToUpToDateConfigurations");
            if (!Boolean.TryParse(ThisAddIn.GetSetting("CheckPreReleases"), out checkPreReleases))
                checkPreReleases = false; // Do not check for pre-releases by default
        }

        internal void CheckUpdate()
        {
            string commandLine = this.pathToUpdateScript;
            if (!string.IsNullOrEmpty(pathToUpToDateConfigurations))
                commandLine += string.Format(" --path_to_up_to_date_configurations {0}", pathToUpToDateConfigurations);
            if (checkPreReleases)
                commandLine += " --check_pre_releases";

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
