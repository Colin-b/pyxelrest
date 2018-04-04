using System;
using System.Drawing;
using System.Windows.Forms;

namespace AutoLoadPyxelRestAddIn
{
    public partial class AdvancedConfigurationForm : Form
    {
        private readonly ServicePanel servicePanel;

        #region Fields

        #region Proxies tab fields
        private TextBox httpProxyTextBox;
        private TextBox httpsProxyTextBox;
        private TextBox noProxyTextBox;
        #endregion

        private TextBox serviceHostTextBox;

        private CheckBox get;
        private CheckBox post;
        private CheckBox put;
        private CheckBox delete;
        private CheckBox patch;
        private CheckBox options;
        private CheckBox head;

        #region OAuth2 tab fields
        private NumericUpDown oauth2PortTextBox;
        private NumericUpDown oauth2TimeoutTextBox;
        private NumericUpDown oauth2SuccessDisplayTimeTextBox;
        private NumericUpDown oauth2FailureDisplayTimeTextBox;
        #endregion

        private TextBox apiKeyTextBox;

        #region Basic tab fields
        private TextBox basicUsernameTextBox;
        private TextBox basicPasswordTextBox;
        #endregion

        #region NTLM tab fields
        private TextBox ntlmUsernameTextBox;
        private TextBox ntlmPasswordTextBox;
        #endregion

        private CheckBox synchronous;
        private CheckBox asynchronous;

        private CheckBox relyOnDefinitions;
        private NumericUpDown MaxRetriesTextBox;
        private NumericUpDown ConnectTimeoutTextBox;
        private NumericUpDown ReadTimeoutTextBox;
        private NumericUpDown SwaggerReadTimeoutTextBox;
        private TextBox tagsTextBox;

        #endregion

