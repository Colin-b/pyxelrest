using log4net;
using System;
using System.Drawing;
using System.Globalization;
using System.Text.RegularExpressions;
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
        private TextBox serviceHostTextBox;
        private CheckBox get;
        private CheckBox post;
        private CheckBox put;
        private CheckBox delete;
        private CheckBox patch;
        private CheckBox options;
        private CheckBox head;
        private CheckBox checkbox;
        private TextBox tagsTextBox;
        private TextBox connectTimeoutTextBox;
        private TextBox readTimeoutTextBox;
        private TextBox securityDetailsTextBox;
        private TextBox advancedConfigurationTextBox;

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
            proxyUrlTextBox.TextChanged += ProxyUrlTextBox_TextChanged;
            servicePanel.Controls.Add(proxyUrlTextBox, 1, 1);
            #endregion

            #region Service Host
            servicePanel.Controls.Add(new Label { Text = "Service Host", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            serviceHostTextBox = new TextBox() { Text = service.ServiceHost };
            serviceHostTextBox.Dock = DockStyle.Fill;
            serviceHostTextBox.AutoSize = true;
            serviceHostTextBox.TextChanged += ServiceHostTextBox_TextChanged;
            servicePanel.Controls.Add(serviceHostTextBox, 1, 2);
            #endregion

            #region Security Details
            servicePanel.Controls.Add(new Label { Text = "Security Details", TextAlign = ContentAlignment.BottomLeft }, 0, 3);
            securityDetailsTextBox = new TextBox() { Text = service.SecurityDetails };
            securityDetailsTextBox.Dock = DockStyle.Fill;
            securityDetailsTextBox.AutoSize = true;
            securityDetailsTextBox.TextChanged += SecurityDetailsTextBox_TextChanged;
            servicePanel.Controls.Add(securityDetailsTextBox, 1, 3);
            #endregion

            #region Advanced Configuration
            servicePanel.Controls.Add(new Label { Text = "Advanced Config", TextAlign = ContentAlignment.BottomLeft }, 0, 4);
            advancedConfigurationTextBox = new TextBox() { Text = service.AdvancedConfiguration };
            advancedConfigurationTextBox.Dock = DockStyle.Fill;
            advancedConfigurationTextBox.AutoSize = true;
            advancedConfigurationTextBox.TextChanged += AdvancedConfigurationTextBox_TextChanged;
            servicePanel.Controls.Add(advancedConfigurationTextBox, 1, 4);
            #endregion

            #region Tags
            servicePanel.Controls.Add(new Label { Text = "Tags", TextAlign = ContentAlignment.BottomLeft }, 0, 5);
            tagsTextBox = new TextBox() { Text = service.Tags };
            tagsTextBox.Dock = DockStyle.Fill;
            tagsTextBox.AutoSize = true;
            tagsTextBox.TextChanged += TagsTextBox_TextChanged;
            servicePanel.Controls.Add(tagsTextBox, 1, 5);
            #endregion

            #region Methods
            servicePanel.Controls.Add(new Label { Text = "Methods", TextAlign = ContentAlignment.BottomLeft }, 0, 6);
            TableLayoutPanel methodsPanel = new TableLayoutPanel();
            methodsPanel.Dock = DockStyle.Fill;
            methodsPanel.AutoSize = true;
            get = new CheckBox() { Text = "get", Checked = service.Get, Width = 50 };
            get.CheckedChanged += Get_CheckedChanged;
            methodsPanel.Controls.Add(get, 0, 0);
            post = new CheckBox() { Text = "post", Checked = service.Post, Width = 50 };
            post.CheckedChanged += Post_CheckedChanged;
            methodsPanel.Controls.Add(post, 1, 0);
            put = new CheckBox() { Text = "put", Checked = service.Put, Width = 50 };
            put.CheckedChanged += Put_CheckedChanged;
            methodsPanel.Controls.Add(put, 2, 0);
            delete = new CheckBox() { Text = "delete", Checked = service.Delete, Width = 60 };
            delete.CheckedChanged += Delete_CheckedChanged;
            methodsPanel.Controls.Add(delete, 3, 0);
            patch = new CheckBox() { Text = "patch", Checked = service.Patch, Width = 60 };
            patch.CheckedChanged += Patch_CheckedChanged;
            methodsPanel.Controls.Add(patch, 4, 0);
            options = new CheckBox() { Text = "options", Checked = service.Options, Width = 60 };
            options.CheckedChanged += Options_CheckedChanged;
            methodsPanel.Controls.Add(options, 5, 0);
            head = new CheckBox() { Text = "head", Checked = service.Head, Width = 50 };
            head.CheckedChanged += Head_CheckedChanged;
            methodsPanel.Controls.Add(head, 6, 0);
            servicePanel.Controls.Add(methodsPanel, 1, 6);
            #endregion

            #region Timeouts
            servicePanel.Controls.Add(new Label { Text = "Timeouts", TextAlign = ContentAlignment.BottomLeft }, 0, 7);
            TableLayoutPanel timeoutsPanel = new TableLayoutPanel();
            timeoutsPanel.Dock = DockStyle.Fill;
            timeoutsPanel.AutoSize = true;
            timeoutsPanel.Controls.Add(new Label { Text = "Connection", TextAlign = ContentAlignment.BottomLeft }, 0, 0);
            connectTimeoutTextBox = new TextBox() { Text = service.ConnectTimeout.HasValue? service.ConnectTimeout.Value.ToString(CultureInfo.InvariantCulture) : string.Empty };
            connectTimeoutTextBox.TextChanged += ConnectTimeoutTextBox_TextChanged;
            timeoutsPanel.Controls.Add(connectTimeoutTextBox, 1, 0);
            timeoutsPanel.Controls.Add(new Label { Text = "Read", TextAlign = ContentAlignment.BottomLeft }, 2, 0);
            readTimeoutTextBox = new TextBox() { Text = service.ReadTimeout.HasValue ? service.ReadTimeout.Value.ToString(CultureInfo.InvariantCulture) : string.Empty };
            readTimeoutTextBox.TextChanged += ReadTimeoutTextBox_TextChanged;
            timeoutsPanel.Controls.Add(readTimeoutTextBox, 3, 0);
            servicePanel.Controls.Add(timeoutsPanel, 1, 7);
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

        private void SecurityDetailsTextBox_TextChanged(object sender, EventArgs e)
        {
            var securityDetailsRegex = new Regex("^(([^\n,]+)=([^\n,]*))(,([^\n,]+)=([^\n,]*))*$");
            if(securityDetailsRegex.IsMatch(securityDetailsTextBox.Text)) {
                securityDetailsTextBox.BackColor = Color.LightGreen;
                service.SecurityDetails = securityDetailsTextBox.Text;
            }
            else
            {
                securityDetailsTextBox.BackColor = string.IsNullOrEmpty(securityDetailsTextBox.Text) ? Color.Empty : Color.Red;
                service.SecurityDetails = string.Empty;
            }
        }

        private void AdvancedConfigurationTextBox_TextChanged(object sender, EventArgs e)
        {
            var advancedConfigurationRegex = new Regex("^(([^\n,]+)=([^\n,]*))(,([^\n,]+)=([^\n,]*))*$");
            if (advancedConfigurationRegex.IsMatch(advancedConfigurationTextBox.Text))
            {
                advancedConfigurationTextBox.BackColor = Color.LightGreen;
                service.AdvancedConfiguration = advancedConfigurationTextBox.Text;
            }
            else
            {
                advancedConfigurationTextBox.BackColor = string.IsNullOrEmpty(advancedConfigurationTextBox.Text) ? Color.Empty : Color.Red;
                service.AdvancedConfiguration = string.Empty;
            }
        }

        private void ReadTimeoutTextBox_TextChanged(object sender, EventArgs e)
        {
            float parsed;
            if (float.TryParse(readTimeoutTextBox.Text, NumberStyles.AllowDecimalPoint, CultureInfo.InvariantCulture, out parsed))
                service.ReadTimeout = parsed;
            else
                service.ReadTimeout = null;
        }

        private void ConnectTimeoutTextBox_TextChanged(object sender, EventArgs e)
        {
            float parsed;
            if (float.TryParse(connectTimeoutTextBox.Text, NumberStyles.AllowDecimalPoint, CultureInfo.InvariantCulture, out parsed))
                service.ConnectTimeout = parsed;
            else
                service.ConnectTimeout = null;
        }

        private void TagsTextBox_TextChanged(object sender, EventArgs e)
        {
            service.Tags = tagsTextBox.Text;
        }

        private void ServiceHostTextBox_TextChanged(object sender, EventArgs e)
        {
            service.ServiceHost = serviceHostTextBox.Text;
        }

        private void ProxyUrlTextBox_TextChanged(object sender, EventArgs e)
        {
            service.ProxyUrl = proxyUrlTextBox.Text;
            swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
        }

        private void Head_CheckedChanged(object sender, EventArgs e)
        {
            service.Head = head.Checked;
        }

        private void Options_CheckedChanged(object sender, EventArgs e)
        {
            service.Options = options.Checked;
        }

        private void Patch_CheckedChanged(object sender, EventArgs e)
        {
            service.Patch = patch.Checked;
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
