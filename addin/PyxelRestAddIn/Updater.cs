using log4net;
using System.Diagnostics;
using System.IO;
using System;

namespace PyxelRestAddIn
{
    internal class Updater
    {
        private static readonly ILog Log = LogManager.GetLogger("Updater");
        
        private readonly string updateScriptPath;

        internal Updater(string pythonPath)
        {
            if (!File.Exists(pythonPath))
                throw new Exception(string.Format("Path to Python '{0}' cannot be found.", pythonPath));

            string scriptsPath = Path.GetDirectoryName(pythonPath);
            // python executable is in scripts folder in virtual environments, in root folder otherwise.
            if (!"Scripts".Equals(Path.GetFileName(scriptsPath)))
                scriptsPath = Path.Combine(scriptsPath, "Scripts");
            updateScriptPath = Path.Combine(scriptsPath, "pyxelrest_auto_update.exe");
            if (!File.Exists(updateScriptPath))
                throw new Exception(string.Format("PyxelRest auto update script '{0}' cannot be found.", updateScriptPath));
        }

        internal void CheckUpdate(bool checkPreReleases)
        {
            string commandLine = string.Empty;
            if (checkPreReleases)
                commandLine += " --check_pre_releases";

            Log.DebugFormat("Check for PyxelRest update: {0} {1}", updateScriptPath, commandLine);
            Process updateScript = new Process();
            updateScript.StartInfo.FileName = updateScriptPath;
            updateScript.StartInfo.Arguments = commandLine;
            updateScript.StartInfo.UseShellExecute = false;
            updateScript.StartInfo.CreateNoWindow = true;
            updateScript.Start();
        }
    }
}
