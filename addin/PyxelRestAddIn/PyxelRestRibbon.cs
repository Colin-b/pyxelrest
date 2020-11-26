using Microsoft.Office.Tools.Ribbon;
using System.Diagnostics;
using System.Windows.Forms;
using System.Configuration;
using log4net;
using Microsoft.Win32;
using System;
using System.IO;
using System.Drawing;
using System.Drawing.Imaging;

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
            generateUDFAtStartupButton.Image = generateUDFAtStartupButton.Checked ? Properties.Resources.refresh_128 : Properties.Resources.refresh_128_orange;

            string autoCheckForUpdates = ThisAddIn.GetSetting("AutoCheckForUpdates");
            // Do not allow to check for update if the parameter is not set in configuration
            autoUpdateButton.Enabled = !string.IsNullOrEmpty(autoCheckForUpdates);
            autoUpdateButton.Checked = "True".Equals(autoCheckForUpdates);
            autoUpdateButton.Label = string.Format("Automatic update is {0}", autoUpdateButton.Checked ? "enabled" : "disabled");
            autoUpdateButton.Image = autoUpdateButton.Checked ? Properties.Resources.data_transfer_download_128 : Properties.Resources.data_transfer_download_128_grey;

            string checkPreReleases = ThisAddIn.GetSetting("CheckPreReleases");
            installDevelopmentReleasesButton.Enabled = autoUpdateButton.Checked;
            installDevelopmentReleasesButton.Checked = "True".Equals(checkPreReleases);
            if (installDevelopmentReleasesButton.Checked)
            {
                installDevelopmentReleasesButton.Label = "Update include unstable releases";
                installDevelopmentReleasesButton.Image = Properties.Resources.data_transfer_download_128_orange;
            }
            else
            {
                installDevelopmentReleasesButton.Label = "Update include stable releases only";
                installDevelopmentReleasesButton.Image = Properties.Resources.data_transfer_download_128;
            }

            pathToUpToDateConfEditBox.Text = ThisAddIn.GetPathToUpToDateConfiguration();

            pathToPythonEditBox.Text = ThisAddIn.GetSetting("PathToPython");
            customXlwingsPathEditBox.Text = ThisAddIn.GetSetting("PathToXlWingsBasFile");

            developerGroup.Label = string.Format("Excel {0} - Python {1}", Globals.ThisAddIn.GetVersion(), Globals.ThisAddIn.GetPyxelRestVersion(pathToPythonEditBox.Text));

            if (!File.Exists(pathToPythonEditBox.Text))
            {
                developerOptionsGroup.Label = "Python path does not exists";
            }
            else
            {
                developerOptionsGroup.Label = "Advanced options seems to be valid";
            }
        }

        private void ActivateOrDeactivateAutoUpdate(object sender, RibbonControlEventArgs e)
        {
            try
            {
                ((RibbonToggleButton)sender).Label = string.Format("Automatic update is {0}", ((RibbonToggleButton)sender).Checked ? "enabled" : "disabled");
                installDevelopmentReleasesButton.Enabled = ((RibbonToggleButton)sender).Checked;
                ((RibbonToggleButton)sender).Image = ((RibbonToggleButton)sender).Checked ? Properties.Resources.data_transfer_download_128 : Properties.Resources.data_transfer_download_128_grey;
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
                ((RibbonToggleButton)sender).Image = ((RibbonToggleButton)sender).Checked ? Properties.Resources.refresh_128 : Properties.Resources.refresh_128_orange;
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
                {
                    ((RibbonToggleButton)sender).Label = "Update include unstable releases";
                    ((RibbonToggleButton)sender).Image = Properties.Resources.data_transfer_download_128_orange;
                }
                else
                {
                    ((RibbonToggleButton)sender).Label = "Update include stable releases only";
                    ((RibbonToggleButton)sender).Image = Properties.Resources.data_transfer_download_128;
                }
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
                if (!File.Exists(((RibbonEditBox)sender).Text))
                {
                    developerOptionsGroup.Label = "Python path does not exists";
                    return;
                }
                developerOptionsGroup.Label = "Advanced options seems to be valid";
                ThisAddIn.SetSetting("PathToPython", ((RibbonEditBox)sender).Text);
            }
            catch (ConfigurationErrorsException ex)
            {
                Log.Error("Unable to update PathToPython configuration.", ex);
            }
        }

        private Image SetImageOpacity(Image image, float opacity)
        {
            try
            {
                Bitmap bmp = new Bitmap(image.Width, image.Height);

                using (Graphics gfx = Graphics.FromImage(bmp))
                {
                    ColorMatrix matrix = new ColorMatrix
                    {
                        Matrix33 = opacity
                    };

                    ImageAttributes attributes = new ImageAttributes();

                    //set the color(opacity) of the image  
                    attributes.SetColorMatrix(matrix, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

                    //now draw the image  
                    gfx.DrawImage(image, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, attributes);
                }
                return bmp;
            }
            catch
            {
                return image;
            }
        }
    }
}
