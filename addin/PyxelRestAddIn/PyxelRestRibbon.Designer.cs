namespace PyxelRestAddIn
{
    partial class PyxelRestRibbon : Microsoft.Office.Tools.Ribbon.RibbonBase
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        public PyxelRestRibbon()
            : base(Globals.Factory.GetRibbonFactory())
        {
            InitializeComponent();
        }

        /// <summary> 
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Component Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pyxelrestTab = this.Factory.CreateRibbonTab();
            this.udfGroup = this.Factory.CreateRibbonGroup();
            this.importButton = this.Factory.CreateRibbonButton();
            this.configureButton = this.Factory.CreateRibbonButton();
            this.developerGroup = this.Factory.CreateRibbonGroup();
            this.generateUDFAtStartupButton = this.Factory.CreateRibbonToggleButton();
            this.autoUpdateButton = this.Factory.CreateRibbonToggleButton();
            this.installDevelopmentReleasesButton = this.Factory.CreateRibbonToggleButton();
            this.openFolderButton = this.Factory.CreateRibbonButton();
            this.createIssueButton = this.Factory.CreateRibbonButton();
            this.developerOptionsGroup = this.Factory.CreateRibbonGroup();
            this.pathToUpToDateConfEditBox = this.Factory.CreateRibbonEditBox();
            this.pathToPythonEditBox = this.Factory.CreateRibbonEditBox();
            this.customXlwingsPathEditBox = this.Factory.CreateRibbonEditBox();
            this.pyxelrestTab.SuspendLayout();
            this.udfGroup.SuspendLayout();
            this.developerGroup.SuspendLayout();
            this.developerOptionsGroup.SuspendLayout();
            this.SuspendLayout();
            // 
            // pyxelrestTab
            // 
            this.pyxelrestTab.Groups.Add(this.udfGroup);
            this.pyxelrestTab.Groups.Add(this.developerGroup);
            this.pyxelrestTab.Groups.Add(this.developerOptionsGroup);
            this.pyxelrestTab.Label = "PyxelRest";
            this.pyxelrestTab.Name = "pyxelrestTab";
            // 
            // udfGroup
            // 
            this.udfGroup.Items.Add(this.importButton);
            this.udfGroup.Items.Add(this.configureButton);
            this.udfGroup.Label = "User Defined Functions";
            this.udfGroup.Name = "udfGroup";
            // 
            // importButton
            // 
            this.importButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.importButton.Description = "Update User Defined Functions";
            this.importButton.Image = global::PyxelRestAddIn.Properties.Resources.refresh_128;
            this.importButton.ImageName = "Update Functions";
            this.importButton.Label = "Update Functions";
            this.importButton.Name = "importButton";
            this.importButton.ScreenTip = "Update Functions";
            this.importButton.ShowImage = true;
            this.importButton.SuperTip = "Reload the list of available UDFs.";
            this.importButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.ImportUserDefinedFunctions);
            // 
            // configureButton
            // 
            this.configureButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.configureButton.Description = "Configure Services";
            this.configureButton.Image = global::PyxelRestAddIn.Properties.Resources.settings_8_128;
            this.configureButton.ImageName = "Configure Services";
            this.configureButton.Label = "Configure Services";
            this.configureButton.Name = "configureButton";
            this.configureButton.ScreenTip = "Configure Services";
            this.configureButton.ShowImage = true;
            this.configureButton.SuperTip = "Open a window to configure available services.";
            this.configureButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.ConfigureServices);
            // 
            // developerGroup
            // 
            this.developerGroup.Items.Add(this.generateUDFAtStartupButton);
            this.developerGroup.Items.Add(this.autoUpdateButton);
            this.developerGroup.Items.Add(this.installDevelopmentReleasesButton);
            this.developerGroup.Items.Add(this.openFolderButton);
            this.developerGroup.Items.Add(this.createIssueButton);
            this.developerGroup.Label = "Excel X.Y.Z - Python A.B.C";
            this.developerGroup.Name = "developerGroup";
            // 
            // generateUDFAtStartupButton
            // 
            this.generateUDFAtStartupButton.Checked = true;
            this.generateUDFAtStartupButton.Image = global::PyxelRestAddIn.Properties.Resources.refresh_128;
            this.generateUDFAtStartupButton.ImageName = "Generate user defined functions at startup";
            this.generateUDFAtStartupButton.Label = "Generate UDFs at startup";
            this.generateUDFAtStartupButton.Name = "generateUDFAtStartupButton";
            this.generateUDFAtStartupButton.ScreenTip = "Generate user defined functions at startup";
            this.generateUDFAtStartupButton.ShowImage = true;
            this.generateUDFAtStartupButton.SuperTip = "Generate user defined functions at Microsoft Excel startup";
            this.generateUDFAtStartupButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.ActivateOrDeactivateUDFGeneration);
            // 
            // autoUpdateButton
            // 
            this.autoUpdateButton.Checked = true;
            this.autoUpdateButton.Image = global::PyxelRestAddIn.Properties.Resources.data_transfer_download_128;
            this.autoUpdateButton.ImageName = "Automatic check for update";
            this.autoUpdateButton.Label = "Check for update on close";
            this.autoUpdateButton.Name = "autoUpdateButton";
            this.autoUpdateButton.ScreenTip = "Check for update on close";
            this.autoUpdateButton.ShowImage = true;
            this.autoUpdateButton.SuperTip = "Check for update once Microsoft Excel is closed.";
            this.autoUpdateButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.ActivateOrDeactivateAutoUpdate);
            // 
            // installDevelopmentReleasesButton
            // 
            this.installDevelopmentReleasesButton.Image = global::PyxelRestAddIn.Properties.Resources.data_transfer_download_128;
            this.installDevelopmentReleasesButton.ImageName = "Check for pre-releases";
            this.installDevelopmentReleasesButton.Label = "Install development releases";
            this.installDevelopmentReleasesButton.Name = "installDevelopmentReleasesButton";
            this.installDevelopmentReleasesButton.ScreenTip = "Install development releases";
            this.installDevelopmentReleasesButton.ShowImage = true;
            this.installDevelopmentReleasesButton.SuperTip = "Include pre-releases when checking for updates";
            this.installDevelopmentReleasesButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.ActivateOrDeactivatePreReleaseCheck);
            // 
            // openFolderButton
            // 
            this.openFolderButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.openFolderButton.Description = "Open PyxelRest logs folder";
            this.openFolderButton.Image = global::PyxelRestAddIn.Properties.Resources.folder_3_128;
            this.openFolderButton.ImageName = "Open Logs Folder";
            this.openFolderButton.Label = "Open Logs";
            this.openFolderButton.Name = "openFolderButton";
            this.openFolderButton.ScreenTip = "Open Logs";
            this.openFolderButton.ShowImage = true;
            this.openFolderButton.SuperTip = "Open the folder containing PyxelRest logs.";
            this.openFolderButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.OpenPyxelRestFolder);
            // 
            // createIssueButton
            // 
            this.createIssueButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.createIssueButton.Description = "Report an issue occurring with PyxelRest";
            this.createIssueButton.Image = global::PyxelRestAddIn.Properties.Resources.help_128;
            this.createIssueButton.ImageName = "Report an issue";
            this.createIssueButton.Label = "Report an issue";
            this.createIssueButton.Name = "createIssueButton";
            this.createIssueButton.ScreenTip = "Report an issue";
            this.createIssueButton.ShowImage = true;
            this.createIssueButton.SuperTip = "Report an issue to PyxelRest developers";
            this.createIssueButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.CreateANewIssue);
            // 
            // developerOptionsGroup
            // 
            this.developerOptionsGroup.Items.Add(this.pathToUpToDateConfEditBox);
            this.developerOptionsGroup.Items.Add(this.pathToPythonEditBox);
            this.developerOptionsGroup.Items.Add(this.customXlwingsPathEditBox);
            this.developerOptionsGroup.Label = "Developer options";
            this.developerOptionsGroup.Name = "developerOptionsGroup";
            // 
            // pathToUpToDateConfEditBox
            // 
            this.pathToUpToDateConfEditBox.Label = "Predefined configurations";
            this.pathToUpToDateConfEditBox.Name = "pathToUpToDateConfEditBox";
            this.pathToUpToDateConfEditBox.ScreenTip = "Path to up-to-date configurations";
            this.pathToUpToDateConfEditBox.SizeString = "C:\\Users\\ThisIsAnExtraLongUserIdentifier\\AppData\\Local\\Programs\\Python\\Python39\\p" +
    "ythonw.exe";
            this.pathToUpToDateConfEditBox.SuperTip = "Path (or URL) to a a file or a folder containing up-to-date REST API configuratio" +
    "ns. Used to propose a list of already configured services and to maintain config" +
    "ured services up to date.";
            this.pathToUpToDateConfEditBox.Text = null;
            this.pathToUpToDateConfEditBox.TextChanged += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.ChangeKnownConfigurations);
            // 
            // pathToPythonEditBox
            // 
            this.pathToPythonEditBox.Label = "Python path";
            this.pathToPythonEditBox.Name = "pathToPythonEditBox";
            this.pathToPythonEditBox.ScreenTip = "Path to python executable";
            this.pathToPythonEditBox.SizeString = "C:\\Users\\ThisIsAnExtraLongUserIdentifier\\AppData\\Local\\Programs\\Python\\Python39\\p" +
    "ythonw.exe";
            this.pathToPythonEditBox.SuperTip = "Path to python executable (python.exe) where pyxelrest was installed";
            this.pathToPythonEditBox.Text = null;
            this.pathToPythonEditBox.TextChanged += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.ChangePythonPath);
            // 
            // customXlwingsPathEditBox
            // 
            this.customXlwingsPathEditBox.Enabled = false;
            this.customXlwingsPathEditBox.Label = "Custom xlwings path";
            this.customXlwingsPathEditBox.Name = "customXlwingsPathEditBox";
            this.customXlwingsPathEditBox.ScreenTip = "Path to xlwings BAS file";
            this.customXlwingsPathEditBox.SizeString = "C:\\Users\\ThisIsAnExtraLongUserIdentifier\\AppData\\Local\\Programs\\Python\\Python39\\p" +
    "ythonw.exe";
            this.customXlwingsPathEditBox.SuperTip = "Path to custom xlwings BAS file modified for pyxelrest";
            this.customXlwingsPathEditBox.Text = null;
            // 
            // PyxelRestRibbon
            // 
            this.Name = "PyxelRestRibbon";
            this.RibbonType = "Microsoft.Excel.Workbook";
            this.Tabs.Add(this.pyxelrestTab);
            this.Load += new Microsoft.Office.Tools.Ribbon.RibbonUIEventHandler(this.PyxelRestRibbon_Load);
            this.pyxelrestTab.ResumeLayout(false);
            this.pyxelrestTab.PerformLayout();
            this.udfGroup.ResumeLayout(false);
            this.udfGroup.PerformLayout();
            this.developerGroup.ResumeLayout(false);
            this.developerGroup.PerformLayout();
            this.developerOptionsGroup.ResumeLayout(false);
            this.developerOptionsGroup.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        internal Microsoft.Office.Tools.Ribbon.RibbonTab pyxelrestTab;
        internal Microsoft.Office.Tools.Ribbon.RibbonGroup udfGroup;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton importButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton configureButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonGroup developerGroup;
        internal Microsoft.Office.Tools.Ribbon.RibbonToggleButton autoUpdateButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton openFolderButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonToggleButton generateUDFAtStartupButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton createIssueButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonGroup developerOptionsGroup;
        internal Microsoft.Office.Tools.Ribbon.RibbonToggleButton installDevelopmentReleasesButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonEditBox pathToPythonEditBox;
        internal Microsoft.Office.Tools.Ribbon.RibbonEditBox customXlwingsPathEditBox;
        internal Microsoft.Office.Tools.Ribbon.RibbonEditBox pathToUpToDateConfEditBox;
    }

    partial class ThisRibbonCollection
    {
        internal PyxelRestRibbon PyxelRestRibbon
        {
            get { return this.GetRibbon<PyxelRestRibbon>(); }
        }
    }
}
