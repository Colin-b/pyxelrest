using log4net;
using System;
using System.Drawing;
using System.Windows.Forms;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class ServicePanel
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private readonly ServiceConfigurationForm configurationForm;  // Parent panel
        internal readonly TableLayoutPanel servicePanel;  // This panel
        private CheckBox checkbox;  // The accordion linking this panel to the parent panel

        #region Service fields

        private TextBox openAPIDefinition;
        private AdvancedConfigurationForm advancedConfigurationForm;

        #endregion

        internal readonly Service service;

        internal long? openAPIDefinitionTicks;

        public ServicePanel(ServiceConfigurationForm configurationForm, Service service)
        {
            this.configurationForm = configurationForm;
            this.service = service;
            servicePanel = DefaultPanel();
        }

        public override string ToString()
        {
            return service.ToString();
        }

        internal bool IsValid()
        {
            return service.Name.Equals("pyxelrest") || openAPIDefinition.TextLength > 0;
        }

        internal void CheckHostReachability()
        {
            if (openAPIDefinitionTicks != null && DateTime.UtcNow.Ticks >= openAPIDefinitionTicks + ServiceConfigurationForm.CHECK_HOST_INTERVAL_TICKS)
            {
                openAPIDefinition.BackColor = UrlChecker.CanReachOpenAPIDefinition(openAPIDefinition.Text, advancedConfigurationForm.GetProxyFor(openAPIDefinition.Text)) ? Color.LightGreen : Color.Red;
                openAPIDefinitionTicks = null;
            }
        }

        internal bool Exists(string serviceName)
        {
            return service.Name.Equals(serviceName);
        }

        internal void UpdateFrom(Service updated)
        {
            service.UpdateFrom(updated);
        }

        internal void Display(bool expanded)
        {
            checkbox = configurationForm.accordion.Add(servicePanel, service.Description(), open: expanded);
        }

        private TableLayoutPanel DefaultPanel()
        {
            var servicePanel = new TableLayoutPanel { TabStop = true };

            if (!"pyxelrest".Equals(service.Name))
            {
                #region OpenAPI Definition
                servicePanel.Controls.Add(new Label { Text = "OpenAPI Definition", TextAlign = ContentAlignment.BottomLeft, Width=120 }, 0, 0);

                ToolTip tooltip = new ToolTip { ToolTipTitle = "URL to the OpenAPI definition of the service", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                openAPIDefinition = new TextBox { Text = service.OpenAPI.ContainsKey("definition") ? service.OpenAPI["definition"].ToString() : string.Empty, Dock = DockStyle.Fill, Width = 290 };
                tooltip.SetToolTip(openAPIDefinition, "It must starts with http://, https:// or file:///.");
                openAPIDefinition.TextChanged += OpenAPIDefinition_TextChanged;
                servicePanel.Controls.Add(openAPIDefinition, 1, 0);

                ToolTip fileTooltip = new ToolTip { ToolTipTitle = "Select an OpenAPI definition", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };
                SelectFileButton selectFile = new SelectFileButton();
                fileTooltip.SetToolTip(selectFile, "It must be a valid OpenAPI definition JSON file.");
                selectFile.Click += SelectFile_Click;
                servicePanel.Controls.Add(selectFile, 2, 0);
                #endregion
            }

            var buttons = new TableLayoutPanel { Width=450, Height=30 };

            #region Advanced Configuration
            var advancedConfigButton = new Button { Text = "Configure", Width = 410 };
            advancedConfigButton.Click += AdvancedConfigButton_Click;
            buttons.Controls.Add(advancedConfigButton, 0, 1);
            buttons.SetColumnSpan(advancedConfigButton, 2);

            advancedConfigurationForm = new AdvancedConfigurationForm(this);
            #endregion

            #region Delete
            {
                ToolTip tooltip = new ToolTip { ToolTipTitle = "Remove this service configuration", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                var deleteButton = new DeleteButton();
                tooltip.SetToolTip(deleteButton, "User defined functions will only be removed when restarting Microsoft Excel.");
                deleteButton.Click += DeleteButton_Click;
                buttons.Controls.Add(deleteButton, 2, 1);
            }
            #endregion

            servicePanel.Controls.Add(buttons);
            servicePanel.SetColumnSpan(buttons, 3);

            return servicePanel;
        }

        private void SelectFile_Click(object sender, EventArgs e)
        {
            OpenFileDialog fileSelection = new OpenFileDialog();
            if (DialogResult.OK == fileSelection.ShowDialog())
                openAPIDefinition.Text = string.Format("file:///{0}", fileSelection.FileName.Replace('\\', '/'));
        }

        private void OpenAPIDefinition_TextChanged(object sender, EventArgs e)
        {
            service.OpenAPI["definition"] = openAPIDefinition.Text;
            configurationForm.ServiceUpdated();
            openAPIDefinitionTicks = DateTime.UtcNow.Ticks;
        }

        private void AdvancedConfigButton_Click(object sender, EventArgs e)
        {
            advancedConfigurationForm.ShowDialog();
        }

        private void DeleteButton_Click(object sender, EventArgs e)
        {
            checkbox.Visible = false;
            configurationForm.configuration.Remove(service);
            configurationForm.Removed(this);
        }
    }
}
