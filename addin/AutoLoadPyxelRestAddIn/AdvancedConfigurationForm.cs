using System;
using System.Drawing;
using System.Windows.Forms;

namespace AutoLoadPyxelRestAddIn
{
    public partial class AdvancedConfigurationForm : Form
    {
        private readonly ServicePanel servicePanel;

        private TextBox httpProxy;
        private TextBox httpsProxy;
        private TextBox noProxy;

        private TableLayoutPanel tagsPanel;
        private TextBox tagName;

        public AdvancedConfigurationForm(ServicePanel servicePanel)
        {
            this.servicePanel = servicePanel;
            InitializeComponent();
        }

        /**
         * Return null if no proxy should be used.
         * Return string.empty if default proxy should be used.
         * Return the proxy to be used otherwise.
         */
        internal string GetProxyFor(string url)
        {
            if (noProxy.Text.Length > 0 && url.StartsWith(noProxy.Text))
                return null;

            if (url.StartsWith("https"))
                return httpsProxy.Text;
            if (url.StartsWith("http"))
                return httpProxy.Text;

            return string.Empty;
        }

        private void InitializeComponent()
        {
            Icon = Properties.Resources.settings_8_16;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Text = string.Format("Configure {0} service", servicePanel.service.Name);
            Size = new Size(600, 400);
            MaximumSize = new Size(800, 600);
            AutoScroll = true;
            StartPosition = FormStartPosition.CenterParent;

            var tabs = new TabControl { Dock = DockStyle.Fill };

            #region Standard settings
            {
                var tab = new TabPage("Standard");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Service Host
                layout.Controls.Add(new Label { Text = "Service Host", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                var serviceHost = new TextBox() { Text = servicePanel.service.ServiceHost, Dock = DockStyle.Fill };
                serviceHost.TextChanged += ServiceHost_TextChanged;
                layout.Controls.Add(serviceHost, 1, 1);
                #endregion

                #region Methods
                {
                    layout.Controls.Add(new Label { Text = "Methods", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                    var panel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };

                    var get = new CheckBox() { Text = "get", Checked = servicePanel.service.Get, Width = 50 };
                    get.CheckedChanged += Get_CheckedChanged;
                    panel.Controls.Add(get, 0, 0);
                    var post = new CheckBox() { Text = "post", Checked = servicePanel.service.Post, Width = 55 };
                    post.CheckedChanged += Post_CheckedChanged;
                    panel.Controls.Add(post, 1, 0);
                    var put = new CheckBox() { Text = "put", Checked = servicePanel.service.Put, Width = 50 };
                    put.CheckedChanged += Put_CheckedChanged;
                    panel.Controls.Add(put, 2, 0);
                    var delete = new CheckBox() { Text = "delete", Checked = servicePanel.service.Delete, Width = 65 };
                    delete.CheckedChanged += Delete_CheckedChanged;
                    panel.Controls.Add(delete, 3, 0);
                    var patch = new CheckBox() { Text = "patch", Checked = servicePanel.service.Patch, Width = 60 };
                    patch.CheckedChanged += Patch_CheckedChanged;
                    panel.Controls.Add(patch, 4, 0);
                    var options = new CheckBox() { Text = "options", Checked = servicePanel.service.Options, Width = 70 };
                    options.CheckedChanged += Options_CheckedChanged;
                    panel.Controls.Add(options, 5, 0);
                    var head = new CheckBox() { Text = "head", Checked = servicePanel.service.Head, Width = 60 };
                    head.CheckedChanged += Head_CheckedChanged;
                    panel.Controls.Add(head, 6, 0);

                    layout.Controls.Add(panel, 1, 2);
                }
                #endregion

                #region Max retries
                layout.Controls.Add(new Label { Text = "Max retries", TextAlign = ContentAlignment.BottomLeft }, 0, 3);

                var maxRetries = new NumericUpDown() { Value = servicePanel.service.MaxRetries, Dock = DockStyle.Fill };
                maxRetries.ValueChanged += MaxRetries_ValueChanged;
                layout.Controls.Add(maxRetries, 1, 3);
                #endregion

                #region Timeout

                #region Connect timeout
                layout.Controls.Add(new Label { Text = "Connect", TextAlign = ContentAlignment.BottomLeft }, 0, 4);

                var connectTimeout = new NumericUpDown() { Value = servicePanel.service.ConnectTimeout, Dock = DockStyle.Fill };
                connectTimeout.ValueChanged += ConnectTimeout_ValueChanged;
                layout.Controls.Add(connectTimeout, 1, 4);
                #endregion

                #region Read timeout
                layout.Controls.Add(new Label { Text = "Read", TextAlign = ContentAlignment.BottomLeft }, 0, 5);

                var readTimeout = new NumericUpDown() { Value = servicePanel.service.ReadTimeout, Dock = DockStyle.Fill };
                readTimeout.ValueChanged += ReadTimeout_ValueChanged;
                layout.Controls.Add(readTimeout, 1, 5);
                #endregion

                #region Swagger read timeout
                layout.Controls.Add(new Label { Text = "Swagger read", TextAlign = ContentAlignment.BottomLeft }, 0, 6);

                var swaggerReadTimeout = new NumericUpDown() { Value = servicePanel.service.SwaggerReadTimeout, Dock = DockStyle.Fill };
                swaggerReadTimeout.ValueChanged += SwaggerReadTimeout_ValueChanged;
                layout.Controls.Add(swaggerReadTimeout, 1, 6);
                #endregion

                #endregion

                #region API Key
                layout.Controls.Add(new Label { Text = "API key", TextAlign = ContentAlignment.BottomLeft }, 0, 7);

                var apiKey = new TextBox() { Text = servicePanel.service.ApiKey, Dock = DockStyle.Fill };
                apiKey.TextChanged += ApiKey_TextChanged;
                layout.Controls.Add(apiKey, 1, 7);
                #endregion

                #region Return behavior
                {
                    layout.Controls.Add(new Label { Text = "Return types", TextAlign = ContentAlignment.BottomLeft }, 0, 8);

                    var panel = new TableLayoutPanel { Dock = DockStyle.Fill };

                    #region UDF Return types
                    var synchronous = new CheckBox() { Text = "synchronous", Checked = servicePanel.service.Synchronous };
                    synchronous.CheckedChanged += Synchronous_CheckedChanged;
                    panel.Controls.Add(synchronous, 0, 0);

                    var asynchronous = new CheckBox() { Text = "asynchronous", Checked = servicePanel.service.Asynchronous };
                    asynchronous.CheckedChanged += Asynchronous_CheckedChanged;
                    panel.Controls.Add(asynchronous, 1, 0);
                    #endregion

                    #region Rely on definitions
                    var relyOnDefinitions = new CheckBox() { Text = "rely on definitions", Checked = servicePanel.service.RelyOnDefinitions, Width = 200 };
                    relyOnDefinitions.CheckedChanged += RelyOnDefinitions_CheckedChanged;
                    panel.Controls.Add(relyOnDefinitions, 2, 0);
                    #endregion

                    layout.Controls.Add(panel, 1, 8);
                }
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Proxies settings
            {
                var tab = new TabPage("Proxies");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region HTTP proxy
                layout.Controls.Add(new Label { Text = "HTTP URL", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                httpProxy = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Proxies.ContainsKey("http") ? (string)servicePanel.service.Proxies["http"] : string.Empty };
                httpProxy.TextChanged += HttpProxy_TextChanged;
                layout.Controls.Add(httpProxy, 1, 1);
                #endregion

                #region HTTPS proxy
                layout.Controls.Add(new Label { Text = "HTTPS URL", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                httpsProxy = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Proxies.ContainsKey("https") ? (string)servicePanel.service.Proxies["https"] : string.Empty };
                httpsProxy.TextChanged += HttpsProxy_TextChanged;
                layout.Controls.Add(httpsProxy, 1, 2);
                #endregion

                #region No proxy
                layout.Controls.Add(new Label { Text = "No proxy URL", TextAlign = ContentAlignment.BottomLeft }, 0, 3);

                noProxy = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Proxies.ContainsKey("no_proxy") ? (string)servicePanel.service.Proxies["no_proxy"] : string.Empty };
                noProxy.TextChanged += NoProxy_TextChanged;
                layout.Controls.Add(noProxy, 1, 3);
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Headers settings
            {
                var tab = new TabPage("Headers");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Add items

                var headerName = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                layout.Controls.Add(headerName, 0, 1);
                layout.SetColumnSpan(headerName, 2);

                var addHeader = new Button { Text = "Add field", Dock = DockStyle.Fill, AutoSize = true };
                layout.Controls.Add(addHeader, 0, 2);
                layout.SetColumnSpan(addHeader, 2);

                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Tags settings
            {
                var tab = new TabPage("Tags");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Add values

                tagsPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                layout.Controls.Add(tagsPanel);
                layout.SetColumnSpan(tagsPanel, 2);

                tagName = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                layout.Controls.Add(tagName);
                layout.SetColumnSpan(tagName, 2);

                var addTag = new Button { Text = "Add tag", Dock = DockStyle.Fill, AutoSize = true };
                addTag.Click += AddTag_Click;
                layout.Controls.Add(addTag);
                layout.SetColumnSpan(addTag, 2);

                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region OAuth2 settings
            {
                var tab = new TabPage("OAuth2");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Port
                layout.Controls.Add(new Label { Width = 150, Text = "Port", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                var port = new NumericUpDown { Width = 400, Maximum = 100000, Dock = DockStyle.Fill, Value = servicePanel.service.OAuth2.ContainsKey("port") ? (decimal)servicePanel.service.OAuth2["port"] : 5000 };
                port.TextChanged += Oauth2Port_TextChanged;
                layout.Controls.Add(port, 1, 1);
                #endregion

                #region Timeout
                layout.Controls.Add(new Label { Width = 150, Text = "Timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                var timeout = new NumericUpDown { Maximum = 1000, Dock = DockStyle.Fill, Value = servicePanel.service.OAuth2.ContainsKey("timeout") ? (decimal)servicePanel.service.OAuth2["timeout"] : 60 };
                timeout.TextChanged += Oauth2Timeout_TextChanged;
                layout.Controls.Add(timeout, 1, 2);
                #endregion

                #region Success display time
                layout.Controls.Add(new Label { Width = 150, Text = "Success display time", TextAlign = ContentAlignment.BottomLeft }, 0, 3);

                var successDisplayTime = new NumericUpDown { Maximum = 100000, Dock = DockStyle.Fill, Value = servicePanel.service.OAuth2.ContainsKey("success_display_time") ? (decimal)servicePanel.service.OAuth2["success_display_time"] : 1 };
                successDisplayTime.TextChanged += Oauth2SuccessDisplayTime_TextChanged;
                layout.Controls.Add(successDisplayTime, 1, 3);
                #endregion

                #region Failure display time
                layout.Controls.Add(new Label { Width = 150, Text = "Failure display time", TextAlign = ContentAlignment.BottomLeft }, 0, 4);

                var failureDisplayTime = new NumericUpDown { Maximum = 100000, Dock = DockStyle.Fill, Value = servicePanel.service.OAuth2.ContainsKey("failure_display_time") ? (decimal)servicePanel.service.OAuth2["failure_display_time"] : 5000 };
                failureDisplayTime.TextChanged += Oauth2FailureDisplayTime_TextChanged;
                layout.Controls.Add(failureDisplayTime, 1, 4);
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Basic Authentication settings
            {
                var tab = new TabPage("Basic");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Username
                layout.Controls.Add(new Label { Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                var userName = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Basic.ContainsKey("username") ? (string)servicePanel.service.Basic["username"] : string.Empty };
                userName.TextChanged += BasicUsername_TextChanged;
                layout.Controls.Add(userName, 1, 1);
                #endregion

                #region Password
                layout.Controls.Add(new Label { Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                var password = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Basic.ContainsKey("password") ? (string)servicePanel.service.Basic["password"] : string.Empty };
                password.TextChanged += BasicPassword_TextChanged;
                layout.Controls.Add(password, 1, 2);
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region NTLM Authentication settings
            {
                var tab = new TabPage("NTLM");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Username
                layout.Controls.Add(new Label { Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                var userName = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Basic.ContainsKey("username") ? (string)servicePanel.service.Basic["username"] : string.Empty };
                userName.TextChanged += NtlmUsername_TextChanged;
                layout.Controls.Add(userName, 1, 1);
                #endregion

                #region Password
                layout.Controls.Add(new Label { Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                var password = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Basic.ContainsKey("password") ? (string)servicePanel.service.Basic["password"] : string.Empty };
                password.TextChanged += NtlmPassword_TextChanged;
                layout.Controls.Add(password, 1, 2);
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            Controls.Add(tabs);
        }

        #region Events

        private void NtlmPassword_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Ntlm.Remove("password");
            else
                servicePanel.service.Ntlm["password"] = ((TextBox)sender).Text;
        }

        private void NtlmUsername_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Ntlm.Remove("username");
            else
                servicePanel.service.Ntlm["username"] = ((TextBox)sender).Text;
        }

        private void BasicPassword_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Basic.Remove("password");
            else
                servicePanel.service.Basic["password"] = ((TextBox)sender).Text;
        }

        private void BasicUsername_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Basic.Remove("username");
            else
                servicePanel.service.Basic["username"] = ((TextBox)sender).Text;
        }

        private void Oauth2FailureDisplayTime_TextChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Value == 0)
                servicePanel.service.OAuth2.Remove("failure_display_time");
            else
                servicePanel.service.OAuth2["failure_display_time"] = ((NumericUpDown)sender).Value;
        }

        private void Oauth2SuccessDisplayTime_TextChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Value == 0)
                servicePanel.service.OAuth2.Remove("success_display_time");
            else
                servicePanel.service.OAuth2["success_display_time"] = ((NumericUpDown)sender).Value;
        }

        private void Oauth2Port_TextChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Value == 0)
                servicePanel.service.OAuth2.Remove("port");
            else
                servicePanel.service.OAuth2["port"] = ((NumericUpDown)sender).Value;
        }

        private void Oauth2Timeout_TextChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Value == 0)
                servicePanel.service.OAuth2.Remove("timeout");
            else
                servicePanel.service.OAuth2["timeout"] = ((NumericUpDown)sender).Value;
        }

        private void NoProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Proxies.Remove("no_proxy");
            else
                servicePanel.service.Proxies["no_proxy"] = ((TextBox)sender).Text;
        }

        private void HttpsProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Proxies.Remove("https");
            else
                servicePanel.service.Proxies["https"] = ((TextBox)sender).Text;
        }

        private void HttpProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Proxies.Remove("http");
            else
                servicePanel.service.Proxies["http"] = ((TextBox)sender).Text;
        }

        private void SwaggerReadTimeout_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.SwaggerReadTimeout = ((NumericUpDown)sender).Value;
        }

        private void ReadTimeout_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.ReadTimeout = ((NumericUpDown)sender).Value;
        }

        private void ConnectTimeout_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.ConnectTimeout = ((NumericUpDown)sender).Value;
        }

        private void MaxRetries_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.MaxRetries = (int)((NumericUpDown)sender).Value;
        }

