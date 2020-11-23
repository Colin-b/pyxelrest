using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace PyxelRestAddIn
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

        private TableLayoutPanel parametersPanel;
        private TextBox parameterName;
        private AddButton addParameter;

        private TableLayoutPanel headersPanel;
        private TextBox headerName;
        private TextBox headerValue;
        private AddButton addHeader;

        private TableLayoutPanel oauth2ParamsPanel;
        private TextBox oauth2ParamName;
        private TextBox oauth2ParamValue;
        private AddButton addOAuth2Param;

        private CheckBox dynamicArrayFormulasLockExcel;

        private CheckBox legacyArrayFormulasLockExcel;

        private TableLayoutPanel pythonModulesPanel;
        private TextBox pythonModuleName;
        private AddButton addPythonModule;

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
            foreach (var oauth2Item in (IDictionary<string, object>)servicePanel.service.Auth["oauth2"])
            {
                if (!oauth2NonParam.Contains(oauth2Item.Key))
                    AddOAuth2Param(oauth2Item.Key, oauth2Item.Value.ToString());
            }

            foreach (var pythonModule in servicePanel.service.PythonModules)
                AddPythonModule(pythonModule);
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

        private int PercentWidth(int percent)
        {
            return (Size.Width * percent) / 100;
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

                    var get = new CheckBox { Text = "get", Checked = servicePanel.service.Get, Width = PercentWidth(11) };
                    get.CheckedChanged += Get_CheckedChanged;
                    panel.Controls.Add(get, 0, 0);
                    var post = new CheckBox { Text = "post", Checked = servicePanel.service.Post, Width = PercentWidth(11) };
                    post.CheckedChanged += Post_CheckedChanged;
                    panel.Controls.Add(post, 1, 0);
                    var put = new CheckBox { Text = "put", Checked = servicePanel.service.Put, Width = PercentWidth(11) };
                    put.CheckedChanged += Put_CheckedChanged;
                    panel.Controls.Add(put, 2, 0);
                    var patch = new CheckBox { Text = "patch", Checked = servicePanel.service.Patch, Width = PercentWidth(11) };
                    patch.CheckedChanged += Patch_CheckedChanged;
                    panel.Controls.Add(patch, 3, 0);
                    var delete = new CheckBox { Text = "delete", Checked = servicePanel.service.Delete, Width = PercentWidth(11) };
                    delete.CheckedChanged += Delete_CheckedChanged;
                    panel.Controls.Add(delete, 4, 0);

                    layout.Controls.Add(panel, 1, 1);
                }
                #endregion

                #region API Key
                {
                    layout.Controls.Add(new Label { Text = "API key", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "API key", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var apiKey = new TextBox { Text = (string)servicePanel.service.Auth["api_key"], Dock = DockStyle.Fill };
                    tooltip.SetToolTip(apiKey, "Only used when required.");
                    apiKey.TextChanged += ApiKey_TextChanged;
                    layout.Controls.Add(apiKey, 1, 2);
                }
                #endregion

                Dictionary<string, object> dynamicArrayFormulasOptions = servicePanel.service.Formulas.ContainsKey("dynamic_array") ? (Dictionary<string, object>)servicePanel.service.Formulas["dynamic_array"] : new Dictionary<string, object>();
                Dictionary<string, object> legacyArrayFormulasOptions = servicePanel.service.Formulas.ContainsKey("legacy_array") ? (Dictionary<string, object>)servicePanel.service.Formulas["legacy_array"] : new Dictionary<string, object>();
                Dictionary<string, object> vbaCompatibleFormulasOptions = servicePanel.service.Formulas.ContainsKey("vba_compatible") ? (Dictionary<string, object>)servicePanel.service.Formulas["vba_compatible"] : new Dictionary<string, object>();

                #region Formulas
                {
                    layout.Controls.Add(new Label { Text = "Formulas", TextAlign = ContentAlignment.BottomLeft }, 0, 3);

                    var panel = new TableLayoutPanel { Height = 30, Dock = DockStyle.Fill };

                    #region Array formulas
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate dynamic array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var dynamicArrayFormulas = new CheckBox { Text = "Dynamic array", Checked = dynamicArrayFormulasOptions.Count > 0 };
                        tooltip.SetToolTip(dynamicArrayFormulas, "If your version of Microsoft Excel supports dynamic array formulas, results will be spilled.\nOtherwise results will only fill selected cells.");
                        dynamicArrayFormulas.CheckedChanged += DynamicArrayFormulas_CheckedChanged;
                        panel.Controls.Add(dynamicArrayFormulas, 0, 0);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate legacy array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var legacyArrayFormulas = new CheckBox { Text = "Legacy array", Checked = legacyArrayFormulasOptions.Count > 0 };
                        tooltip.SetToolTip(legacyArrayFormulas, "If your version of Microsoft Excel does not supports dynamic array formulas, use this to spill results.");
                        legacyArrayFormulas.CheckedChanged += LegacyArrayFormulas_CheckedChanged;
                        panel.Controls.Add(legacyArrayFormulas, 1, 0);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate VBA compatible formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var vbaCompatibleFormulas = new CheckBox { Text = "Visual basic", Checked = vbaCompatibleFormulasOptions.Count > 0, Width = 160 };
                        tooltip.SetToolTip(vbaCompatibleFormulas, "Use this formula behavior if you want to call it using Visual Basic for Applications (VBA).");
                        vbaCompatibleFormulas.CheckedChanged += VBACompatibleFormulas_CheckedChanged;
                        panel.Controls.Add(vbaCompatibleFormulas, 2, 0);
                    }
                    #endregion

                    layout.Controls.Add(panel, 1, 3);
                }
                #endregion

                #region Dynamic array formulas behavior
                {
                    layout.Controls.Add(new Label { Text = "Dynamic array", TextAlign = ContentAlignment.BottomLeft }, 0, 4);

                    var panel = new TableLayoutPanel { Height = 30, Dock = DockStyle.Fill };


                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Lock Microsoft Excel while waiting for results", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var synchronousChecked = dynamicArrayFormulasOptions.ContainsKey("lock_excel") ? (bool)dynamicArrayFormulasOptions["lock_excel"] : false;
                        dynamicArrayFormulasLockExcel = new CheckBox { Text = "Wait for result", Checked = synchronousChecked };
                        tooltip.SetToolTip(dynamicArrayFormulasLockExcel, "Uncheck to still be able to use Microsoft Excel while waiting for results.");
                        dynamicArrayFormulasLockExcel.CheckedChanged += DynamicArrayFormulasLockExcel_CheckedChanged;
                        dynamicArrayFormulasLockExcel.Enabled = dynamicArrayFormulasOptions.Count > 0;
                        panel.Controls.Add(dynamicArrayFormulasLockExcel, 0, 0);
                    }

                    layout.Controls.Add(panel, 1, 4);
                }
                #endregion

                #region Legacy array formulas behavior
                {
                    layout.Controls.Add(new Label { Text = "Legacy array", TextAlign = ContentAlignment.BottomLeft }, 0, 5);

                    var panel = new TableLayoutPanel { Height = 30, Dock = DockStyle.Fill };

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Lock Microsoft Excel while waiting for results", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var synchronousChecked = legacyArrayFormulasOptions.ContainsKey("lock_excel") ? (bool)legacyArrayFormulasOptions["lock_excel"] : false;
                        legacyArrayFormulasLockExcel = new CheckBox { Text = "Wait for result", Checked = synchronousChecked };
                        tooltip.SetToolTip(legacyArrayFormulasLockExcel, "Uncheck to still be able to use Microsoft Excel while waiting for results.");
                        legacyArrayFormulasLockExcel.CheckedChanged += LegacyArrayFormulasLockExcel_CheckedChanged;
                        legacyArrayFormulasLockExcel.Enabled = legacyArrayFormulasOptions.Count > 0;
                        panel.Controls.Add(legacyArrayFormulasLockExcel, 0, 0);
                    }

                    layout.Controls.Add(panel, 1, 5);
                }
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Network settings
            {
                var tab = new TabPage("Network");
                var layout = new TableLayoutPanel { AutoSize = true };

                var networkOptions = (Dictionary<string, object>)servicePanel.service.Network;

                #region Max retries
                {
                    layout.Controls.Add(new Label { Text = "Max retries", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of time a request should be retried before considered as failed", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var maxRetries = new NumericUpDown { Maximum = int.MaxValue, Value = (int)networkOptions["max_retries"], Dock = DockStyle.Fill };
                    tooltip.SetToolTip(maxRetries, "Retry 5 times by default.");
                    maxRetries.ValueChanged += MaxRetries_ValueChanged;
                    layout.Controls.Add(maxRetries, 1, 1);
                }
                #endregion

                #region Timeout

                #region Connect timeout
                {
                    layout.Controls.Add(new Label { Text = "Connect timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when trying to reach the service", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var connectTimeout = new NumericUpDown { Maximum = int.MaxValue, Value = Convert.ToDecimal(networkOptions["connect_timeout"]), Dock = DockStyle.Fill };
                    tooltip.SetToolTip(connectTimeout, "Wait for 1 second by default.");
                    connectTimeout.ValueChanged += ConnectTimeout_ValueChanged;
                    layout.Controls.Add(connectTimeout, 1, 2);
                }
                #endregion

                #region Read timeout
                {
                    layout.Controls.Add(new Label { Text = "Read timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 3);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when requesting the service", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var readTimeout = new NumericUpDown { Maximum = int.MaxValue, Value = Convert.ToDecimal(networkOptions["read_timeout"]), Dock = DockStyle.Fill };
                    tooltip.SetToolTip(readTimeout, "Wait for 5 seconds by default.");
                    readTimeout.ValueChanged += ReadTimeout_ValueChanged;
                    layout.Controls.Add(readTimeout, 1, 3);
                }
                #endregion

                #endregion

                var proxiesOptions = (Dictionary<string, object>)networkOptions["proxies"];

                #region HTTP proxy
                {
                    layout.Controls.Add(new Label { Text = "HTTP proxy URL", TextAlign = ContentAlignment.BottomLeft }, 0, 4);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Proxy to be used for HTTP requests", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    httpProxy = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = proxiesOptions.ContainsKey("http") ? (string)proxiesOptions["http"] : string.Empty };
                    tooltip.SetToolTip(httpProxy, "Default system HTTP_PROXY will be used if not set.");
                    httpProxy.TextChanged += HttpProxy_TextChanged;
                    layout.Controls.Add(httpProxy, 1, 4);
                }
                #endregion

                #region HTTPS proxy
                {
                    layout.Controls.Add(new Label { Text = "HTTPS proxy URL", TextAlign = ContentAlignment.BottomLeft }, 0, 5);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Proxy to be used for HTTPS requests", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    httpsProxy = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = proxiesOptions.ContainsKey("https") ? (string)proxiesOptions["https"] : string.Empty };
                    tooltip.SetToolTip(httpsProxy, "Default system HTTPS_PROXY will be used if not set.");
                    httpsProxy.TextChanged += HttpsProxy_TextChanged;
                    layout.Controls.Add(httpsProxy, 1, 5);
                }
                #endregion

                #region No proxy
                {
                    layout.Controls.Add(new Label { Text = "No proxy URL", TextAlign = ContentAlignment.BottomLeft }, 0, 6);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "URL starting with this will not use any proxy", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    noProxy = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = proxiesOptions.ContainsKey("no_proxy") ? (string)proxiesOptions["no_proxy"] : string.Empty };
                    tooltip.SetToolTip(noProxy, "Default system NO_PROXY will be used if not set.");
                    noProxy.TextChanged += NoProxy_TextChanged;
                    layout.Controls.Add(noProxy, 1, 6);
                }
                #endregion

                #region SSL certificate verification
                {
                    layout.Controls.Add(new Label { Text = "Verify SSL certificate", TextAlign = ContentAlignment.BottomLeft }, 0, 7);

                    var panel = new TableLayoutPanel { Height = 30, Dock = DockStyle.Fill };


                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Enable SSL certificate verification", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var verifyChecked = networkOptions.ContainsKey("verify") ? Convert.ToBoolean(networkOptions["verify"]) : true;
                        var verifySSLCertificate = new CheckBox { Text = "Verify SSL certificate for https requests", Checked = verifyChecked };
                        tooltip.SetToolTip(verifySSLCertificate, "Uncheck to disable SSL certificate validation.");
                        verifySSLCertificate.CheckedChanged += VerifySSLCertificate_CheckedChanged;
                        panel.Controls.Add(verifySSLCertificate, 0, 0);
                    }

                    layout.Controls.Add(panel, 1, 7);
                }
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

                {
                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of the header field", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    headerName = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                    tooltip.SetToolTip(headerName, "Sent in every request on this service.");
                    headerName.TextChanged += HeaderName_TextChanged;
                    headerName.KeyDown += HeaderName_KeyDown;
                    layout.Controls.Add(headerName, 0, 3);
                }
                {
                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Value of the header field", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    headerValue = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                    tooltip.SetToolTip(headerValue, "Sent in every request on this service.");
                    headerValue.TextChanged += HeaderValue_TextChanged;
                    headerValue.KeyDown += HeaderValue_KeyDown;
                    layout.Controls.Add(headerValue, 1, 3);
                }
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

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Root URL of the server", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var serviceHost = new TextBox { Text = servicePanel.service.OpenAPI.ContainsKey("service_host") ? servicePanel.service.OpenAPI["service_host"].ToString() : string.Empty, Width = 400 };
                        tooltip.SetToolTip(serviceHost, "Usefull when service is behind a reverse proxy.");
                        serviceHost.TextChanged += ServiceHost_TextChanged;
                        hostPanel.Controls.Add(serviceHost, 1, 1);

                        layout.Controls.Add(hostPanel);
                    }
                    #endregion

                    {
                        var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Width = 530, Height = 30 };

                        #region OpenAPI Definition read timeout
                        {
                            panel.Controls.Add(new Label { Text = "Definition read timeout", TextAlign = ContentAlignment.BottomLeft, Width = 130 }, 0, 1);

                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when requesting an OpenAPI definition", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var openAPIDefinitionReadTimeout = new NumericUpDown { Maximum = int.MaxValue, Value = servicePanel.service.OpenAPI.ContainsKey("definition_read_timeout") ? decimal.Parse(servicePanel.service.OpenAPI["definition_read_timeout"].ToString()) : 5, Width = 200 };
                            tooltip.SetToolTip(openAPIDefinitionReadTimeout, "Wait for 5 seconds by default.");
                            openAPIDefinitionReadTimeout.ValueChanged += OpenAPIDefinitionReadTimeout_ValueChanged;
                            panel.Controls.Add(openAPIDefinitionReadTimeout, 1, 1);
                        }
                        #endregion

                        #region Rely on definitions
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Rely on OpenAPI definitions to re-order fields received in response", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var relyOnDefinitions = new CheckBox { Text = "Rely on definitions", Checked = servicePanel.service.OpenAPI.ContainsKey("rely_on_definitions") ? bool.Parse(servicePanel.service.OpenAPI["rely_on_definitions"].ToString()) : false, Width = 200 };
                            tooltip.SetToolTip(relyOnDefinitions, "Deactivated by default as it impact performances.");
                            relyOnDefinitions.CheckedChanged += RelyOnDefinitions_CheckedChanged;
                            panel.Controls.Add(relyOnDefinitions, 2, 1);
                        }
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

                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of an OpenAPI tag to filter on", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            tagName = new TextBox { Text = string.Empty, Width = 530 };
                            tooltip.SetToolTip(tagName, "You will be able to filter in/out this tag.");
                            tagName.TextChanged += TagName_TextChanged;
                            tagName.KeyDown += TagName_KeyDown;
                            addPanel.Controls.Add(tagName, 0, 1);
                        }

                        addTag = new AddButton();
                        addTag.Click += AddTag_Click;
                        addPanel.Controls.Add(addTag, 1, 1);

                        layout.Controls.Add(addPanel);
                    }

                    #endregion

                    #region Operation IDs
                    {
                        var operationIdsLabel = new Label { Dock = DockStyle.Fill, Width = 580, Text = "Operation IDs" };
                        layout.Controls.Add(operationIdsLabel);

                        operationIDsPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                        layout.Controls.Add(operationIDsPanel);

                        {
                            var addPanel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 30 };

                            {
                                ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of an OpenAPI operationID to filter on", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                operationIDName = new TextBox { Text = string.Empty, Width = 530 };
                                tooltip.SetToolTip(operationIDName, "You will be able to filter in/out this operation ID.");
                                operationIDName.TextChanged += OperationIDName_TextChanged;
                                operationIDName.KeyDown += OperationIDName_KeyDown;
                                addPanel.Controls.Add(operationIDName, 0, 1);
                            }

                            addOperationID = new AddButton();
                            addOperationID.Click += AddOperationID_Click;
                            addPanel.Controls.Add(addOperationID, 1, 1);

                            layout.Controls.Add(addPanel);
                        }
                    }
                    #endregion

                    #region Parameters
                    {
                        var parametersLabel = new Label { Dock = DockStyle.Fill, Width = 580, Text = "Parameters" };
                        layout.Controls.Add(parametersLabel);

                        parametersPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                        layout.Controls.Add(parametersPanel);

                        {
                            var addPanel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 30 };

                            {
                                ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of an OpenAPI parameter to filter on", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                parameterName = new TextBox { Text = string.Empty, Width = 530 };
                                tooltip.SetToolTip(parameterName, "You will be able to filter in/out this parameter.");
                                parameterName.TextChanged += ParameterName_TextChanged;
                                parameterName.KeyDown += ParameterName_KeyDown;
                                addPanel.Controls.Add(parameterName, 0, 1);
                            }

                            addParameter = new AddButton();
                            addParameter.Click += AddParameter_Click;
                            addPanel.Controls.Add(addParameter, 1, 1);

                            layout.Controls.Add(addPanel);
                        }
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
                var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];

                #region Timeout
                {
                    layout.Controls.Add(new Label { Width = 150, Text = "Timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait for the authentication response to be received", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var timeout = new NumericUpDown { Dock = DockStyle.Fill, Maximum = int.MaxValue, Value = Convert.ToDecimal(oauth2Options["timeout"]) };
                    tooltip.SetToolTip(timeout, "Wait for 1 minute (60 seconds) by default.");
                    timeout.TextChanged += Oauth2Timeout_TextChanged;
                    layout.Controls.Add(timeout, 1, 2);
                }
                #endregion
                
                #region Header name
                {
                    layout.Controls.Add(new Label { Width = 150, Text = "Header name", TextAlign = ContentAlignment.BottomLeft }, 0, 5);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of the header field used to send token.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var headerName = new TextBox { Dock = DockStyle.Fill, Text = (string)oauth2Options["header_name"] };
                    tooltip.SetToolTip(headerName, "Token will be sent in Authorization header field by default.");
                    headerName.TextChanged += Oauth2HeaderName_TextChanged;
                    layout.Controls.Add(headerName, 1, 5);
                }
                #endregion

                #region Header value
                {
                    layout.Controls.Add(new Label { Width = 150, Text = "Header value", TextAlign = ContentAlignment.BottomLeft }, 0, 6);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Format used to send the token value. '{token}' must be present as it will be replaced by the actual token.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var headerValue = new TextBox { Dock = DockStyle.Fill, Text = (string)oauth2Options["header_value"] };
                    tooltip.SetToolTip(headerValue, "Token will be sent as 'Bearer {token}' by default.");
                    headerValue.TextChanged += Oauth2HeaderValue_TextChanged;
                    layout.Controls.Add(headerValue, 1, 6);
                }
                #endregion

                #region Add items

                oauth2ParamsPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                layout.Controls.Add(oauth2ParamsPanel, 0, 7);
                layout.SetColumnSpan(oauth2ParamsPanel, 3);

                {
                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of parameter to be sent when requesting the authorization.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    oauth2ParamName = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                    tooltip.SetToolTip(oauth2ParamName, "Parameter will be sent in query.");
                    oauth2ParamName.TextChanged += Oauth2ParamName_TextChanged;
                    oauth2ParamName.KeyDown += Oauth2ParamName_KeyDown;
                    layout.Controls.Add(oauth2ParamName, 0, 8);
                }
                {
                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Value of parameter to be sent when requesting the authorization.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    oauth2ParamValue = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                    tooltip.SetToolTip(oauth2ParamValue, "Parameter will be sent in query.");
                    oauth2ParamValue.TextChanged += Oauth2ParamValue_TextChanged;
                    oauth2ParamValue.KeyDown += Oauth2ParamValue_KeyDown;
                    layout.Controls.Add(oauth2ParamValue, 1, 8);
                }
                addOAuth2Param = new AddButton();
                addOAuth2Param.Click += AddOAuth2Param_Click;
                layout.Controls.Add(addOAuth2Param, 2, 8);

                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Basic Authentication settings
            {
                var tab = new TabPage("Basic");
                var layout = new TableLayoutPanel { AutoSize = true };
                var basicOptions = (IDictionary<string, object>)servicePanel.service.Auth["basic"];

                #region Username
                {
                    layout.Controls.Add(new Label { Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "User name.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var userName = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = (string)basicOptions["username"] };
                    tooltip.SetToolTip(userName, "Used only if basic authentication is required.");
                    userName.TextChanged += BasicUsername_TextChanged;
                    layout.Controls.Add(userName, 1, 1);
                }
                #endregion

                #region Password
                {
                    layout.Controls.Add(new Label { Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "User password to be used if needed.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var password = new TextBox { UseSystemPasswordChar = true, Width = 450, Dock = DockStyle.Fill, Text = (string)basicOptions["password"] };
                    tooltip.SetToolTip(password, "Used only if basic authentication is required.");
                    password.TextChanged += BasicPassword_TextChanged;
                    layout.Controls.Add(password, 1, 2);
                }
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region NTLM Authentication settings
            {
                var tab = new TabPage("NTLM");
                var layout = new TableLayoutPanel { AutoSize = true };
                var ntlmOptions = (IDictionary<string, object>)servicePanel.service.Auth["ntlm"];

                #region Username
                {
                    layout.Controls.Add(new Label { Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "User name (including domain if needed).", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var userName = new TextBox { Width = 450, Dock = DockStyle.Fill, Text = (string)ntlmOptions["username"] };
                    tooltip.SetToolTip(userName, "To be set if service requires NTLM authentication.");
                    userName.TextChanged += NtlmUsername_TextChanged;
                    layout.Controls.Add(userName, 1, 1);
                }
                #endregion

                #region Password
                {
                    layout.Controls.Add(new Label { Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "User password (including domain if needed).", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var password = new TextBox { UseSystemPasswordChar = true, Width = 450, Dock = DockStyle.Fill, Text = (string)ntlmOptions["password"] };
                    tooltip.SetToolTip(password, "To be set if service requires NTLM authentication.");
                    password.TextChanged += NtlmPassword_TextChanged;
                    layout.Controls.Add(password, 1, 2);
                }
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Python modules settings
            {
                var tab = new TabPage("Extra modules");
                var layout = new TableLayoutPanel { AutoSize = true };

                var pythonModulesLabel = new Label { Dock = DockStyle.Fill, Width = 580, Text = "Extra python modules" };
                layout.Controls.Add(pythonModulesLabel);

                pythonModulesPanel = new TableLayoutPanel { Dock = DockStyle.Fill, AutoSize = true };
                layout.Controls.Add(pythonModulesPanel);

                {
                    var addPanel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 30 };

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of an extra python module", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        pythonModuleName = new TextBox { Text = string.Empty, Width = 530 };
                        tooltip.SetToolTip(pythonModuleName, "Module will be installed at UDF loading.");
                        pythonModuleName.TextChanged += PythonModuleName_TextChanged;
                        pythonModuleName.KeyDown += PythonModuleName_KeyDown;
                        addPanel.Controls.Add(pythonModuleName, 0, 1);
                    }

                    addPythonModule = new AddButton();
                    addPythonModule.Click += AddPythonModule_Click;
                    addPanel.Controls.Add(addPythonModule, 1, 1);

                    layout.Controls.Add(addPanel);
                }


                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            #region Caching settings
            {
                var tab = new TabPage("Caching");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Result caching time
                {
                    layout.Controls.Add(new Label { Text = "Result caching time", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Number of seconds during which a GET request will return previous result.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var resultCachingTime = new NumericUpDown { Maximum = int.MaxValue, Width = 450, Dock = DockStyle.Fill, Value = servicePanel.service.Caching.ContainsKey("result_caching_time") ? int.Parse(servicePanel.service.Caching["result_caching_time"].ToString()) : 0 };
                    tooltip.SetToolTip(resultCachingTime, "Always send a new request by default.");
                    resultCachingTime.TextChanged += CachingResultTime_TextChanged;
                    layout.Controls.Add(resultCachingTime, 1, 1);
                }
                #endregion

                #region Maximum number of results
                {
                    layout.Controls.Add(new Label { Text = "Maximum number of results", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                    ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of results to store in cache.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                    var maxNbresults = new NumericUpDown { Maximum = int.MaxValue, Width = 450, Dock = DockStyle.Fill, Value = servicePanel.service.Caching.ContainsKey("max_nb_results") ? int.Parse(servicePanel.service.Caching["max_nb_results"].ToString()) : 100 };
                    tooltip.SetToolTip(maxNbresults, "100 by default.");
                    maxNbresults.TextChanged += CachingMaxNumber_TextChanged;
                    layout.Controls.Add(maxNbresults, 1, 2);
                }
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
            var ntlmOptions = (IDictionary<string, object>)servicePanel.service.Auth["ntlm"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                ntlmOptions.Remove("password");
            else
                ntlmOptions["password"] = ((TextBox)sender).Text;
        }

        private void NtlmUsername_TextChanged(object sender, EventArgs e)
        {
            var ntlmOptions = (IDictionary<string, object>)servicePanel.service.Auth["ntlm"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                ntlmOptions.Remove("username");
            else
                ntlmOptions["username"] = ((TextBox)sender).Text;
        }

        private void CachingResultTime_TextChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Value == 0)
            {
                servicePanel.service.Caching.Remove("result_caching_time");
                servicePanel.service.PythonModules.Remove("cachetools==3.0.0");
            }
            else
            {
                servicePanel.service.Caching["result_caching_time"] = ((NumericUpDown)sender).Value;
                if (!servicePanel.service.PythonModules.Contains("cachetools==3.0.0"))
                    servicePanel.service.PythonModules.Add("cachetools==3.0.0");
            }
        }

        private void CachingMaxNumber_TextChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Value == 0)
                servicePanel.service.Caching.Remove("max_nb_results");
            else
                servicePanel.service.Caching["max_nb_results"] = ((NumericUpDown)sender).Value;
        }

        private void BasicPassword_TextChanged(object sender, EventArgs e)
        {
            var basicOptions = (IDictionary<string, object>)servicePanel.service.Auth["basic"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                basicOptions.Remove("password");
            else
                basicOptions["password"] = ((TextBox)sender).Text;
        }

        private void BasicUsername_TextChanged(object sender, EventArgs e)
        {
            var basicOptions = (IDictionary<string, object>)servicePanel.service.Auth["basic"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                basicOptions.Remove("username");
            else
                basicOptions["username"] = ((TextBox)sender).Text;
        }

        private void Oauth2HeaderValue_TextChanged(object sender, EventArgs e)
        {
            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                oauth2Options.Remove("header_value");
            else
                oauth2Options["header_value"] = ((TextBox)sender).Text;
        }

        private void Oauth2HeaderName_TextChanged(object sender, EventArgs e)
        {
            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                oauth2Options.Remove("header_name");
            else
                oauth2Options["header_name"] = ((TextBox)sender).Text;
        }

        private void Oauth2Timeout_TextChanged(object sender, EventArgs e)
        {
            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            if (((NumericUpDown)sender).Value == 0)
                oauth2Options.Remove("timeout");
            else
                oauth2Options["timeout"] = ((NumericUpDown)sender).Value;
        }

        private void NoProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.openAPIDefinitionTicks = DateTime.UtcNow.Ticks;
            var proxiesOptions = (Dictionary<string, object>)servicePanel.service.Network["proxies"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                proxiesOptions.Remove("no_proxy");
            else
                proxiesOptions["no_proxy"] = ((TextBox)sender).Text;
        }

        private void HttpsProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.openAPIDefinitionTicks = DateTime.UtcNow.Ticks;
            var proxiesOptions = (Dictionary<string, object>)servicePanel.service.Network["proxies"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                proxiesOptions.Remove("https");
            else
                proxiesOptions["https"] = ((TextBox)sender).Text;
        }

        private void HttpProxy_TextChanged(object sender, EventArgs e)
        {
            servicePanel.openAPIDefinitionTicks = DateTime.UtcNow.Ticks;
            var proxiesOptions = (Dictionary<string, object>)servicePanel.service.Network["proxies"];
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                proxiesOptions.Remove("http");
            else
                proxiesOptions["http"] = ((TextBox)sender).Text;
        }

        private void OpenAPIDefinitionReadTimeout_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.OpenAPI["definition_read_timeout"] = ((NumericUpDown)sender).Value;
        }

        private void ReadTimeout_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.Network["read_timeout"] = ((NumericUpDown)sender).Value;
        }

        private void ConnectTimeout_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.Network["connect_timeout"] = ((NumericUpDown)sender).Value;
        }

        private void MaxRetries_ValueChanged(object sender, EventArgs e)
        {
            servicePanel.service.Network["max_retries"] = (int)((NumericUpDown)sender).Value;
        }

        private void VerifySSLCertificate_CheckedChanged(object sender, EventArgs e)
        {
            servicePanel.service.Network["verify"] = ((CheckBox)sender).Checked;
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
            servicePanel.service.Auth["api_key"] = ((TextBox)sender).Text;
        }

        private void LegacyArrayFormulas_CheckedChanged(object sender, EventArgs e)
        {
            bool legacyArrayFormulasChecked = ((CheckBox)sender).Checked;
            if (legacyArrayFormulasChecked)
            {
                servicePanel.service.Formulas["legacy_array"] = new Dictionary<string, object>();
                LegacyArrayFormulasLockExcel_CheckedChanged();
            }
            else
            {
                servicePanel.service.Formulas.Remove("legacy_array");
            }

            legacyArrayFormulasLockExcel.Enabled = legacyArrayFormulasChecked;
        }

        private void LegacyArrayFormulasLockExcel_CheckedChanged(object sender, EventArgs e)
        {
            LegacyArrayFormulasLockExcel_CheckedChanged();
        }

        private void LegacyArrayFormulasLockExcel_CheckedChanged()
        {
            AddValueToFormulasSubSection("legacy_array", "lock_excel", legacyArrayFormulasLockExcel.Checked);
        }

        private void DynamicArrayFormulas_CheckedChanged(object sender, EventArgs e)
        {
            bool dynamicArrayFormulasChecked = ((CheckBox)sender).Checked;
            if (dynamicArrayFormulasChecked)
            {
                servicePanel.service.Formulas["dynamic_array"] = new Dictionary<string, object>();
                DynamicArrayFormulasLockExcel_CheckedChanged();
            }
            else
            {
                servicePanel.service.Formulas.Remove("dynamic_array");
            }

            dynamicArrayFormulasLockExcel.Enabled = dynamicArrayFormulasChecked;
        }

        private void DynamicArrayFormulasLockExcel_CheckedChanged(object sender, EventArgs e)
        {
            DynamicArrayFormulasLockExcel_CheckedChanged();
        }

        private void DynamicArrayFormulasLockExcel_CheckedChanged()
        {
            AddValueToFormulasSubSection("dynamic_array", "lock_excel", dynamicArrayFormulasLockExcel.Checked);
        }

        private void VBACompatibleFormulas_CheckedChanged(object sender, EventArgs e)
        {
            bool vbaCompatibleFormulasChecked = ((CheckBox)sender).Checked;
            if (vbaCompatibleFormulasChecked)
            {
                servicePanel.service.Formulas["vba_compatible"] = new Dictionary<string, object>();
                AddValueToFormulasSubSection("vba_compatible", "lock_excel", true);
            }
            else
            {
                servicePanel.service.Formulas.Remove("vba_compatible");
            }
        }

        private void AddValueToFormulasSubSection(string formulaType, string key, object value)
        {
            ((IDictionary<string, object>)servicePanel.service.Formulas[formulaType])[key] = value;
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
            tagName.Text = string.Empty;
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

        #region Python Modules

        private void PythonModuleName_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addPythonModule.Enabled)
                        AddPythonModule();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void PythonModuleName_TextChanged(object sender, EventArgs e)
        {
            var pythonModuleValue = ((TextBox)sender).Text;
            addPythonModule.Enabled = pythonModuleValue.Length > 0 && !servicePanel.service.PythonModules.Contains(pythonModuleValue);
        }

        private void AddPythonModule_Click(object sender, EventArgs e)
        {
            AddPythonModule();
        }

        private void AddPythonModule()
        {
            // Service update
            servicePanel.service.PythonModules.Add(pythonModuleName.Text);
            // Visual update
            AddPythonModule(pythonModuleName.Text);
            pythonModuleName.Text = "";
        }

        private void AddPythonModule(string value)
        {
            var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 25 };

            panel.Controls.Add(new Label { Name = "pythonModuleLabel", Text = value, Width = 515, Dock = DockStyle.Fill }, 0, 1);

            var remove = new DeleteButton();
            remove.Click += RemovePythonModule_Click;
            panel.Controls.Add(remove, 1, 1);

            pythonModulesPanel.Controls.Add(panel);
            pythonModulesPanel.SetColumnSpan(panel, 2);
        }

        private void RemovePythonModule_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            var pythonModuleLabel = (Label)panel.Controls.Find("pythonModuleLabel", false)[0];

            servicePanel.service.PythonModules.Remove(pythonModuleLabel.Text);

            pythonModulesPanel.Controls.Remove(panel);
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

        #region Parameters

        private void ParameterName_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addParameter.Enabled)
                        AddParameter();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void ParameterName_TextChanged(object sender, EventArgs e)
        {
            var parameterValue = ((TextBox)sender).Text;
            addParameter.Enabled = parameterValue.Length > 0 && !ContainsValue(parameterValue, "selected_parameters") && !ContainsValue(parameterValue, "excluded_parameters");
        }

        private void AddParameter_Click(object sender, EventArgs e)
        {
            AddParameter();
        }

        private void AddParameter()
        {
            // Service update
            AddValueToList(parameterName.Text, "selected_parameters");
            // Visual update
            AddParameter(parameterName.Text, false);
            parameterName.Text = "";
        }

        private void AddParameter(string value, bool excluded)
        {
            var panel = new TableLayoutPanel { Dock = DockStyle.Fill, Height = 25 };

            panel.Controls.Add(new Label { Name = "parameterLabel", Text = value, Width = 335, Dock = DockStyle.Fill }, 0, 1);

            panel.Controls.Add(new RadioButton { Text = "excluded", Width = 90, Checked = excluded }, 1, 1);

            var parameterSelected = new RadioButton { Name = "parameterSelected", Text = "selected", Width = 90, Checked = !excluded };
            parameterSelected.CheckedChanged += ParameterSelected_CheckedChanged;
            panel.Controls.Add(parameterSelected, 2, 1);

            var remove = new DeleteButton();
            remove.Click += RemoveParameter_Click;
            panel.Controls.Add(remove, 3, 1);

            parametersPanel.Controls.Add(panel);
            parametersPanel.SetColumnSpan(panel, 2);
        }

        private void ParameterSelected_CheckedChanged(object sender, EventArgs e)
        {
            var parameterSelected = (RadioButton)sender;
            Label parameterLabel = (Label)parameterSelected.Parent.Controls.Find("parameterLabel", false)[0];

            if (parameterSelected.Checked) // Moved from excluded to selected
                MoveFromListToList(parameterLabel.Text, "excluded_parameters", "selected_parameters");
            else // Move from selected to excluded
                MoveFromListToList(parameterLabel.Text, "selected_parameters", "excluded_parameters");
        }

        private void RemoveParameter_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            var parameterLabel = (Label)panel.Controls.Find("parameterLabel", false)[0];
            var parameterSelected = (RadioButton)panel.Controls.Find("parameterSelected", false)[0];

            RemoveValueFromList(parameterLabel.Text, parameterSelected.Checked ? "selected_parameters" : "excluded_parameters");

            parametersPanel.Controls.Remove(panel);
        }

        #endregion

        #region Header

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

            headerName.Text = string.Empty;
            headerValue.Text = string.Empty;
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

        #endregion

        #region OAuth2

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
            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            addOAuth2Param.Enabled = ((TextBox)sender).Text.Length > 0 && oauth2ParamValue.Text.Length > 0 && !oauth2Options.ContainsKey(((TextBox)sender).Text);
        }

        private void AddOAuth2Param_Click(object sender, EventArgs e)
        {
            AddOAuth2Param();
        }

        private void AddOAuth2Param()
        {
            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            oauth2Options.Add(oauth2ParamName.Text, oauth2ParamValue.Text);

            AddOAuth2Param(oauth2ParamName.Text, oauth2ParamValue.Text);

            oauth2ParamName.Text = string.Empty;
            oauth2ParamValue.Text = string.Empty;
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

            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            oauth2Options[oauth2ParamNameLabel.Text] = valueTextBox.Text;
        }

        private void RemoveOAuth2Param_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            Label oauth2ParamNameLabel = (Label)panel.Controls.Find("oauth2ParamNameLabel", false)[0];

            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            oauth2Options.Remove(oauth2ParamNameLabel.Text);

            oauth2ParamsPanel.Controls.Remove(panel);
        }

        #endregion

        #endregion
    }
}
