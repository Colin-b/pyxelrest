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

        private TextBox swaggerUrlTextBox;
        private AdvancedConfigurationForm advancedConfigurationForm;

        #endregion

        internal readonly Service service;

        internal long? swaggerUrlModificationTicks;

        public ServicePanel(ServiceConfigurationForm configurationForm, Service service)
        {
            this.configurationForm = configurationForm;
            this.service = service;
            servicePanel = service.Name.Equals("pyxelrest") ? PyxelRestDefaultPanel() : DefaultPanel();
        }

        public override string ToString()
        {
            return service.ToString();
        }

        internal bool IsValid()
        {
            return service.Name.Equals("pyxelrest") || swaggerUrlTextBox.TextLength > 0;
        }

        internal void CheckHostReachability()
        {
            if (swaggerUrlModificationTicks != null && DateTime.UtcNow.Ticks >= swaggerUrlModificationTicks + ServiceConfigurationForm.CHECK_HOST_INTERVAL_TICKS)
            {
                swaggerUrlTextBox.BackColor = UrlChecker.IsSwaggerReachable(swaggerUrlTextBox.Text, advancedConfigurationForm.GetProxyFor(swaggerUrlTextBox.Text)) ? Color.LightGreen : Color.Red;
                swaggerUrlModificationTicks = null;
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
            checkbox = configurationForm.accordion.Add(servicePanel, service.Name, open: expanded);
        }

        private TableLayoutPanel DefaultPanel()
        {
            var servicePanel = new TableLayoutPanel { Dock = DockStyle.Fill, Padding = new Padding(5), TabStop = true };

            #region Swagger Url
            servicePanel.Controls.Add(new Label { Text = "Swagger URL", TextAlign = ContentAlignment.BottomLeft }, 0, 0);

            swaggerUrlTextBox = new TextBox { Text = service.SwaggerUrl, Dock = DockStyle.Fill, Width=300 };
            swaggerUrlTextBox.TextChanged += SwaggerUrlTextBox_TextChanged;
            servicePanel.Controls.Add(swaggerUrlTextBox, 1, 0);
            #endregion

            #region Advanced Configuration
            var advancedConfigButton = new Button { Text = "Configure", Dock = DockStyle.Fill };
            advancedConfigButton.Click += AdvancedConfigButton_Click;
            servicePanel.Controls.Add(advancedConfigButton);
            servicePanel.SetColumnSpan(advancedConfigButton, 2);

            advancedConfigurationForm = new AdvancedConfigurationForm(this);
            #endregion

            #region Delete
            var deleteButton = new Button { ForeColor = Color.White, BackColor = Color.MediumOrchid, Dock = DockStyle.Fill, Text = "Delete " + service.Name + " Configuration" };
            deleteButton.Click += DeleteButton_Click;
            servicePanel.Controls.Add(deleteButton);
            servicePanel.SetColumnSpan(deleteButton, 2);
            #endregion

            return servicePanel;
        }

        private TableLayoutPanel PyxelRestDefaultPanel()
        {
            var servicePanel = new TableLayoutPanel { Dock = DockStyle.Fill, Padding = new Padding(5), TabStop = true };

            #region Advanced Configuration
            var advancedConfigButton = new Button { Text = "Configure", Dock = DockStyle.Fill };
            advancedConfigButton.Click += AdvancedConfigButton_Click;
            servicePanel.Controls.Add(advancedConfigButton);

            advancedConfigurationForm = new AdvancedConfigurationForm(this);
            #endregion

            #region Delete
            var deleteButton = new Button { ForeColor = Color.White, BackColor = Color.MediumOrchid, Dock = DockStyle.Fill, Text = "Delete " + service.Name + " Configuration" };
            deleteButton.Click += DeleteButton_Click;
            servicePanel.Controls.Add(deleteButton);
            #endregion

            return servicePanel;
        }

        private void SwaggerUrlTextBox_TextChanged(object sender, EventArgs e)
        {
            service.SwaggerUrl = swaggerUrlTextBox.Text;
            configurationForm.ServiceUpdated();
            swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
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
