using log4net;
using System.Diagnostics;
using System;
using System.Xml;
using System.Net;
using System.Windows.Forms;
using System.IO;
using System.Linq;

namespace PyxelRestAddIn
{
    internal class Updater
    {
        private static readonly ILog Log = LogManager.GetLogger("Updater");

        // Check update once per hour
        private static readonly int UPDATE_CHECK_INTERVAL_MS = 60 * 60 * 1000;

        internal bool InstallPreRelease;
        private readonly string CurrentVersion;
        private readonly bool IsUnstableCurrentVersion;
        private readonly string StableCurrentVersion;
        private readonly Timer Check;

        internal Updater(string currentVersion, bool installPreRelease)
        {
            InstallPreRelease = installPreRelease;
            CurrentVersion = currentVersion;
            // X.Y.Z is a stable version while X.Y.Z.dev0 is a pre-release
            IsUnstableCurrentVersion = CurrentVersion.Count(c => c == '.') != 2;
            StableCurrentVersion = CurrentVersion.Substring(0, IsUnstableCurrentVersion ? CurrentVersion.Length : CurrentVersion.LastIndexOf('.'));

            Check = new Timer { Interval = UPDATE_CHECK_INTERVAL_MS };
            Check.Tick += Check_Tick;
        }

        internal void StartCheck()
        {
            Check.Start();
        }

        internal void StopCheck()
        {
            Check.Stop();
        }

        private void Check_Tick(object sender, EventArgs e)
        {
            try
            {
                CheckUpdate();
            }
            catch (Exception ex)
            {
                Log.Error("Unable to check update.", ex);
            }
        }

        private void CheckUpdate()
        {
            HttpWebResponse response = HttpHelper.ConnectTo("https://pypi.org/rss/project/pyxelrest/releases.xml");
            if (response == null || response.StatusCode != HttpStatusCode.OK)
            {
                string details = response == null ? "" : response.StatusDescription;
                Log.ErrorFormat("pyxelrest releases cannot be retrieved from https://pypi.org/rss/project/pyxelrest/releases.xml: {0}.", details);
                if (response != null)
                    response.Close();
                return;
            }
            XmlTextReader reader = new XmlTextReader(response.GetResponseStream());
            while (reader.Read())
            {
                if (reader.NodeType == XmlNodeType.Element && "title".Equals(reader.Name))
                {
                    reader.Read();
                    if (!"PyPI recent updates for pyxelrest".Equals(reader.Value))
                    {
                        var version = reader.Value;
                        if (IsNewVersion(version))
                        {
                            if (DialogResult.Yes == MessageBox.Show(
                                string.Format("Upgrade to PyxelRest {0}?", version),
                                "Update is available",
                                MessageBoxButtons.YesNo,
                                MessageBoxIcon.Information))
                            {
                                DownloadLatestVersion(version);
                            }
                            else
                            {
                                Log.Debug("Update skipped upon user request.");
                            }
                            return;
                        }
                    }
                }
            }
        }

        private bool IsNewVersion(string version)
        {
            // X.Y.Z is a stable version while X.Y.Z.dev0 is a pre-release
            var isStableVersion = version.Count(c => c == '.') == 2;
            var stableVersion = version.Substring(0, isStableVersion ? version.Length : version.LastIndexOf('.'));

            if (isStableVersion)
                if (IsUnstableCurrentVersion)
                    // Compare X.Y.Z to X.Y.Z.dev0 (current) -> use X.Y.Z vs X.Y.Z
                    return string.Compare(stableVersion, StableCurrentVersion) != -1;
                else
                    // Compare X.Y.Z to X.Y.Z (current) -> use X.Y.Z vs X.Y.Z
                    return string.Compare(stableVersion, StableCurrentVersion) == 1;

            // This is an unstable version

            if (IsUnstableCurrentVersion)
                // Compare X.Y.Z.dev0 to X.Y.Z.dev0 (current) -> use X.Y.Z.dev0 vs X.Y.Z.dev0
                return InstallPreRelease && (string.Compare(version, CurrentVersion) == 1);
            else
                // Compare X.Y.Z.dev0 to X.Y.Z (current) -> use X.Y.Z vs X.Y.Z
                return InstallPreRelease && (string.Compare(stableVersion, StableCurrentVersion) == 1);
        }

        private void DownloadLatestVersion(string version)
        {
            Log.Debug("Downloading new version installer.");
            using (var client = new WebClient())
            {
                try
                {
                    var installerPath = Path.GetTempFileName();
                    client.DownloadFile("https://raw.githubusercontent.com/Colin-b/pyxelrest/master/pyxelrest_installer.exe", installerPath);
                    LaunchInstallation(installerPath);
                }
                catch (Exception ex)
                {
                    Log.Error("Unable to perform installation of a new version.", ex);
                    MessageBox.Show(
                        string.Format("PyxelRest could not be updated to {0}.\n{1}", version, ex.Message),
                        "Update failed",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Warning
                    );
                }
            }
        }

        private void LaunchInstallation(string installerPath)
        {
            Log.DebugFormat("Launching installer located in {0}", installerPath);
            Process updateScript = new Process();
            updateScript.StartInfo.FileName = installerPath;
            updateScript.StartInfo.UseShellExecute = false;
            updateScript.StartInfo.CreateNoWindow = true;
            updateScript.Start();
        }
    }
}
