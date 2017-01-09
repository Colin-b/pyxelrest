namespace AutoLoadPyxelRestAddIn
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
            this.tab1 = this.Factory.CreateRibbonTab();
            this.group1 = this.Factory.CreateRibbonGroup();
            this.importButton = this.Factory.CreateRibbonButton();
            this.configureButton = this.Factory.CreateRibbonButton();
            this.tab1.SuspendLayout();
            this.group1.SuspendLayout();
            this.SuspendLayout();
            // 
            // tab1
            // 
            this.tab1.Groups.Add(this.group1);
            this.tab1.Label = "PyxelRest";
            this.tab1.Name = "tab1";
            // 
            // group1
            // 
            this.group1.Items.Add(this.importButton);
            this.group1.Items.Add(this.configureButton);
            this.group1.Label = "User Defined Functions";
            this.group1.Name = "group1";
            // 
            // importButton
            // 
            this.importButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.importButton.Description = "Update User Defined Functions";
            this.importButton.Image = global::AutoLoadPyxelRestAddIn.Properties.Resources.refresh_128;
            this.importButton.ImageName = "Update Functions";
            this.importButton.Label = "Update Functions";
            this.importButton.Name = "importButton";
            this.importButton.ShowImage = true;
            // 
            // configureButton
            // 
            this.configureButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.configureButton.Description = "Configure Services";
            this.configureButton.Image = global::AutoLoadPyxelRestAddIn.Properties.Resources.settings_8_128;
            this.configureButton.ImageName = "Configure Services";
            this.configureButton.Label = "Configure Services";
            this.configureButton.Name = "configureButton";
            this.configureButton.ShowImage = true;
            // 
            // PyxelRestRibbon
            // 
            this.Name = "PyxelRestRibbon";
            this.RibbonType = "Microsoft.Excel.Workbook";
            this.Tabs.Add(this.tab1);
            this.Load += new Microsoft.Office.Tools.Ribbon.RibbonUIEventHandler(this.PyxelRestRibbon_Load);
            this.tab1.ResumeLayout(false);
            this.tab1.PerformLayout();
            this.group1.ResumeLayout(false);
            this.group1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        internal Microsoft.Office.Tools.Ribbon.RibbonTab tab1;
        internal Microsoft.Office.Tools.Ribbon.RibbonGroup group1;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton importButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton configureButton;
    }

    partial class ThisRibbonCollection
    {
        internal PyxelRestRibbon PyxelRestRibbon
        {
            get { return this.GetRibbon<PyxelRestRibbon>(); }
        }
    }
}
