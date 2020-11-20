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
            this.autoUpdateButton = this.Factory.CreateRibbonToggleButton();
            this.generateUDFAtStartupButton = this.Factory.CreateRibbonToggleButton();
            this.openFolderButton = this.Factory.CreateRibbonButton();
            this.pyxelrestTab.SuspendLayout();
            this.udfGroup.SuspendLayout();
            this.developerGroup.SuspendLayout();
            this.SuspendLayout();
            // 
            // pyxelrestTab
            // 
            this.pyxelrestTab.Groups.Add(this.udfGroup);
            this.pyxelrestTab.Groups.Add(this.developerGroup);
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
            // 
            // developerGroup
            // 
            this.developerGroup.Items.Add(this.autoUpdateButton);
            this.developerGroup.Items.Add(this.generateUDFAtStartupButton);
            this.developerGroup.Items.Add(this.openFolderButton);
            this.developerGroup.Label = "Excel X.Y.Z - Python A.B.C";
            this.developerGroup.Name = "developerGroup";
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
    }

    partial class ThisRibbonCollection
    {
        internal PyxelRestRibbon PyxelRestRibbon
        {
            get { return this.GetRibbon<PyxelRestRibbon>(); }
        }
    }
}
