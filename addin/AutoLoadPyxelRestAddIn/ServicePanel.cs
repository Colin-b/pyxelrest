using log4net;
using System;
using System.Drawing;
using System.Net;
using System.Windows.Forms;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class ServicePanel
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private readonly Service service;
        internal readonly TableLayoutPanel servicePanel;
        private TextBox swaggerUrlTextBox;
        private TextBox proxyUrlTextBox;
        private CheckBox get;
        private CheckBox post;
        private CheckBox put;
        private CheckBox delete;
        private CheckBox checkbox;

        private readonly ServiceConfigurationForm configurationForm;
        private long? swaggerUrlModificationTicks;

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
            return swaggerUrlTextBox.TextLength > 0;
        }

        internal void CheckHostReachability()
        {
            if (swaggerUrlModificationTicks != null && DateTime.UtcNow.Ticks >= swaggerUrlModificationTicks + ServiceConfigurationForm.CHECK_HOST_INTERVAL_TICKS)
            {
                swaggerUrlTextBox.BackColor = UrlChecker.IsSwaggerReachable(swaggerUrlTextBox.Text, proxyUrlTextBox.Text) ? Color.LightGreen : Color.Red;
                swaggerUrlModificationTicks = null;
            }
        }

        internal bool Exists(string serviceName)
        {
            return service.Name.Equals(serviceName);
        }

        internal void Display(bool expanded)
        {
            checkbox = configurationForm.accordion.Add(servicePanel, service.Name, open: expanded);
        }

        private TableLayoutPanel DefaultPanel()
        {
            TableLayoutPanel servicePanel = new TableLayoutPanel { Dock = DockStyle.Fill, Padding = new Padding(5) };
            servicePanel.TabStop = true;

            #region Swagger Url
            servicePanel.Controls.Add(new Label { Text = "Swagger URL", TextAlign = ContentAlignment.BottomLeft }, 0, 0);
            swaggerUrlTextBox = new TextBox() { Text = service.SwaggerUrl };
            swaggerUrlTextBox.Dock = DockStyle.Fill;
            swaggerUrlTextBox.AutoSize = true;
            swaggerUrlTextBox.TextChanged += SwaggerUrlTextBox_TextChanged;
            servicePanel.Controls.Add(swaggerUrlTextBox, 1, 0);
            #endregion

            #region Proxy Url
            servicePanel.Controls.Add(new Label { Text = "Proxy URL", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            proxyUrlTextBox = new TextBox() { Text = service.ProxyUrl };
            proxyUrlTextBox.Dock = DockStyle.Fill;
            proxyUrlTextBox.AutoSize = true;
            proxyUrlTextBox.TextChanged += ProxyUrlTextBox_TextChanged; ;
            servicePanel.Controls.Add(proxyUrlTextBox, 1, 1);
            #endregion

            #region Methods
            servicePanel.Controls.Add(new Label { Text = "Methods", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            TableLayoutPanel methodsPanel = new TableLayoutPanel();
            methodsPanel.Dock = DockStyle.Fill;
            methodsPanel.AutoSize = true;
            get = new CheckBox() { Text = "get", Checked = service.Get };
            get.CheckedChanged += Get_CheckedChanged;
            methodsPanel.Controls.Add(get, 0, 0);
            post = new CheckBox() { Text = "post", Checked = service.Post };
            post.CheckedChanged += Post_CheckedChanged;
            methodsPanel.Controls.Add(post, 1, 0);
            put = new CheckBox() { Text = "put", Checked = service.Put };
            put.CheckedChanged += Put_CheckedChanged;
            methodsPanel.Controls.Add(put, 2, 0);
            delete = new CheckBox() { Text = "delete", Checked = service.Delete };
            delete.CheckedChanged += Delete_CheckedChanged;
            methodsPanel.Controls.Add(delete, 3, 0);
            servicePanel.Controls.Add(methodsPanel, 1, 2);
            #endregion

            #region Delete
            Button deleteButton = new Button() { Text = "Delete " + service.Name + " Configuration" };
            deleteButton.Dock = DockStyle.Fill;
            deleteButton.ForeColor = Color.White;
            deleteButton.BackColor = Color.MediumOrchid;
            deleteButton.AutoSize = true;
            deleteButton.Click += DeleteButton_Click;
            servicePanel.Controls.Add(deleteButton);
            servicePanel.SetColumnSpan(deleteButton, 2);
            #endregion

            return servicePanel;
        }

        private void ProxyUrlTextBox_TextChanged(object sender, EventArgs e)
        {
            service.ProxyUrl = proxyUrlTextBox.Text;
            swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
        }

        private void Delete_CheckedChanged(object sender, EventArgs e)
        {
            service.Delete = delete.Checked;
        }

        private void Put_CheckedChanged(object sender, EventArgs e)
        {
            service.Put = put.Checked;
        }

        private void Post_CheckedChanged(object sender, EventArgs e)
        {
            service.Post = post.Checked;
        }

        private void Get_CheckedChanged(object sender, EventArgs e)
        {
            service.Get = get.Checked;
        }

        private void SwaggerUrlTextBox_TextChanged(object sender, EventArgs e)
        {
            service.SwaggerUrl = swaggerUrlTextBox.Text;
            configurationForm.ServiceUpdated();
            swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
        }

        private void DeleteButton_Click(object sender, EventArgs e)
        {
            checkbox.Visible = false;
            configurationForm.configuration.Remove(service);
            configurationForm.Removed(this);
        }
    }
}