        public AdvancedConfigurationForm(ServicePanel servicePanel)
        {
            this.servicePanel = servicePanel;
            InitializeComponent();
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

            TabControl tabs = new TabControl();
            tabs.Dock = DockStyle.Fill;

            #region Standard settings
            TabPage standardTab = new TabPage("Standard");
            TableLayoutPanel layout = new TableLayoutPanel();
            layout.AutoSize = true;

            #region Service Host
            layout.Controls.Add(new Label { Text = "Service Host", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            serviceHostTextBox = new TextBox() { Text = servicePanel.service.ServiceHost };
            serviceHostTextBox.Dock = DockStyle.Fill;
            serviceHostTextBox.TextChanged += ServiceHostTextBox_TextChanged;
            layout.Controls.Add(serviceHostTextBox, 1, 1);
            #endregion

            #region Methods
            layout.Controls.Add(new Label { Text = "Methods", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            TableLayoutPanel methodsPanel = new TableLayoutPanel();
            methodsPanel.Dock = DockStyle.Fill;
            methodsPanel.AutoSize = true;
            get = new CheckBox() { Text = "get", Checked = servicePanel.service.Get, Width = 50 };
            get.CheckedChanged += Get_CheckedChanged;
            methodsPanel.Controls.Add(get, 0, 0);
            post = new CheckBox() { Text = "post", Checked = servicePanel.service.Post, Width = 55 };
            post.CheckedChanged += Post_CheckedChanged;
            methodsPanel.Controls.Add(post, 1, 0);
            put = new CheckBox() { Text = "put", Checked = servicePanel.service.Put, Width = 50 };
            put.CheckedChanged += Put_CheckedChanged;
            methodsPanel.Controls.Add(put, 2, 0);
            delete = new CheckBox() { Text = "delete", Checked = servicePanel.service.Delete, Width = 65 };
            delete.CheckedChanged += Delete_CheckedChanged;
            methodsPanel.Controls.Add(delete, 3, 0);
            patch = new CheckBox() { Text = "patch", Checked = servicePanel.service.Patch, Width = 60 };
            patch.CheckedChanged += Patch_CheckedChanged;
            methodsPanel.Controls.Add(patch, 4, 0);
            options = new CheckBox() { Text = "options", Checked = servicePanel.service.Options, Width = 70 };
            options.CheckedChanged += Options_CheckedChanged;
            methodsPanel.Controls.Add(options, 5, 0);
            head = new CheckBox() { Text = "head", Checked = servicePanel.service.Head, Width = 60 };
            head.CheckedChanged += Head_CheckedChanged;
            methodsPanel.Controls.Add(head, 6, 0);
            layout.Controls.Add(methodsPanel, 1, 2);
            #endregion

            #region Max retries
            layout.Controls.Add(new Label { Text = "Max retries", TextAlign = ContentAlignment.BottomLeft }, 0, 3);
            MaxRetriesTextBox = new NumericUpDown() { Value = servicePanel.service.MaxRetries };
            MaxRetriesTextBox.Dock = DockStyle.Fill;
            MaxRetriesTextBox.ValueChanged += MaxRetriesTextBox_ValueChanged;
            layout.Controls.Add(MaxRetriesTextBox, 1, 3);
            #endregion

            #region Timeout

            #region Connect timeout
            layout.Controls.Add(new Label { Text = "Connect", TextAlign = ContentAlignment.BottomLeft }, 0, 4);
            ConnectTimeoutTextBox = new NumericUpDown() { Value = servicePanel.service.ConnectTimeout };
            ConnectTimeoutTextBox.Dock = DockStyle.Fill;
            ConnectTimeoutTextBox.ValueChanged += ConnectTimeoutTextBox_ValueChanged;
            layout.Controls.Add(ConnectTimeoutTextBox, 1, 4);
            #endregion

            #region Read timeout
            layout.Controls.Add(new Label { Text = "Read", TextAlign = ContentAlignment.BottomLeft }, 0, 5);
            ReadTimeoutTextBox = new NumericUpDown() { Value = servicePanel.service.ReadTimeout };
            ReadTimeoutTextBox.Dock = DockStyle.Fill;
            ReadTimeoutTextBox.ValueChanged += ReadTimeoutTextBox_ValueChanged;
            layout.Controls.Add(ReadTimeoutTextBox, 1, 5);
            #endregion

            #region Swagger read timeout
            layout.Controls.Add(new Label { Text = "Swagger read", TextAlign = ContentAlignment.BottomLeft }, 0, 6);
            SwaggerReadTimeoutTextBox = new NumericUpDown() { Value = servicePanel.service.SwaggerReadTimeout };
            SwaggerReadTimeoutTextBox.Dock = DockStyle.Fill;
            SwaggerReadTimeoutTextBox.ValueChanged += SwaggerReadTimeoutTextBox_ValueChanged;
            layout.Controls.Add(SwaggerReadTimeoutTextBox, 1, 6);
            #endregion

            #endregion

            #region API Key
            layout.Controls.Add(new Label { Text = "API key", TextAlign = ContentAlignment.BottomLeft }, 0, 7);
            apiKeyTextBox = new TextBox() { Text = servicePanel.service.ApiKey };
            apiKeyTextBox.Dock = DockStyle.Fill;
            apiKeyTextBox.TextChanged += ApiKeyTextBox_TextChanged;
            layout.Controls.Add(apiKeyTextBox, 1, 7);
            #endregion

            #region Return behavior

            layout.Controls.Add(new Label { Text = "Return types", TextAlign = ContentAlignment.BottomLeft }, 0, 8);

            TableLayoutPanel returnBehaviorPanel = new TableLayoutPanel();
            returnBehaviorPanel.Dock = DockStyle.Fill;

            #region UDF Return types
            synchronous = new CheckBox() { Text = "synchronous", Checked = servicePanel.service.Synchronous };
            synchronous.CheckedChanged += Synchronous_CheckedChanged;
            returnBehaviorPanel.Controls.Add(synchronous, 0, 0);
            asynchronous = new CheckBox() { Text = "asynchronous", Checked = servicePanel.service.Asynchronous };
            asynchronous.CheckedChanged += Asynchronous_CheckedChanged;
            returnBehaviorPanel.Controls.Add(asynchronous, 1, 0);
            #endregion

            #region Rely on definitions
            relyOnDefinitions = new CheckBox() { Text = "rely on definitions", Checked = servicePanel.service.RelyOnDefinitions, Width=200 };
            relyOnDefinitions.CheckedChanged += RelyOnDefinitions_CheckedChanged;
            returnBehaviorPanel.Controls.Add(relyOnDefinitions, 2, 0);
            #endregion

            layout.Controls.Add(returnBehaviorPanel, 1, 8);

            #endregion

            standardTab.Controls.Add(layout);

            tabs.TabPages.Add(standardTab);
            #endregion

            #region Proxies settings
            TabPage proxiesTab = new TabPage("Proxies");
            TableLayoutPanel proxiesLayout = new TableLayoutPanel();
            proxiesLayout.AutoSize = true;

            #region HTTP proxy
            proxiesLayout.Controls.Add(new Label { Text = "HTTP URL", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            httpProxyTextBox = new TextBox() { Width=450, Text = servicePanel.service.Proxies.ContainsKey("http") ? (string)servicePanel.service.Proxies["http"] : string.Empty };
            httpProxyTextBox.Dock = DockStyle.Fill;
            httpProxyTextBox.TextChanged += HttpProxyTextBox_TextChanged;
            proxiesLayout.Controls.Add(httpProxyTextBox, 1, 1);
            #endregion

            #region HTTPS proxy
            proxiesLayout.Controls.Add(new Label { Text = "HTTPS URL", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            httpsProxyTextBox = new TextBox() { Width = 450, Text = servicePanel.service.Proxies.ContainsKey("https") ? (string)servicePanel.service.Proxies["https"] : string.Empty };
            httpsProxyTextBox.Dock = DockStyle.Fill;
            httpsProxyTextBox.TextChanged += HttpsProxyTextBox_TextChanged;
            proxiesLayout.Controls.Add(httpsProxyTextBox, 1, 2);
            #endregion

            #region No proxy
            proxiesLayout.Controls.Add(new Label { Text = "No proxy URL", TextAlign = ContentAlignment.BottomLeft }, 0, 3);
            noProxyTextBox = new TextBox() { Width = 450, Text = servicePanel.service.Proxies.ContainsKey("no_proxy") ? (string)servicePanel.service.Proxies["no_proxy"] : string.Empty };
            noProxyTextBox.Dock = DockStyle.Fill;
            noProxyTextBox.TextChanged += NoProxyTextBox_TextChanged;
            proxiesLayout.Controls.Add(noProxyTextBox, 1, 3);
            #endregion

            proxiesTab.Controls.Add(proxiesLayout);

            tabs.TabPages.Add(proxiesTab);
            #endregion

            #region Headers settings
            TabPage headersTab = new TabPage("Headers");
            TableLayoutPanel headersLayout = new TableLayoutPanel();
            headersLayout.AutoSize = true;

            #region Add items

            TextBox newHeaderFieldNameTextBox = new TextBox() { Text = string.Empty };
            newHeaderFieldNameTextBox.Dock = DockStyle.Fill;
            headersLayout.Controls.Add(newHeaderFieldNameTextBox, 0, 1);
            headersLayout.SetColumnSpan(newHeaderFieldNameTextBox, 2);

            Button addHeaderFieldButton = new Button() { Text = "Add field" };
            addHeaderFieldButton.Dock = DockStyle.Fill;
            addHeaderFieldButton.AutoSize = true;
            headersLayout.Controls.Add(addHeaderFieldButton, 0, 2);
            headersLayout.SetColumnSpan(addHeaderFieldButton, 2);

            #endregion

            headersTab.Controls.Add(headersLayout);

            tabs.TabPages.Add(headersTab);
            #endregion

            #region Tags settings
            TabPage tagsTab = new TabPage("Tags");
            TableLayoutPanel tagsLayout = new TableLayoutPanel();
            tagsLayout.AutoSize = true;

            #region Add values

            TextBox newTagValueTextBox = new TextBox() { Text = string.Empty };
            newTagValueTextBox.Dock = DockStyle.Fill;
            tagsLayout.Controls.Add(newTagValueTextBox, 0, 1);
            tagsLayout.SetColumnSpan(newTagValueTextBox, 2);

            Button addTagButton = new Button() { Text = "Add tag" };
            addTagButton.Dock = DockStyle.Fill;
            addTagButton.AutoSize = true;
            tagsLayout.Controls.Add(addTagButton, 0, 2);
            tagsLayout.SetColumnSpan(addTagButton, 2);

            #endregion

            tagsTab.Controls.Add(tagsLayout);

            tabs.TabPages.Add(tagsTab);
            #endregion

            #region OAuth2 settings
            TabPage oauth2Tab = new TabPage("OAuth2");
            TableLayoutPanel oauth2Layout = new TableLayoutPanel();
            oauth2Layout.AutoSize = true;

            #region Port
            oauth2Layout.Controls.Add(new Label { Width=150, Text = "Port", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            oauth2PortTextBox = new NumericUpDown() { Width = 400, Maximum = 100000, Value = servicePanel.service.OAuth2.ContainsKey("port") ? (decimal)servicePanel.service.OAuth2["port"] : 5000 };
            oauth2PortTextBox.Dock = DockStyle.Fill;
            oauth2PortTextBox.TextChanged += Oauth2PortTextBox_TextChanged;
            oauth2Layout.Controls.Add(oauth2PortTextBox, 1, 1);
            #endregion

            #region Timeout
            oauth2Layout.Controls.Add(new Label { Width = 150, Text = "Timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            oauth2TimeoutTextBox = new NumericUpDown() { Maximum=1000, Value = servicePanel.service.OAuth2.ContainsKey("timeout") ? (decimal)servicePanel.service.OAuth2["timeout"] : 60 };
            oauth2TimeoutTextBox.Dock = DockStyle.Fill;
            oauth2TimeoutTextBox.TextChanged += Oauth2TimeoutTextBox_TextChanged;
            oauth2Layout.Controls.Add(oauth2TimeoutTextBox, 1, 2);
            #endregion

            #region Success display time
            oauth2Layout.Controls.Add(new Label { Width = 150, Text = "Success display time", TextAlign = ContentAlignment.BottomLeft }, 0, 3);
            oauth2SuccessDisplayTimeTextBox = new NumericUpDown() { Maximum = 100000, Value = servicePanel.service.OAuth2.ContainsKey("success_display_time") ? (decimal)servicePanel.service.OAuth2["success_display_time"] : 1 };
            oauth2SuccessDisplayTimeTextBox.Dock = DockStyle.Fill;
            oauth2SuccessDisplayTimeTextBox.TextChanged += Oauth2SuccessDisplayTimeTextBox_TextChanged;
            oauth2Layout.Controls.Add(oauth2SuccessDisplayTimeTextBox, 1, 3);
            #endregion

            #region Failure display time
            oauth2Layout.Controls.Add(new Label { Width = 150, Text = "Failure display time", TextAlign = ContentAlignment.BottomLeft }, 0, 4);
            oauth2FailureDisplayTimeTextBox = new NumericUpDown() { Maximum = 100000, Value = servicePanel.service.OAuth2.ContainsKey("failure_display_time") ? (decimal)servicePanel.service.OAuth2["failure_display_time"] : 5000 };
            oauth2FailureDisplayTimeTextBox.Dock = DockStyle.Fill;
            oauth2FailureDisplayTimeTextBox.TextChanged += Oauth2FailureDisplayTimeTextBox_TextChanged;
            oauth2Layout.Controls.Add(oauth2FailureDisplayTimeTextBox, 1, 4);
            #endregion

            oauth2Tab.Controls.Add(oauth2Layout);

            tabs.TabPages.Add(oauth2Tab);
            #endregion

            #region Basic Authentication settings
            TabPage basicTab = new TabPage("Basic");
            TableLayoutPanel basicLayout = new TableLayoutPanel();
            basicLayout.AutoSize = true;

            #region Username
            basicLayout.Controls.Add(new Label { Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            basicUsernameTextBox = new TextBox() { Width = 450, Text = servicePanel.service.Basic.ContainsKey("username") ? (string)servicePanel.service.Basic["username"] : string.Empty };
            basicUsernameTextBox.Dock = DockStyle.Fill;
            basicUsernameTextBox.TextChanged += BasicUsernameTextBox_TextChanged;
            basicLayout.Controls.Add(basicUsernameTextBox, 1, 1);
            #endregion

            #region Password
            basicLayout.Controls.Add(new Label { Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            basicPasswordTextBox = new TextBox() { Width = 450, Text = servicePanel.service.Basic.ContainsKey("password") ? (string)servicePanel.service.Basic["password"] : string.Empty };
            basicPasswordTextBox.Dock = DockStyle.Fill;
            basicPasswordTextBox.TextChanged += BasicPasswordTextBox_TextChanged;
            basicLayout.Controls.Add(basicPasswordTextBox, 1, 2);
            #endregion

            basicTab.Controls.Add(basicLayout);

            tabs.TabPages.Add(basicTab);
            #endregion

            #region NTLM Authentication settings
            TabPage ntlmTab = new TabPage("NTLM");
            TableLayoutPanel ntlmLayout = new TableLayoutPanel();
            ntlmLayout.AutoSize = true;

            #region Username
            ntlmLayout.Controls.Add(new Label { Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            ntlmUsernameTextBox = new TextBox() { Width = 450, Text = servicePanel.service.Basic.ContainsKey("username") ? (string)servicePanel.service.Basic["username"] : string.Empty };
            ntlmUsernameTextBox.Dock = DockStyle.Fill;
            ntlmUsernameTextBox.TextChanged += NtlmUsernameTextBox_TextChanged;
            ntlmLayout.Controls.Add(ntlmUsernameTextBox, 1, 1);
            #endregion

            #region Password
            ntlmLayout.Controls.Add(new Label { Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            ntlmPasswordTextBox = new TextBox() { Width = 450, Text = servicePanel.service.Basic.ContainsKey("password") ? (string)servicePanel.service.Basic["password"] : string.Empty };
            ntlmPasswordTextBox.Dock = DockStyle.Fill;
            ntlmPasswordTextBox.TextChanged += NtlmPasswordTextBox_TextChanged;
            ntlmLayout.Controls.Add(ntlmPasswordTextBox, 1, 2);
            #endregion

            ntlmTab.Controls.Add(ntlmLayout);

            tabs.TabPages.Add(ntlmTab);
            #endregion

            Controls.Add(tabs);
        }

        private void NtlmPasswordTextBox_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(ntlmPasswordTextBox.Text))
                servicePanel.service.Ntlm.Remove("password");
            else
                servicePanel.service.Ntlm["password"] = ntlmPasswordTextBox.Text;
        }

        private void NtlmUsernameTextBox_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(ntlmUsernameTextBox.Text))
                servicePanel.service.Ntlm.Remove("username");
            else
                servicePanel.service.Ntlm["username"] = ntlmUsernameTextBox.Text;
        }

        private void BasicPasswordTextBox_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(basicPasswordTextBox.Text))
                servicePanel.service.Basic.Remove("password");
            else
                servicePanel.service.Basic["password"] = basicPasswordTextBox.Text;
        }

        private void BasicUsernameTextBox_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(basicUsernameTextBox.Text))
                servicePanel.service.Basic.Remove("username");
            else
                servicePanel.service.Basic["username"] = basicUsernameTextBox.Text;
        }

        private void Oauth2FailureDisplayTimeTextBox_TextChanged(object sender, EventArgs e)
        {
            if (oauth2FailureDisplayTimeTextBox.Value == 0)
                servicePanel.service.OAuth2.Remove("failure_display_time");
            else
                servicePanel.service.OAuth2["failure_display_time"] = oauth2FailureDisplayTimeTextBox.Value;
        }

        private void Oauth2SuccessDisplayTimeTextBox_TextChanged(object sender, EventArgs e)
        {
            if (oauth2SuccessDisplayTimeTextBox.Value == 0)
                servicePanel.service.OAuth2.Remove("success_display_time");
            else
                servicePanel.service.OAuth2["success_display_time"] = oauth2SuccessDisplayTimeTextBox.Value;
        }

        private void Oauth2PortTextBox_TextChanged(object sender, EventArgs e)
        {
            if (oauth2PortTextBox.Value == 0)
                servicePanel.service.OAuth2.Remove("port");
            else
                servicePanel.service.OAuth2["port"] = oauth2PortTextBox.Value;
        }

        private void Oauth2TimeoutTextBox_TextChanged(object sender, EventArgs e)
        {
            if (oauth2TimeoutTextBox.Value == 0)
                servicePanel.service.OAuth2.Remove("timeout");
            else
                servicePanel.service.OAuth2["timeout"] = oauth2TimeoutTextBox.Value;
        }

        private void NoProxyTextBox_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(noProxyTextBox.Text))
                servicePanel.service.Proxies.Remove("no_proxy");
            else
                servicePanel.service.Proxies["no_proxy"] = noProxyTextBox.Text;
        }

        private void HttpsProxyTextBox_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(httpsProxyTextBox.Text))
                servicePanel.service.Proxies.Remove("https");
            else
                servicePanel.service.Proxies["https"] = httpsProxyTextBox.Text;
        }

        private void HttpProxyTextBox_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(httpProxyTextBox.Text))
                servicePanel.service.Proxies.Remove("http");
            else
                servicePanel.service.Proxies["http"] = httpProxyTextBox.Text;
        }

        private void SwaggerReadTimeoutTextBox_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.SwaggerReadTimeout = SwaggerReadTimeoutTextBox.Value;
        }

        private void ReadTimeoutTextBox_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.ReadTimeout = ReadTimeoutTextBox.Value;
        }

        private void ConnectTimeoutTextBox_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.ConnectTimeout = ConnectTimeoutTextBox.Value;
        }

        private void MaxRetriesTextBox_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.MaxRetries = (int)MaxRetriesTextBox.Value;
        }

        private void RelyOnDefinitions_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.RelyOnDefinitions = relyOnDefinitions.Checked;
        }

        internal string GetProxyFor(string url)
        {
            if (noProxyTextBox.Text.Length > 0 && url.StartsWith(noProxyTextBox.Text))
                return null;

            if (url.StartsWith("http:"))
                return httpProxyTextBox.Text;
            if (url.StartsWith("https:"))
                return httpsProxyTextBox.Text;
            return null;
        }

        private void ServiceHostTextBox_TextChanged(object sender, EventArgs e)
        {
            servicePanel.service.ServiceHost = serviceHostTextBox.Text;
        }

        private void Head_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Head = head.Checked;
        }

