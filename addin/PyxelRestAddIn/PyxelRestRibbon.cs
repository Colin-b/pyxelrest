using Microsoft.Office.Tools.Ribbon;
using System.Diagnostics;
using System.Windows.Forms;
using System.Configuration;
using log4net;
using Microsoft.Win32;
using System;

namespace PyxelRestAddIn
{
    public partial class PyxelRestRibbon
    {
        private static readonly ILog Log = LogManager.GetLogger("PyxelRestRibbon");
        private static readonly string UDF_IMPORT_FAILURE_MSG = 
            "User Defined Functions cannot be loaded.\n"+
            "Check logs for more details or contact your support team.\n";

        private void PyxelRestRibbon_Load(object sender, RibbonUIEventArgs e)
        {
            generateUDFAtStartupButton.Checked = ThisAddIn.GenerateUDFAtStartup();
            generateUDFAtStartupButton.Label = string.Format("Functions are {0}generated at startup", generateUDFAtStartupButton.Checked ? "": "NOT ");
            
            string autoCheckForUpdates = ThisAddIn.GetSetting("AutoCheckForUpdates");
            // Do not allow to check for update if the parameter is not set in configuration
            autoUpdateButton.Enabled = !string.IsNullOrEmpty(autoCheckForUpdates);
            autoUpdateButton.Checked = "True".Equals(autoCheckForUpdates);
            autoUpdateButton.Label = string.Format("Automatic update is {0}", autoUpdateButton.Checked ? "enabled" : "disabled");

            string checkPreReleases = ThisAddIn.GetSetting("CheckPreReleases");
            installDevelopmentReleasesButton.Enabled = autoUpdateButton.Checked;
            installDevelopmentReleasesButton.Checked = "True".Equals(checkPreReleases);
            if (installDevelopmentReleasesButton.Checked)
                installDevelopmentReleasesButton.Label = "Update include unstable releases";
            else
                installDevelopmentReleasesButton.Label = "Update include stable releases only";

            pathToUpToDateConfEditBox.Text = ThisAddIn.GetPathToUpToDateConfiguration();

            pathToPythonEditBox.Text = ThisAddIn.GetSetting("PathToPython");
            customXlwingsPathEditBox.Text = ThisAddIn.GetSetting("PathToXlWingsBasFile");

            developerGroup.Label = string.Format("Excel {0} - Python {1}", Globals.ThisAddIn.GetVersion(), Globals.ThisAddIn.GetPyxelRestVersion(pathToPythonEditBox.Text));
        }

        private void ActivateOrDeactivateAutoUpdate(object sender, RibbonControlEventArgs e)
        {
            try
            {
                ((RibbonToggleButton)sender).Label = string.Format("Automatic update is {0}", ((RibbonToggleButton)sender).Checked ? "enabled" : "disabled");
                installDevelopmentReleasesButton.Enabled = ((RibbonToggleButton)sender).Checked;
                ThisAddIn.SetSetting("AutoCheckForUpdates", "" + ((RibbonToggleButton)sender).Checked);
                Log.DebugFormat("Auto check for update set to {0}", ((RibbonToggleButton)sender).Checked);
            }
            catch (ConfigurationErrorsException ex)
            {
                Log.Error("Unable to update configuration.", ex);
            }
        }

        private void ActivateOrDeactivateUDFGeneration(object sender, RibbonControlEventArgs e)
        {
            try
            {
                ((RibbonToggleButton)sender).Label = string.Format("Functions are {0}generated at startup", ((RibbonToggleButton)sender).Checked ? "" : "NOT ");
                ThisAddIn.SetSetting("GenerateUDFAtStartup", "" + ((RibbonToggleButton)sender).Checked);
                Log.DebugFormat("User defined functions generation at startup set to {0}", ((RibbonToggleButton)sender).Checked);
            }
            catch (ConfigurationErrorsException ex)
            {
                Log.Error("Unable to update configuration.", ex);
            }
        }

        private void OpenPyxelRestFolder(object sender, RibbonControlEventArgs e)
        {
            string installLocation = (string)Registry.GetValue(@"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest", "InstallLocation", null);
            if (installLocation != null)
            {
                string logsFolder = System.IO.Path.Combine(installLocation, "logs");
                if (!System.IO.Directory.Exists(logsFolder))
                {
                    Log.WarnFormat("{0} logs folder does not exists. Creating it.", logsFolder);
                    System.IO.Directory.CreateDirectory(logsFolder);
                }
                Process.Start(logsFolder);
            }
        }

        private void ConfigureServices(object sender, RibbonControlEventArgs e)
        {
            if (DialogResult.Yes == new ServiceConfigurationForm(ThisAddIn.GetPathToUpToDateConfiguration()).ShowDialog())
            {
                if (!Globals.ThisAddIn.ImportUserDefinedFunctions(reload:true))
                    MessageBox.Show(
                        UDF_IMPORT_FAILURE_MSG,
                        "Import failed",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Warning);
            }
        }

        private void ImportUserDefinedFunctions(object sender, RibbonControlEventArgs e)
        {
            if(!Globals.ThisAddIn.ImportUserDefinedFunctions(reload:true))
                MessageBox.Show(
                    UDF_IMPORT_FAILURE_MSG, 
                    "Import failed",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
        }

        private void CreateANewIssue(object sender, RibbonControlEventArgs e)
        {
            Process.Start("https://github.com/Colin-b/pyxelrest/issues/new");
        }

        private void ActivateOrDeactivatePreReleaseCheck(object sender, RibbonControlEventArgs e)
        {
            try
            {
                if (((RibbonToggleButton)sender).Checked)
                    ((RibbonToggleButton)sender).Label = "Update include unstable releases";
                else
                    ((RibbonToggleButton)sender).Label = "Update include stable releases only";
                ThisAddIn.SetSetting("CheckPreReleases", "" + ((RibbonToggleButton)sender).Checked);
                Log.DebugFormat("Check pre-releases during update set to {0}", ((RibbonToggleButton)sender).Checked);
            }
            catch (ConfigurationErrorsException ex)
            {
                Log.Error("Unable to update CheckPreReleases configuration.", ex);
            }
        }

        private void ChangeKnownConfigurations(object sender, RibbonControlEventArgs e)
        {
            try
            {
                Registry.SetValue(@"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest", "PathToUpToDateConfigurations", ((RibbonEditBox)sender).Text);
            }
            catch (Exception ex)
            {
                Log.Error("An error occurred while updating path to up to date configurations.", ex);
            }
        }

        private void ChangePythonPath(object sender, RibbonControlEventArgs e)
        {
            try
            {
                ThisAddIn.SetSetting("PathToPython", ((RibbonEditBox)sender).Text);
            }
            catch (ConfigurationErrorsException ex)
            {
                Log.Error("Unable to update PathToPython configuration.", ex);
            }
        }
    }
}
