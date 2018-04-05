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

        private TextBox openAPISpecification;
        private AdvancedConfigurationForm advancedConfigurationForm;

        #endregion

        internal readonly Service service;

        internal long? openAPISpecificationTicks;

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
            return service.Name.Equals("pyxelrest") || openAPISpecification.TextLength > 0;
        }

        internal void CheckHostReachability()
        {
            if (openAPISpecificationTicks != null && DateTime.UtcNow.Ticks >= openAPISpecificationTicks + ServiceConfigurationForm.CHECK_HOST_INTERVAL_TICKS)
            {
                openAPISpecification.BackColor = UrlChecker.CanReachOpenAPISpecification(openAPISpecification.Text, advancedConfigurationForm.GetProxyFor(openAPISpecification.Text)) ? Color.LightGreen : Color.Red;
                openAPISpecificationTicks = null;
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
            var servicePanel = new TableLayoutPanel { TabStop = true };

            if (!"pyxelrest".Equals(service.Name))
            {
                #region OpenAPI Specification Url
                servicePanel.Controls.Add(new Label { Text = "OpenAPI Specification", TextAlign = ContentAlignment.BottomLeft, Width=120 }, 0, 0);

                openAPISpecification = new TextBox { Text = service.OpenAPISpecification, Dock = DockStyle.Fill, Width = 300 };
                openAPISpecification.TextChanged += OpenAPISpecification_TextChanged;
                servicePanel.Controls.Add(openAPISpecification, 1, 0);
                #endregion
            }

            var buttons = new TableLayoutPanel { Width=450, Height=30 };

            #region Advanced Configuration
            var advancedConfigButton = new Button { Text = "Configure", Width = 410 };
            advancedConfigButton.Click += AdvancedConfigButton_Click;
            buttons.Controls.Add(advancedConfigButton, 0, 1);

            advancedConfigurationForm = new AdvancedConfigurationForm(this);
            #endregion

            #region Delete
            var deleteButton = new PictureBox {Image = Properties.Resources.x_mark_3_16, Padding=new Padding(0, 4, 0, 0), Width=20 };
            deleteButton.MouseEnter += DeleteButton_MouseEnter;
            deleteButton.MouseLeave += DeleteButton_MouseLeave;
            deleteButton.Click += DeleteButton_Click;
            buttons.Controls.Add(deleteButton, 1, 1);
            #endregion

            servicePanel.Controls.Add(buttons);
            servicePanel.SetColumnSpan(buttons, 2);

            return servicePanel;
        }

        private void DeleteButton_MouseEnter(object sender, EventArgs e)
        {
            ((PictureBox)sender).Image = Properties.Resources.x_mark_4_16;
        }

        private void DeleteButton_MouseLeave(object sender, EventArgs e)
        {
            ((PictureBox)sender).Image = Properties.Resources.x_mark_3_16;
        }

        private void OpenAPISpecification_TextChanged(object sender, EventArgs e)
        {
            service.OpenAPISpecification = openAPISpecification.Text;
            configurationForm.ServiceUpdated();
            openAPISpecificationTicks = DateTime.UtcNow.Ticks;
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
