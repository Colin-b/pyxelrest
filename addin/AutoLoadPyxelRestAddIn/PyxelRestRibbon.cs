using Microsoft.Office.Tools.Ribbon;

namespace AutoLoadPyxelRestAddIn
{
    public partial class PyxelRestRibbon
    {
        private static readonly string UDF_IMPORT_FAILURE_MSG = 
            "User Defined Functions cannot be loaded.\n"+
            "Please check that you trust access to Visual Basic Project\n";

        private void PyxelRestRibbon_Load(object sender, RibbonUIEventArgs e)
        {
            importButton.Click += ImportUserDefinedFunctions;
        }

        private void ImportUserDefinedFunctions(object sender, RibbonControlEventArgs e)
        {
            if(!Globals.ThisAddIn.ImportUserDefinedFunctions())
                System.Windows.Forms.MessageBox.Show(
                    UDF_IMPORT_FAILURE_MSG, 
                    "Import failed",
                    System.Windows.Forms.MessageBoxButtons.OK,
                    System.Windows.Forms.MessageBoxIcon.Warning);
        }
    }
}
