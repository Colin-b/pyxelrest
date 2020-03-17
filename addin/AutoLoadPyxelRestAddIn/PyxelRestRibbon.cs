using Microsoft.Office.Tools.Ribbon;
using System.Diagnostics;
using System.Windows.Forms;
using System;
using System.Configuration;
using log4net;

namespace AutoLoadPyxelRestAddIn
{
    public partial class PyxelRestRibbon
    {
        private static readonly ILog Log = LogManager.GetLogger("PyxelRestRibbon");
        private static readonly string UDF_IMPORT_FAILURE_MSG = 
            "User Defined Functions cannot be loaded.\n"+
            "Check logs for more details or contact your support team.\n";

        private void PyxelRestRibbon_Load(object sender, RibbonUIEventArgs e)
        {
            developerGroup.Label = string.Format("Excel {0} - Python {1}", Globals.ThisAddIn.GetVersion(), Globals.ThisAddIn.GetPyxelRestVersion());

            string autoCheckForUpdates = ThisAddIn.GetSetting("AutoCheckForUpdates");
            // Do not allow to check for update if the parameter is not set in configuration
            autoUpdateButton.Enabled = !string.IsNullOrEmpty(autoCheckForUpdates);
            autoUpdateButton.Checked = "True".Equals(autoCheckForUpdates);
            autoUpdateButton.Click += ActivateOrDeactivateAutoUpdate;

            generateUDFAtStartupButton.Checked = ThisAddIn.GenerateUDFAtStartup();

            importButton.Click += ImportUserDefinedFunctions;
            configureButton.Click += ConfigureServices;
            openFolderButton.Click += OpenPyxelRestFolder;
        }

        private void ActivateOrDeactivateAutoUpdate(object sender, RibbonControlEventArgs e)
        {
            try
            {
                ThisAddIn.SetSetting("AutoCheckForUpdates", "" + autoUpdateButton.Checked);
                Log.DebugFormat("Auto check for update set to {0}", autoUpdateButton.Checked);
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
                ThisAddIn.SetSetting("GenerateUDFAtStartup", "" + generateUDFAtStartupButton.Checked);
                Log.DebugFormat("User defined functions generation at startup set to {0}", generateUDFAtStartupButton.Checked);
            }
            catch (ConfigurationErrorsException ex)
            {
                Log.Error("Unable to update configuration.", ex);
            }
        }

        private void OpenPyxelRestFolder(object sender, RibbonControlEventArgs e)
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if (appDataFolder != null)
            {
                string logsFolder = System.IO.Path.Combine(appDataFolder, "pyxelrest", "logs");
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
            if (DialogResult.Yes == new ServiceConfigurationForm().ShowDialog())
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
    }
}