        private void Options_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Options = options.Checked;
        }

        private void Patch_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Patch = patch.Checked;
        }

        private void Delete_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Delete = delete.Checked;
        }

        private void Put_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Put = put.Checked;
        }

        private void Post_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Post = post.Checked;
        }

        private void Get_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Get = get.Checked;
        }

        private void ApiKeyTextBox_TextChanged(object sender, EventArgs e)
        {
            servicePanel.service.ApiKey = apiKeyTextBox.Text;
        }

        private void Asynchronous_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Asynchronous = asynchronous.Checked;
        }

        private void Synchronous_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Synchronous = synchronous.Checked;
        }

        //        private void SecurityDetailsTextBox_TextChanged(object sender, EventArgs e)
        //        {
        //            var securityDetailsRegex = new Regex("^(([^\n,]+)=([^\n,]*))(,([^\n,]+)=([^\n,]*))*$");
        //            if(securityDetailsRegex.IsMatch(securityDetailsTextBox.Text)) {
        //                securityDetailsTextBox.BackColor = Color.LightGreen;
        //                service.SecurityDetails = securityDetailsTextBox.Text;
        //            }
        //            else
        //            {
        //                securityDetailsTextBox.BackColor = string.IsNullOrEmpty(securityDetailsTextBox.Text) ? Color.Empty : Color.Red;
        //               service.SecurityDetails = string.Empty;
        //           }
        //       }

        //        private void ProxiesTextBox_TextChanged(object sender, EventArgs e)
        //        {
        //service.Proxies = proxiesTextBox.Text;
        //swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
        //}
    }
}