        private void RelyOnDefinitions_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.RelyOnDefinitions = ((CheckBox)sender).Checked;
        }

        private void ServiceHost_TextChanged(object sender, EventArgs e)
        {
            servicePanel.service.ServiceHost = ((TextBox)sender).Text;
        }

        private void Head_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Head = ((CheckBox)sender).Checked;
        }

        private void Options_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Options = ((CheckBox)sender).Checked;
        }

        private void Patch_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Patch = ((CheckBox)sender).Checked;
        }

        private void Delete_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Delete = ((CheckBox)sender).Checked;
        }

        private void Put_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Put = ((CheckBox)sender).Checked;
        }

        private void Post_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Post = ((CheckBox)sender).Checked;
        }

        private void Get_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Get = ((CheckBox)sender).Checked;
        }

        private void ApiKey_TextChanged(object sender, EventArgs e)
        {
            servicePanel.service.ApiKey = ((TextBox)sender).Text;
        }

        private void Asynchronous_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Asynchronous = ((CheckBox)sender).Checked;
        }

        private void Synchronous_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Synchronous = ((CheckBox)sender).Checked;
        }

        private void AddTag_Click(object sender, EventArgs e)
        {
            servicePanel.service.Tags.Add(tagName.Text);

            var panel = new TableLayoutPanel { Dock = DockStyle.Fill };

            panel.Controls.Add(new Label { Name="tagLabel", Text = tagName.Text, Dock = DockStyle.Fill }, 0, 1);

            var remove = new Button { Text = "Remove tag", Dock = DockStyle.Fill };
            remove.Click += RemoveTag_Click;
            panel.Controls.Add(remove, 1, 1);

            tagsPanel.Controls.Add(panel);
            tagsPanel.SetColumnSpan(panel, 2);

            tagName.Text = "";
        }

        private void RemoveTag_Click(object sender, EventArgs e)
        {
            var panel = ((Button)sender).Parent;
            Label tagLabel = (Label) panel.Controls.Find("tagLabel", false)[0];

            servicePanel.service.Tags.Add(tagLabel.Text);

            tagsPanel.Controls.Remove(panel);
        }

        #endregion
    }
}
