using Microsoft.Office.Tools.Ribbon;
using System.Diagnostics;
using System.Windows.Forms;
using System;

namespace AutoLoadPyxelRestAddIn
{
    public partial class PyxelRestRibbon
    {
        private static readonly string UDF_IMPORT_FAILURE_MSG = 
            "User Defined Functions cannot be loaded.\n"+
            "Check logs for more details or contact your support team.\n";

        private void PyxelRestRibbon_Load(object sender, RibbonUIEventArgs e)
        {
            developerGroup.Label = string.Format("Version {0}", Globals.ThisAddIn.GetVersion()); 
            importButton.Click += ImportUserDefinedFunctions;
            configureButton.Click += ConfigureServices;
            openFolderButton.Click += OpenPyxelRestFolder;
        }

        private void OpenPyxelRestFolder(object sender, RibbonControlEventArgs e)
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if (appDataFolder != null)
                Process.Start(System.IO.Path.Combine(appDataFolder, "pyxelrest"));
        }

        private void ConfigureServices(object sender, RibbonControlEventArgs e)
        {
            if (DialogResult.Yes == new ServiceConfigurationForm().ShowDialog())
            {
                if (!Globals.ThisAddIn.ImportUserDefinedFunctions())
                    MessageBox.Show(
                        UDF_IMPORT_FAILURE_MSG,
                        "Import failed",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Warning);
            }
        }

        private void ImportUserDefinedFunctions(object sender, RibbonControlEventArgs e)
        {
            if(!Globals.ThisAddIn.ImportUserDefinedFunctions())
                MessageBox.Show(
                    UDF_IMPORT_FAILURE_MSG, 
                    "Import failed",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
        }
    }
}
