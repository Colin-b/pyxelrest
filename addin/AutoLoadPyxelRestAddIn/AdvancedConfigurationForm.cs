using System;
using System.Collections.Generic;
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
        private AddButton addTag;

        private TableLayoutPanel operationIDsPanel;
        private TextBox operationIDName;
        private AddButton addOperationID;

        private TableLayoutPanel headersPanel;
        private TextBox headerName;
        private TextBox headerValue;
        private AddButton addHeader;

        private TableLayoutPanel oauth2ParamsPanel;
        private TextBox oauth2ParamName;
        private TextBox oauth2ParamValue;
        private AddButton addOAuth2Param;

        public AdvancedConfigurationForm(ServicePanel servicePanel)
        {
            this.servicePanel = servicePanel;
            InitializeComponent();

            foreach (var header in servicePanel.service.Headers)
                AddHeader(header.Key, header.Value.ToString());

            if (servicePanel.service.OpenAPI.ContainsKey("excluded_tags"))
                foreach (var tag in (IList<string>)servicePanel.service.OpenAPI["excluded_tags"])
                    AddTag(tag, true);

            if (servicePanel.service.OpenAPI.ContainsKey("selected_tags"))
                foreach (var tag in (IList<string>)servicePanel.service.OpenAPI["selected_tags"])
                    AddTag(tag, false);

            if (servicePanel.service.OpenAPI.ContainsKey("excluded_operation_ids"))
                foreach (var tag in (IList<string>)servicePanel.service.OpenAPI["excluded_operation_ids"])
                    AddOperationID(tag, true);

            if (servicePanel.service.OpenAPI.ContainsKey("selected_operation_ids"))
                foreach (var tag in (IList<string>)servicePanel.service.OpenAPI["selected_operation_ids"])
                    AddOperationID(tag, false);

            var oauth2NonParam = new List<string> { "port", "timeout", "success_display_time", "failure_display_time" };
            foreach (var oauth2Item in servicePanel.service.OAuth2)
            {
                if (!oauth2NonParam.Contains(oauth2Item.Key))
                    AddOAuth2Param(oauth2Item.Key, oauth2Item.Value.ToString());
            }
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

                #region Methods
                {
                    layout.Controls.Add(new Label { Text = "Methods", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                    var panel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };

                    var get = new CheckBox { Text = "get", Checked = servicePanel.service.Get, Width = 50 };
                    get.CheckedChanged += Get_CheckedChanged;
                    panel.Controls.Add(get, 0, 0);
                    var post = new CheckBox { Text = "post", Checked = servicePanel.service.Post, Width = 55 };
                    post.CheckedChanged += Post_CheckedChanged;
                    panel.Controls.Add(post, 1, 0);
                    var put = new CheckBox { Text = "put", Checked = servicePanel.service.Put, Width = 50 };
                    put.CheckedChanged += Put_CheckedChanged;
                    panel.Controls.Add(put, 2, 0);
                    var delete = new CheckBox { Text = "delete", Checked = servicePanel.service.Delete, Width = 65 };
                    delete.CheckedChanged += Delete_CheckedChanged;
                    panel.Controls.Add(delete, 3, 0);
                    var patch = new CheckBox { Text = "patch", Checked = servicePanel.service.Patch, Width = 60 };
                    patch.CheckedChanged += Patch_CheckedChanged;
                    panel.Controls.Add(patch, 4, 0);
                    var options = new CheckBox { Text = "options", Checked = servicePanel.service.Options, Width = 70 };
                    options.CheckedChanged += Options_CheckedChanged;
                    panel.Controls.Add(options, 5, 0);
                    var head = new CheckBox { Text = "head", Checked = servicePanel.service.Head, Width = 60 };
                    head.CheckedChanged += Head_CheckedChanged;
                    panel.Controls.Add(head, 6, 0);

                    layout.Controls.Add(panel, 1, 1);
                }
                #endregion

                #region Max retries
                layout.Controls.Add(new Label { Text = "Max retries", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                var maxRetries = new NumericUpDown { Value = servicePanel.service.MaxRetries, Dock = DockStyle.Fill };
                maxRetries.ValueChanged += MaxRetries_ValueChanged;
                layout.Controls.Add(maxRetries, 1, 2);
                #endregion

                #region Timeout

                #region Connect timeout
                layout.Controls.Add(new Label { Text = "Connect timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 3);

                var connectTimeout = new NumericUpDown { Value = servicePanel.service.ConnectTimeout, Dock = DockStyle.Fill };
                connectTimeout.ValueChanged += ConnectTimeout_ValueChanged;
                layout.Controls.Add(connectTimeout, 1, 3);
                #endregion

                #region Read timeout
                layout.Controls.Add(new Label { Text = "Read timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 4);

                var readTimeout = new NumericUpDown { Value = servicePanel.service.ReadTimeout, Dock = DockStyle.Fill };
                readTimeout.ValueChanged += ReadTimeout_ValueChanged;
                layout.Controls.Add(readTimeout, 1, 4);
                #endregion

                #endregion

                #region API Key
                layout.Controls.Add(new Label { Text = "API key", TextAlign = ContentAlignment.BottomLeft }, 0, 5);

                var apiKey = new TextBox { Text = servicePanel.service.ApiKey, Dock = DockStyle.Fill };
                apiKey.TextChanged += ApiKey_TextChanged;
                layout.Controls.Add(apiKey, 1, 5);
                #endregion

                #region Return behavior
                {
                    layout.Controls.Add(new Label { Text = "Return types", TextAlign = ContentAlignment.BottomLeft }, 0, 6);

                    var panel = new TableLayoutPanel { Height = 30, Dock = DockStyle.Fill };

                    #region UDF Return types
                    var vbaCompatible = new CheckBox { Text = "VBA compatible", Checked = servicePanel.service.Udf.ContainsKey("return_types") ? ((IList<string>)servicePanel.service.Udf["return_types"]).Contains("vba_compatible") : false };
                    vbaCompatible.CheckedChanged += VBACompatible_CheckedChanged;
                    panel.Controls.Add(vbaCompatible, 0, 0);

                    var synchronousAutoExpand = new RadioButton { Text = "Auto expand (synchronous)", Checked = servicePanel.service.Udf.ContainsKey("return_types") ? ((IList<string>)servicePanel.service.Udf["return_types"]).Contains("sync_auto_expand") : true, Width = 160 };
                    synchronousAutoExpand.CheckedChanged += SynchronousAutoExpand_CheckedChanged;
                    panel.Controls.Add(synchronousAutoExpand, 1, 0);

                    var asynchronousAutoExpand = new RadioButton { Text = "Auto expand (asynchronous)", Checked = servicePanel.service.Udf.ContainsKey("return_types") ? ((IList<string>)servicePanel.service.Udf["return_types"]).Contains("async_auto_expand") : false, Width = 170 };
                    asynchronousAutoExpand.CheckedChanged += AsynchronousAutoExpand_CheckedChanged;
                    panel.Controls.Add(asynchronousAutoExpand, 2, 0);
                    #endregion

                    layout.Controls.Add(panel, 1, 6);
                }
                #endregion

                #region Shift results
                {
                    layout.Controls.Add(new Label { Text = "UDF ", TextAlign = ContentAlignment.BottomLeft }, 0, 7);

                    var panel = new TableLayoutPanel { Height = 30, Dock = DockStyle.Fill };

                    var shiftResult = new CheckBox { Text = "Shift results", Checked = servicePanel.service.Udf.ContainsKey("shift_result") ? (bool)servicePanel.service.Udf["shift_result"] : false };
                    shiftResult.CheckedChanged += ShiftResult_CheckedChanged;
                    panel.Controls.Add(shiftResult, 0, 0);

                    layout.Controls.Add(panel, 1, 7);
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

                var nameLabel = new Label { Text="Name", Dock = DockStyle.Fill, Width=200 };
                layout.Controls.Add(nameLabel, 0, 1);

                var valueLabel = new Label { Text = "Value", Dock = DockStyle.Fill, Width=330 };
                layout.Controls.Add(valueLabel, 1, 1);

                headersPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                layout.Controls.Add(headersPanel, 0, 2);
                layout.SetColumnSpan(headersPanel, 3);

                headerName = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                headerName.TextChanged += HeaderName_TextChanged;
                headerName.KeyDown += HeaderName_KeyDown;
                layout.Controls.Add(headerName, 0, 3);

                headerValue = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                headerValue.TextChanged += HeaderValue_TextChanged;
                headerValue.KeyDown += HeaderValue_KeyDown;
                layout.Controls.Add(headerValue, 1, 3);

                addHeader = new AddButton();
                addHeader.Click += AddHeader_Click;
                layout.Controls.Add(addHeader, 2, 3);

                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            if (!"pyxelrest".Equals(servicePanel.service.Name))
            {
                #region OpenAPI settings
                {
                    var tab = new TabPage("OpenAPI");
                    var layout = new TableLayoutPanel { AutoSize = true };

                    #region Service Host
                    {
                        var hostPanel = new TableLayoutPanel { Dock = DockStyle.Fill, Width = 530, Height=30 };

                        hostPanel.Controls.Add(new Label { Text = "Service Host", TextAlign = ContentAlignment.BottomLeft, Width = 130 }, 0, 1);

                        var serviceHost = new TextBox { Text = servicePanel.service.OpenAPI.ContainsKey("service_host") ? servicePanel.service.OpenAPI["service_host"].ToString() : string.Empty, Width = 400 };
                        serviceHost.TextChanged += ServiceHost_TextChanged;
                        hostPanel.Controls.Add(serviceHost, 1, 1);

                        layout.Controls.Add(hostPanel);
                    }
                    #endregion

                    {
                        var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Width = 530, Height = 30 };

                        #region OpenAPI Definition read timeout
                        panel.Controls.Add(new Label { Text = "Definition read timeout", TextAlign = ContentAlignment.BottomLeft, Width = 130 }, 0, 1);

                        var openAPIDefinitionReadTimeout = new NumericUpDown { Value = servicePanel.service.OpenAPI.ContainsKey("definition_read_timeout") ? decimal.Parse(servicePanel.service.OpenAPI["definition_read_timeout"].ToString()) : 5, Width = 200 };
                        openAPIDefinitionReadTimeout.ValueChanged += OpenAPIDefinitionReadTimeout_ValueChanged;
                        panel.Controls.Add(openAPIDefinitionReadTimeout, 1, 1);
                        #endregion

                        #region Rely on definitions
                        var relyOnDefinitions = new CheckBox { Text = "Rely on definitions", Checked = servicePanel.service.OpenAPI.ContainsKey("rely_on_definitions") ? bool.Parse(servicePanel.service.OpenAPI["rely_on_definitions"].ToString()) : false, Width = 200 };
                        relyOnDefinitions.CheckedChanged += RelyOnDefinitions_CheckedChanged;
                        panel.Controls.Add(relyOnDefinitions, 2, 1);
                        #endregion

                        layout.Controls.Add(panel);
                    }

                    #region Tags

                    var tagsLabel = new Label { Dock = DockStyle.Fill, Width = 580, Text = "Tags" };
                    layout.Controls.Add(tagsLabel);

                    tagsPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                    layout.Controls.Add(tagsPanel);

                    {
                        var addPanel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 30 };

                        tagName = new TextBox { Text = string.Empty, Width = 530 };
                        tagName.TextChanged += TagName_TextChanged;
                        tagName.KeyDown += TagName_KeyDown;
                        addPanel.Controls.Add(tagName, 0, 1);

                        addTag = new AddButton();
                        addTag.Click += AddTag_Click;
                        addPanel.Controls.Add(addTag, 1, 1);

                        layout.Controls.Add(addPanel);
                    }

                    #endregion

                    #region Operation IDs

                    var operationIdsLabel = new Label { Dock = DockStyle.Fill, Width = 580, Text = "Operation IDs" };
                    layout.Controls.Add(operationIdsLabel);

                    operationIDsPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                    layout.Controls.Add(operationIDsPanel);

                    {
                        var addPanel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 30 };

                        operationIDName = new TextBox { Text = string.Empty, Width = 530 };
                        operationIDName.TextChanged += OperationIDName_TextChanged;
                        operationIDName.KeyDown += OperationIDName_KeyDown;
                        addPanel.Controls.Add(operationIDName, 0, 1);

                        addOperationID = new AddButton();
                        addOperationID.Click += AddOperationID_Click;
                        addPanel.Controls.Add(addOperationID, 1, 1);

                        layout.Controls.Add(addPanel);
                    }

                    #endregion

                    tab.Controls.Add(layout);
                    tabs.TabPages.Add(tab);
                }
                #endregion
            }

            #region OAuth2 settings
            {
                var tab = new TabPage("OAuth2");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Port
                layout.Controls.Add(new Label { Width = 150, Text = "Port", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                var port = new NumericUpDown { Width = 380, Maximum = 100000, Dock = DockStyle.Fill, Value = servicePanel.service.OAuth2.ContainsKey("port") ? (decimal)servicePanel.service.OAuth2["port"] : 5000 };
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

                #region Add items

                oauth2ParamsPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                layout.Controls.Add(oauth2ParamsPanel, 0, 5);
                layout.SetColumnSpan(oauth2ParamsPanel, 3);

                oauth2ParamName = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                oauth2ParamName.TextChanged += Oauth2ParamName_TextChanged;
                oauth2ParamName.KeyDown += Oauth2ParamName_KeyDown;
                layout.Controls.Add(oauth2ParamName, 0, 6);

                oauth2ParamValue = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                oauth2ParamValue.TextChanged += Oauth2ParamValue_TextChanged;
                oauth2ParamValue.KeyDown += Oauth2ParamValue_KeyDown;
                layout.Controls.Add(oauth2ParamValue, 1, 6);

                addOAuth2Param = new AddButton();
                addOAuth2Param.Click += AddOAuth2Param_Click;
                layout.Controls.Add(addOAuth2Param, 2, 6);

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

                var password = new TextBox { UseSystemPasswordChar = true, Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Basic.ContainsKey("password") ? (string)servicePanel.service.Basic["password"] : string.Empty };
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

                var userName = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Ntlm.ContainsKey("username") ? (string)servicePanel.service.Ntlm["username"] : string.Empty };
                userName.TextChanged += NtlmUsername_TextChanged;
                layout.Controls.Add(userName, 1, 1);
                #endregion

                #region Password
                layout.Controls.Add(new Label { Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                var password = new TextBox { UseSystemPasswordChar = true, Width = 450, Dock = DockStyle.Fill, Text = servicePanel.service.Ntlm.ContainsKey("password") ? (string)servicePanel.service.Ntlm["password"] : string.Empty };
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
            servicePanel.openAPIDefinitionTicks = DateTime.UtcNow.Ticks;
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Proxies.Remove("no_proxy");
            else
                servicePanel.service.Proxies["no_proxy"] = ((TextBox)sender).Text;
        }

        private void HttpsProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.openAPIDefinitionTicks = DateTime.UtcNow.Ticks;
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Proxies.Remove("https");
            else
                servicePanel.service.Proxies["https"] = ((TextBox)sender).Text;
        }

        private void HttpProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.openAPIDefinitionTicks = DateTime.UtcNow.Ticks;
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Proxies.Remove("http");
            else
                servicePanel.service.Proxies["http"] = ((TextBox)sender).Text;
        }

        private void OpenAPIDefinitionReadTimeout_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.OpenAPI["definition_read_timeout"] = ((NumericUpDown)sender).Value;
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
            servicePanel.service.OpenAPI["rely_on_definitions"] = ((CheckBox)sender).Checked;
        }

        private void ServiceHost_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.OpenAPI.Remove("service_host");
            else
                servicePanel.service.OpenAPI["service_host"] = ((TextBox)sender).Text;
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

        private void AsynchronousAutoExpand_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked)
                AddValueToUdfList("async_auto_expand", "return_types");
            else
                RemoveValueToUdfList("async_auto_expand", "return_types");
        }

        private void SynchronousAutoExpand_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked)
                AddValueToUdfList("sync_auto_expand", "return_types");
            else
                RemoveValueToUdfList("sync_auto_expand", "return_types");
        }

        private void VBACompatible_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
                AddValueToUdfList("vba_compatible", "return_types");
            else
                RemoveValueToUdfList("vba_compatible", "return_types");
        }

        private void AddValueToUdfList(string value, string listName)
        {
            if (!servicePanel.service.Udf.ContainsKey(listName))
                servicePanel.service.Udf[listName] = new List<string>();

            ((IList<string>)servicePanel.service.Udf[listName]).Add(value);
        }

        private void RemoveValueToUdfList(string value, string listName)
        {
            if (servicePanel.service.Udf.ContainsKey(listName))
                ((IList<string>)servicePanel.service.Udf[listName]).Remove(value);
        }

        private void ShiftResult_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Udf["shift_result"] = ((CheckBox)sender).Checked;
        }

        private void AddValueToList(string value, string listName)
        {
            if (!servicePanel.service.OpenAPI.ContainsKey(listName))
                servicePanel.service.OpenAPI[listName] = new List<string>();

            ((IList<string>)servicePanel.service.OpenAPI[listName]).Add(value);
        }

        private bool ContainsValue(string value, string listName)
        {
            if (!servicePanel.service.OpenAPI.ContainsKey(listName))
                return false;

            return ((IList<string>)servicePanel.service.OpenAPI[listName]).Contains(value);
        }

        private void MoveFromListToList(string value, string fromList, string toList)
        {
            RemoveValueFromList(value, fromList);
            AddValueToList(value, toList);
        }

        private void RemoveValueFromList(string value, string listName)
        {
            var values = (IList<string>)servicePanel.service.OpenAPI[listName];
            values.Remove(value);
            if (values.Count == 0)
                servicePanel.service.OpenAPI.Remove(listName);
        }

        #region Tags

        private void TagName_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addTag.Enabled)
                        AddTag();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void TagName_TextChanged(object sender, EventArgs e)
        {
            var tagValue = ((TextBox)sender).Text;
            addTag.Enabled = tagValue.Length > 0 && !ContainsValue(tagValue, "selected_tags") && !ContainsValue(tagValue, "excluded_tags");
        }

        private void AddTag_Click(object sender, EventArgs e)
        {
            AddTag();
        }

        private void AddTag()
        {
            // Service update
            AddValueToList(tagName.Text, "selected_tags");
            // Visual update
            AddTag(tagName.Text, false);
            tagName.Text = "";
        }

        private void AddTag(string value, bool excluded)
        {
            var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 25 };

            panel.Controls.Add(new Label { Name = "tagLabel", Text = value, Width = 335, Dock = DockStyle.Fill }, 0, 1);

            panel.Controls.Add(new RadioButton { Text = "excluded", Width = 90, Checked = excluded }, 1, 1);

            var tagSelected = new RadioButton { Name = "tagSelected", Text = "selected", Width = 90, Checked = !excluded };
            tagSelected.CheckedChanged += TagSelected_CheckedChanged;
            panel.Controls.Add(tagSelected, 2, 1);

            var remove = new DeleteButton();
            remove.Click += RemoveTag_Click;
            panel.Controls.Add(remove, 3, 1);

            tagsPanel.Controls.Add(panel);
            tagsPanel.SetColumnSpan(panel, 2);
        }

        private void TagSelected_CheckedChanged(object sender, EventArgs e)
        {
            var tagSelected = (RadioButton) sender;
            Label tagLabel = (Label)tagSelected.Parent.Controls.Find("tagLabel", false)[0];

            if (tagSelected.Checked) // Moved from excluded to selected
                MoveFromListToList(tagLabel.Text, "excluded_tags", "selected_tags");
            else // Move from selected to excluded
                MoveFromListToList(tagLabel.Text, "selected_tags", "excluded_tags");
        }

        private void RemoveTag_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            var tagLabel = (Label) panel.Controls.Find("tagLabel", false)[0];
            var tagSelected = (RadioButton)panel.Controls.Find("tagSelected", false)[0];

            RemoveValueFromList(tagLabel.Text, tagSelected.Checked ? "selected_tags" : "excluded_tags");

            tagsPanel.Controls.Remove(panel);
        }

        #endregion

        #region Operation IDs

        private void OperationIDName_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addOperationID.Enabled)
                        AddOperationID();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void OperationIDName_TextChanged(object sender, EventArgs e)
        {
            var operationIDValue = ((TextBox)sender).Text;
            addOperationID.Enabled = operationIDValue.Length > 0 && !ContainsValue(operationIDValue, "selected_operation_ids") && !ContainsValue(operationIDValue, "excluded_operation_ids");
        }

        private void AddOperationID_Click(object sender, EventArgs e)
        {
            AddOperationID();
        }

        private void AddOperationID()
        {
            // Service update
            AddValueToList(operationIDName.Text, "selected_operation_ids");
            // Visual update
            AddOperationID(operationIDName.Text, false);
            operationIDName.Text = "";
        }

        private void AddOperationID(string value, bool excluded)
        {
            var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 25 };

            panel.Controls.Add(new Label { Name = "operationIDLabel", Text = value, Width = 335, Dock = DockStyle.Fill }, 0, 1);

            panel.Controls.Add(new RadioButton { Text = "excluded", Width = 90, Checked = excluded }, 1, 1);

            var operationIDSelected = new RadioButton { Name = "operationIDSelected", Text = "selected", Width = 90, Checked = !excluded };
            operationIDSelected.CheckedChanged += OperationIDSelected_CheckedChanged;
            panel.Controls.Add(operationIDSelected, 2, 1);

            var remove = new DeleteButton();
            remove.Click += RemoveOperationID_Click;
            panel.Controls.Add(remove, 3, 1);

            operationIDsPanel.Controls.Add(panel);
            operationIDsPanel.SetColumnSpan(panel, 2);
        }

        private void OperationIDSelected_CheckedChanged(object sender, EventArgs e)
        {
            var operationIDSelected = (RadioButton)sender;
            Label operationIDLabel = (Label)operationIDSelected.Parent.Controls.Find("operationIDLabel", false)[0];

            if (operationIDSelected.Checked) // Moved from excluded to selected
                MoveFromListToList(operationIDLabel.Text, "excluded_operation_ids", "selected_operation_ids");
            else // Move from selected to excluded
                MoveFromListToList(operationIDLabel.Text, "selected_operation_ids", "excluded_operation_ids");
        }

        private void RemoveOperationID_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            var operationIDLabel = (Label)panel.Controls.Find("operationIDLabel", false)[0];
            var operationIDSelected = (RadioButton)panel.Controls.Find("operationIDSelected", false)[0];

            RemoveValueFromList(operationIDLabel.Text, operationIDSelected.Checked ? "selected_operation_ids" : "excluded_operation_ids");

            operationIDsPanel.Controls.Remove(panel);
        }

        #endregion

        private void HeaderValue_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addHeader.Enabled)
                        AddHeader();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void HeaderValue_TextChanged(object sender, EventArgs e)
        {
            addHeader.Enabled = ((TextBox)sender).Text.Length > 0 && headerName.Text.Length > 0;
        }

        private void HeaderName_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addHeader.Enabled)
                        AddHeader();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private bool ContainsHeader(string value)
        {
            return servicePanel.service.Headers.ContainsKey(value);
        }

        private void HeaderName_TextChanged(object sender, EventArgs e)
        {
            addHeader.Enabled = ((TextBox)sender).Text.Length > 0 && headerValue.Text.Length > 0 && !ContainsHeader(((TextBox)sender).Text);
        }

        private void AddHeader_Click(object sender, EventArgs e)
        {
            AddHeader();
        }

        private void AddHeader()
        {
            servicePanel.service.Headers.Add(headerName.Text, headerValue.Text);

            AddHeader(headerName.Text, headerValue.Text);

            headerName.Text = "";
            headerValue.Text = "";
        }

        private void AddHeader(string name, string value)
        {
            var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 25 };

            panel.Controls.Add(new Label { Name = "headerNameLabel", Text = name, Width = 195, Dock = DockStyle.Fill }, 0, 1);

            var valueTextBox = new TextBox { Text = value, Width = 330, Dock = DockStyle.Fill };
            valueTextBox.TextChanged += ExistingHeaderValue_TextChanged;
            panel.Controls.Add(valueTextBox, 1, 1);

            var remove = new DeleteButton();
            remove.Click += RemoveHeader_Click;
            panel.Controls.Add(remove, 2, 1);

            headersPanel.Controls.Add(panel);
            headersPanel.SetColumnSpan(panel, 3);
        }

        private void ExistingHeaderValue_TextChanged(object sender, EventArgs e)
        {
            var valueTextBox = (TextBox)sender;
            Label headerNameLabel = (Label)valueTextBox.Parent.Controls.Find("headerNameLabel", false)[0];

            servicePanel.service.Headers[headerNameLabel.Text] = valueTextBox.Text;
        }

        private void RemoveHeader_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            Label headerNameLabel = (Label)panel.Controls.Find("headerNameLabel", false)[0];

            servicePanel.service.Headers.Remove(headerNameLabel.Text);

            headersPanel.Controls.Remove(panel);
        }

        private void Oauth2ParamValue_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addOAuth2Param.Enabled)
                        AddOAuth2Param();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private bool ContainsOAuth2Param(string value)
        {
            return servicePanel.service.OAuth2.ContainsKey(value);
        }

        private void Oauth2ParamValue_TextChanged(object sender, EventArgs e)
        {
            addOAuth2Param.Enabled = ((TextBox)sender).Text.Length > 0 && oauth2ParamName.Text.Length > 0;
        }

        private void Oauth2ParamName_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addOAuth2Param.Enabled)
                        AddOAuth2Param();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void Oauth2ParamName_TextChanged(object sender, EventArgs e)
        {
            addOAuth2Param.Enabled = ((TextBox)sender).Text.Length > 0 && oauth2ParamValue.Text.Length > 0 && !ContainsOAuth2Param(((TextBox)sender).Text);
        }

        private void AddOAuth2Param_Click(object sender, EventArgs e)
        {
            AddOAuth2Param();
        }

        private void AddOAuth2Param()
        {
            servicePanel.service.OAuth2.Add(oauth2ParamName.Text, oauth2ParamValue.Text);

            AddOAuth2Param(oauth2ParamName.Text, oauth2ParamValue.Text);

            oauth2ParamName.Text = "";
            oauth2ParamValue.Text = "";
        }

        private void AddOAuth2Param(string name, string value)
        {
            var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 25 };

            panel.Controls.Add(new Label { Name = "oauth2ParamNameLabel", Text = name, Width = 145, Dock = DockStyle.Fill }, 0, 1);

            var valueTextBox = new TextBox { Text = value, Width = 380, Dock = DockStyle.Fill };
            valueTextBox.TextChanged += OAuth2ParamValue_TextChanged;
            panel.Controls.Add(valueTextBox, 1, 1);

            var remove = new DeleteButton();
            remove.Click += RemoveOAuth2Param_Click;
            panel.Controls.Add(remove, 2, 1);

            oauth2ParamsPanel.Controls.Add(panel);
            oauth2ParamsPanel.SetColumnSpan(panel, 3);
        }

        private void OAuth2ParamValue_TextChanged(object sender, EventArgs e)
        {
            var valueTextBox = (TextBox)sender;
            Label oauth2ParamNameLabel = (Label)valueTextBox.Parent.Controls.Find("oauth2ParamNameLabel", false)[0];

            servicePanel.service.OAuth2[oauth2ParamNameLabel.Text] = valueTextBox.Text;
        }

        private void RemoveOAuth2Param_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            Label oauth2ParamNameLabel = (Label)panel.Controls.Find("oauth2ParamNameLabel", false)[0];

            servicePanel.service.OAuth2.Remove(oauth2ParamNameLabel.Text);

            oauth2ParamsPanel.Controls.Remove(panel);
        }

        #endregion
    }
}
