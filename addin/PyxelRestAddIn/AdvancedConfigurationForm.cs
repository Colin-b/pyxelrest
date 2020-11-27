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
        private NumericUpDown maxNbresults;

        public AdvancedConfigurationForm(ServicePanel servicePanel)
        {
            this.servicePanel = servicePanel;
            InitializeComponent();

            foreach (var header in (IDictionary<string, object>)servicePanel.service.Network["headers"])
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
            Screen screen = Screen.FromControl(this);
            Rectangle screenSize = screen.WorkingArea;

            Size = new Size(screenSize.Width / 2, screenSize.Height / 2);
            MaximumSize = Size;
            StartPosition = FormStartPosition.CenterParent;

            var tabs = new TabControl { Dock = DockStyle.Fill };

            #region Formulas settings
            {
                var tab = new TabPage("Formulas");
                var layout = new TableLayoutPanel { AutoSize = true };

                #region Dynamic array formulas
                {
                    var panel = new TableLayoutPanel { AutoSize = true };
                    Dictionary<string, object> dynamicArrayFormulasOptions = servicePanel.service.Formulas.ContainsKey("dynamic_array") ? (Dictionary<string, object>)servicePanel.service.Formulas["dynamic_array"] : new Dictionary<string, object>();

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate dynamic array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var dynamicArrayFormulas = new CheckBox { Text = "Dynamic array", Checked = dynamicArrayFormulasOptions.Count > 0, Width = PercentWidth(20) };
                        tooltip.SetToolTip(dynamicArrayFormulas, "If your version of Microsoft Excel supports dynamic array formulas, results will be spilled.\nOtherwise results will only fill selected cells.");
                        dynamicArrayFormulas.CheckedChanged += DynamicArrayFormulas_CheckedChanged;
                        panel.Controls.Add(dynamicArrayFormulas, 0, 0);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Lock Microsoft Excel while waiting for results", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var synchronousChecked = dynamicArrayFormulasOptions.ContainsKey("lock_excel") ? (bool)dynamicArrayFormulasOptions["lock_excel"] : false;
                        dynamicArrayFormulasLockExcel = new CheckBox { Text = "Wait for dynamic array result", Checked = synchronousChecked, Width = PercentWidth(50) };
                        tooltip.SetToolTip(dynamicArrayFormulasLockExcel, "Uncheck to still be able to use Microsoft Excel while waiting for results.");
                        dynamicArrayFormulasLockExcel.CheckedChanged += DynamicArrayFormulasLockExcel_CheckedChanged;
                        dynamicArrayFormulasLockExcel.Enabled = dynamicArrayFormulasOptions.Count > 0;
                        panel.Controls.Add(dynamicArrayFormulasLockExcel, 1, 0);
                    }

                    layout.Controls.Add(panel);
                }
                #endregion

                #region Legacy array formulas
                {
                    var panel = new TableLayoutPanel { AutoSize = true };
                    Dictionary<string, object> legacyArrayFormulasOptions = servicePanel.service.Formulas.ContainsKey("legacy_array") ? (Dictionary<string, object>)servicePanel.service.Formulas["legacy_array"] : new Dictionary<string, object>();

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate legacy array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var legacyArrayFormulas = new CheckBox { Text = "Legacy array", Checked = legacyArrayFormulasOptions.Count > 0, Width = PercentWidth(20) };
                        tooltip.SetToolTip(legacyArrayFormulas, "If your version of Microsoft Excel does not supports dynamic array formulas, use this to spill results.");
                        legacyArrayFormulas.CheckedChanged += LegacyArrayFormulas_CheckedChanged;
                        panel.Controls.Add(legacyArrayFormulas, 0, 0);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Lock Microsoft Excel while waiting for results", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var synchronousChecked = legacyArrayFormulasOptions.ContainsKey("lock_excel") ? (bool)legacyArrayFormulasOptions["lock_excel"] : false;
                        legacyArrayFormulasLockExcel = new CheckBox { Text = "Wait for legacy array result", Checked = synchronousChecked, Width = PercentWidth(50) };
                        tooltip.SetToolTip(legacyArrayFormulasLockExcel, "Uncheck to still be able to use Microsoft Excel while waiting for results.");
                        legacyArrayFormulasLockExcel.CheckedChanged += LegacyArrayFormulasLockExcel_CheckedChanged;
                        legacyArrayFormulasLockExcel.Enabled = legacyArrayFormulasOptions.Count > 0;
                        panel.Controls.Add(legacyArrayFormulasLockExcel, 1, 0);
                    }

                    layout.Controls.Add(panel);
                }
                #endregion

                #region Visual Basic compatible formulas
                {
                    var panel = new TableLayoutPanel { AutoSize = true };
                    Dictionary<string, object> vbaCompatibleFormulasOptions = servicePanel.service.Formulas.ContainsKey("vba_compatible") ? (Dictionary<string, object>)servicePanel.service.Formulas["vba_compatible"] : new Dictionary<string, object>();

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate VBA compatible formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var vbaCompatibleFormulas = new CheckBox { Text = "Visual basic", Checked = vbaCompatibleFormulasOptions.Count > 0, Width = PercentWidth(20) };
                        tooltip.SetToolTip(vbaCompatibleFormulas, "Use this formula behavior if you want to call it using Visual Basic for Applications (VBA).");
                        vbaCompatibleFormulas.CheckedChanged += VBACompatibleFormulas_CheckedChanged;
                        panel.Controls.Add(vbaCompatibleFormulas, 0, 0);
                    }

                    layout.Controls.Add(panel);
                }
                #endregion

                #region Caching settings
                {
                    var panel = new TableLayoutPanel { AutoSize = true };

                    #region Result caching time
                    {
                        panel.Controls.Add(new Label { Width = PercentWidth(20), Text = "Result caching time", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Number of seconds during which a GET request will return previous result.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var resultCachingTime = new NumericUpDown { Maximum = int.MaxValue, Width = PercentWidth(10), Value = int.Parse(servicePanel.service.Caching["result_caching_time"].ToString()) };
                        tooltip.SetToolTip(resultCachingTime, "Always send a new request by default (0 seconds means that caching is disabled).");
                        resultCachingTime.TextChanged += CachingResultTime_TextChanged;
                        panel.Controls.Add(resultCachingTime, 1, 1);
                    }
                    #endregion

                    #region Maximum number of results
                    {
                        panel.Controls.Add(new Label { Width = PercentWidth(20), Text = "Maximum number of results", TextAlign = ContentAlignment.BottomLeft }, 2, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of results to store in cache.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        maxNbresults = new NumericUpDown { Maximum = int.MaxValue, Width = PercentWidth(10), Value = int.Parse(servicePanel.service.Caching["max_nb_results"].ToString()) };
                        tooltip.SetToolTip(maxNbresults, "Store the last 100 results by default (if caching is enabled).");
                        maxNbresults.TextChanged += CachingMaxNumber_TextChanged;
                        maxNbresults.Enabled = int.Parse(servicePanel.service.Caching["result_caching_time"].ToString()) > 0;
                        panel.Controls.Add(maxNbresults, 3, 1);
                    }
                    #endregion

                    layout.Controls.Add(panel);
                }
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            if (!"pyxelrest".Equals(servicePanel.service.Name))
            {
                #region OpenAPI settings
                {
                    var tab = new TabPage { Text = "OpenAPI", AutoScroll = true };
                    var layout = new TableLayoutPanel { AutoSize = true };

                    #region Host
                    {
                        var panel = new TableLayoutPanel { AutoSize = true };

                        panel.Controls.Add(new Label { Text = "Host", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(15) }, 0, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Root URL of the server", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var host = new TextBox { Width = PercentWidth(70), Text = servicePanel.service.OpenAPI.ContainsKey("host") ? servicePanel.service.OpenAPI["host"].ToString() : string.Empty };
                        tooltip.SetToolTip(host, "Usefull when host is not provided in the OpenAPI definition and API is behind a reverse proxy.");
                        host.TextChanged += Host_TextChanged;
                        panel.Controls.Add(host, 1, 1);

                        layout.Controls.Add(panel);
                    }
                    #endregion

                    {
                        var panel = new TableLayoutPanel { AutoSize = true };

                        #region OpenAPI Definition read timeout
                        {
                            panel.Controls.Add(new Label { Text = "Definition read timeout", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(25) }, 0, 1);

                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when requesting an OpenAPI definition", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var openAPIDefinitionReadTimeout = new NumericUpDown { Width = PercentWidth(10), Maximum = int.MaxValue, Value = servicePanel.service.OpenAPI.ContainsKey("definition_read_timeout") ? decimal.Parse(servicePanel.service.OpenAPI["definition_read_timeout"].ToString()) : 5 };
                            tooltip.SetToolTip(openAPIDefinitionReadTimeout, "Wait for 5 seconds by default.");
                            openAPIDefinitionReadTimeout.ValueChanged += OpenAPIDefinitionReadTimeout_ValueChanged;
                            panel.Controls.Add(openAPIDefinitionReadTimeout, 1, 1);
                        }
                        #endregion

                        #region Rely on definitions
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Rely on OpenAPI definitions to re-order fields received in response", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var relyOnDefinitions = new CheckBox { Width = PercentWidth(40), Text = "Rely on definitions", Checked = servicePanel.service.OpenAPI.ContainsKey("rely_on_definitions") ? bool.Parse(servicePanel.service.OpenAPI["rely_on_definitions"].ToString()) : false };
                            tooltip.SetToolTip(relyOnDefinitions, "Deactivated by default as it impact performances.");
                            relyOnDefinitions.CheckedChanged += RelyOnDefinitions_CheckedChanged;
                            panel.Controls.Add(relyOnDefinitions, 2, 1);
                        }
                        #endregion

                        layout.Controls.Add(panel);
                    }

                    #region Methods
                    {
                        layout.Controls.Add(new Label { Text = "Methods" });

                        var panel = new TableLayoutPanel { AutoSize = true };
                        List<string> selectedMethods = (List<string>)servicePanel.service.OpenAPI["selected_methods"];

                        var get = new CheckBox { Text = "get", Checked = selectedMethods.Contains("get"), Width = PercentWidth(11) };
                        get.CheckedChanged += Get_CheckedChanged;
                        panel.Controls.Add(get, 0, 0);
                        var post = new CheckBox { Text = "post", Checked = selectedMethods.Contains("post"), Width = PercentWidth(11) };
                        post.CheckedChanged += Post_CheckedChanged;
                        panel.Controls.Add(post, 1, 0);
                        var put = new CheckBox { Text = "put", Checked = selectedMethods.Contains("put"), Width = PercentWidth(11) };
                        put.CheckedChanged += Put_CheckedChanged;
                        panel.Controls.Add(put, 2, 0);
                        var patch = new CheckBox { Text = "patch", Checked = selectedMethods.Contains("patch"), Width = PercentWidth(11) };
                        patch.CheckedChanged += Patch_CheckedChanged;
                        panel.Controls.Add(patch, 3, 0);
                        var delete = new CheckBox { Text = "delete", Checked = selectedMethods.Contains("delete"), Width = PercentWidth(11) };
                        delete.CheckedChanged += Delete_CheckedChanged;
                        panel.Controls.Add(delete, 4, 0);

                        layout.Controls.Add(panel);
                    }
                    #endregion

                    #region Tags
                    {
                        var tagsLabel = new Label { Text = "Tags" };
                        layout.Controls.Add(tagsLabel);

                        tagsPanel = new TableLayoutPanel { AutoSize = true };
                        layout.Controls.Add(tagsPanel);

                        {
                            var addPanel = new TableLayoutPanel { AutoSize = true };

                            {
                                ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of an OpenAPI tag to filter on", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                tagName = new TextBox { Text = string.Empty, Width = PercentWidth(80) };
                                tooltip.SetToolTip(tagName, "You will be able to filter in/out this tag.");
                                tagName.TextChanged += TagName_TextChanged;
                                tagName.KeyDown += TagName_KeyDown;
                                addPanel.Controls.Add(tagName, 0, 1);
                            }

                            addTag = new AddButton(PercentWidth(5));
                            addTag.Click += AddTag_Click;
                            addPanel.Controls.Add(addTag, 1, 1);

                            layout.Controls.Add(addPanel);
                        }
                    }
                    #endregion

                    #region Operation IDs
                    {
                        var operationIdsLabel = new Label { Text = "Operation IDs" };
                        layout.Controls.Add(operationIdsLabel);

                        operationIDsPanel = new TableLayoutPanel { AutoSize = true };
                        layout.Controls.Add(operationIDsPanel);

                        {
                            var addPanel = new TableLayoutPanel { AutoSize = true };

                            {
                                ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of an OpenAPI operationID to filter on", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                operationIDName = new TextBox { Text = string.Empty, Width = PercentWidth(80) };
                                tooltip.SetToolTip(operationIDName, "You will be able to filter in/out this operation ID.");
                                operationIDName.TextChanged += OperationIDName_TextChanged;
                                operationIDName.KeyDown += OperationIDName_KeyDown;
                                addPanel.Controls.Add(operationIDName, 0, 1);
                            }

                            addOperationID = new AddButton(PercentWidth(5));
                            addOperationID.Click += AddOperationID_Click;
                            addPanel.Controls.Add(addOperationID, 1, 1);

                            layout.Controls.Add(addPanel);
                        }
                    }
                    #endregion

                    #region Parameters
                    {
                        var parametersLabel = new Label { Text = "Parameters" };
                        layout.Controls.Add(parametersLabel);

                        parametersPanel = new TableLayoutPanel { AutoSize = true };
                        layout.Controls.Add(parametersPanel);

                        {
                            var addPanel = new TableLayoutPanel { AutoSize = true };

                            {
                                ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of an OpenAPI parameter to filter on", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                parameterName = new TextBox { Text = string.Empty, Width = PercentWidth(80) };
                                tooltip.SetToolTip(parameterName, "You will be able to filter in/out this parameter.");
                                parameterName.TextChanged += ParameterName_TextChanged;
                                parameterName.KeyDown += ParameterName_KeyDown;
                                addPanel.Controls.Add(parameterName, 0, 1);
                            }

                            addParameter = new AddButton(PercentWidth(5));
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

            #region Authentication settings
            {
                var authTab = new TabPage { Text = "Authentication" };
                var authTabs = new TabControl { Dock = DockStyle.Fill };

                #region API Key settings
                {
                    var tab = new TabPage { Text = "API key", AutoScroll = true };
                    var layout = new TableLayoutPanel { AutoSize = true };

                    #region API Key
                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(15), Text = "API key", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "API key", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var apiKey = new TextBox { Width = PercentWidth(75), Text = (string)servicePanel.service.Auth["api_key"] };
                        tooltip.SetToolTip(apiKey, "Only used when required.");
                        apiKey.TextChanged += ApiKey_TextChanged;
                        layout.Controls.Add(apiKey, 1, 1);
                    }
                    #endregion

                    tab.Controls.Add(layout);
                    authTabs.TabPages.Add(tab);
                }
                #endregion

                #region OAuth2 settings
                {
                    var tab = new TabPage { Text = "OAuth2", AutoScroll = true };
                    var layout = new TableLayoutPanel { AutoSize = true };
                    var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];

                    #region Timeout
                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(25), Text = "Timeout", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait for the authentication response to be received", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var timeout = new NumericUpDown { Width = PercentWidth(60), Maximum = int.MaxValue, Value = Convert.ToDecimal(oauth2Options["timeout"]) };
                        tooltip.SetToolTip(timeout, "Wait for 1 minute (60 seconds) by default.");
                        timeout.TextChanged += Oauth2Timeout_TextChanged;
                        layout.Controls.Add(timeout, 1, 2);
                    }
                    #endregion

                    #region Add items

                    oauth2ParamsPanel = new TableLayoutPanel { AutoSize = true };
                    layout.Controls.Add(oauth2ParamsPanel, 0, 7);
                    layout.SetColumnSpan(oauth2ParamsPanel, 3);

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of parameter to be sent when requesting the authorization.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        oauth2ParamName = new TextBox { Width = PercentWidth(25), Text = string.Empty };
                        tooltip.SetToolTip(oauth2ParamName, "Parameter will be sent in query.");
                        oauth2ParamName.TextChanged += Oauth2ParamName_TextChanged;
                        oauth2ParamName.KeyDown += Oauth2ParamName_KeyDown;
                        layout.Controls.Add(oauth2ParamName, 0, 8);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Value of parameter to be sent when requesting the authorization.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        oauth2ParamValue = new TextBox { Width = PercentWidth(60), Text = string.Empty };
                        tooltip.SetToolTip(oauth2ParamValue, "Parameter will be sent in query.");
                        oauth2ParamValue.TextChanged += Oauth2ParamValue_TextChanged;
                        oauth2ParamValue.KeyDown += Oauth2ParamValue_KeyDown;
                        layout.Controls.Add(oauth2ParamValue, 1, 8);
                    }
                    addOAuth2Param = new AddButton(PercentWidth(5));
                    addOAuth2Param.Click += AddOAuth2Param_Click;
                    layout.Controls.Add(addOAuth2Param, 2, 8);

                    #endregion

                    tab.Controls.Add(layout);
                    authTabs.TabPages.Add(tab);
                }
                #endregion

                #region Basic Authentication settings
                {
                    var tab = new TabPage("Basic");
                    var layout = new TableLayoutPanel { AutoSize = true };
                    var basicOptions = (IDictionary<string, object>)servicePanel.service.Auth["basic"];

                    #region Username
                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(15), Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "User name.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var userName = new TextBox { Width = PercentWidth(75), Text = (string)basicOptions["username"] };
                        tooltip.SetToolTip(userName, "Used only if basic authentication is required.");
                        userName.TextChanged += BasicUsername_TextChanged;
                        layout.Controls.Add(userName, 1, 1);
                    }
                    #endregion

                    #region Password
                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(15), Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "User password to be used if needed.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var password = new TextBox { UseSystemPasswordChar = true, Width = PercentWidth(75), Text = (string)basicOptions["password"] };
                        tooltip.SetToolTip(password, "Used only if basic authentication is required.");
                        password.TextChanged += BasicPassword_TextChanged;
                        layout.Controls.Add(password, 1, 2);
                    }
                    #endregion

                    tab.Controls.Add(layout);
                    authTabs.TabPages.Add(tab);
                }
                #endregion

                #region NTLM Authentication settings
                {
                    var tab = new TabPage("NTLM");
                    var layout = new TableLayoutPanel { AutoSize = true };
                    var ntlmOptions = (IDictionary<string, object>)servicePanel.service.Auth["ntlm"];

                    #region Username
                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(15), Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "User name (including domain if needed).", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var userName = new TextBox { Width = PercentWidth(75), Text = (string)ntlmOptions["username"] };
                        tooltip.SetToolTip(userName, "To be set if service requires NTLM authentication.");
                        userName.TextChanged += NtlmUsername_TextChanged;
                        layout.Controls.Add(userName, 1, 1);
                    }
                    #endregion

                    #region Password
                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(15), Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 0, 2);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "User password (including domain if needed).", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var password = new TextBox { UseSystemPasswordChar = true, Width = PercentWidth(75), Text = (string)ntlmOptions["password"] };
                        tooltip.SetToolTip(password, "To be set if service requires NTLM authentication.");
                        password.TextChanged += NtlmPassword_TextChanged;
                        layout.Controls.Add(password, 1, 2);
                    }
                    #endregion

                    tab.Controls.Add(layout);
                    authTabs.TabPages.Add(tab);
                }
                #endregion

                authTab.Controls.Add(authTabs);
                tabs.TabPages.Add(authTab);
            }
            #endregion

            #region Network settings
            {
                var tab = new TabPage { Text = "Network", AutoScroll = true };
                var layout = new TableLayoutPanel { AutoSize = true };

                var networkOptions = (Dictionary<string, object>)servicePanel.service.Network;

                {
                    var panel = new TableLayoutPanel { AutoSize = true };

                    #region Timeout

                    #region Connect timeout
                    {
                        panel.Controls.Add(new Label { Text = "Connect timeout", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(17) }, 0, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when trying to reach the service", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var connectTimeout = new NumericUpDown { Maximum = int.MaxValue, Value = Convert.ToDecimal(networkOptions["connect_timeout"]), Width = PercentWidth(10) };
                        tooltip.SetToolTip(connectTimeout, "Wait for 1 second by default.");
                        connectTimeout.ValueChanged += ConnectTimeout_ValueChanged;
                        panel.Controls.Add(connectTimeout, 1, 1);
                    }
                    #endregion

                    #region Read timeout
                    {
                        panel.Controls.Add(new Label { Text = "Read timeout", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(15) }, 2, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when requesting the service", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var readTimeout = new NumericUpDown { Maximum = int.MaxValue, Value = Convert.ToDecimal(networkOptions["read_timeout"]), Width = PercentWidth(10) };
                        tooltip.SetToolTip(readTimeout, "Wait for 5 seconds by default.");
                        readTimeout.ValueChanged += ReadTimeout_ValueChanged;
                        panel.Controls.Add(readTimeout, 3, 1);
                    }
                    #endregion

                    #endregion

                    #region Max retries
                    {
                        panel.Controls.Add(new Label { Text = "Max retries", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(15) }, 4, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of time a request should be retried before considered as failed", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var maxRetries = new NumericUpDown { Maximum = int.MaxValue, Value = (int)networkOptions["max_retries"], Width = PercentWidth(10) };
                        tooltip.SetToolTip(maxRetries, "Retry 5 times by default.");
                        maxRetries.ValueChanged += MaxRetries_ValueChanged;
                        panel.Controls.Add(maxRetries, 5, 1);
                    }
                    #endregion

                    layout.Controls.Add(panel, 0, 1);
                }

                {
                    var panel = new TableLayoutPanel { AutoSize = true };

                    #region SSL certificate verification
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Enable SSL certificate verification", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var verifyChecked = !networkOptions.ContainsKey("verify") || Convert.ToBoolean(networkOptions["verify"]);
                        var verifySSLCertificate = new CheckBox { Text = "Verify SSL certificate for https requests", Checked = verifyChecked, Width = PercentWidth(60) };
                        tooltip.SetToolTip(verifySSLCertificate, "Uncheck to disable SSL certificate validation.");
                        verifySSLCertificate.CheckedChanged += VerifySSLCertificate_CheckedChanged;
                        panel.Controls.Add(verifySSLCertificate, 0, 1);
                    }
                    #endregion

                    layout.Controls.Add(panel, 0, 2);
                }

                {
                    var panel = new TableLayoutPanel { AutoSize = true };

                    var proxiesOptions = (Dictionary<string, object>)networkOptions["proxies"];

                    #region HTTP proxy
                    {
                        panel.Controls.Add(new Label { Text = "HTTP proxy", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(15) }, 0, 1);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Proxy URL to be used for HTTP requests", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        httpProxy = new TextBox { Width = PercentWidth(75), Text = proxiesOptions.ContainsKey("http") ? (string)proxiesOptions["http"] : string.Empty };
                        tooltip.SetToolTip(httpProxy, "Default system HTTP_PROXY will be used if not set.");
                        httpProxy.TextChanged += HttpProxy_TextChanged;
                        panel.Controls.Add(httpProxy, 1, 1);
                    }
                    #endregion

                    #region HTTPS proxy
                    {
                        panel.Controls.Add(new Label { Text = "HTTPS proxy", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(15) }, 0, 2);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Proxy URL to be used for HTTPS requests", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        httpsProxy = new TextBox { Width = PercentWidth(75), Text = proxiesOptions.ContainsKey("https") ? (string)proxiesOptions["https"] : string.Empty };
                        tooltip.SetToolTip(httpsProxy, "Default system HTTPS_PROXY will be used if not set.");
                        httpsProxy.TextChanged += HttpsProxy_TextChanged;
                        panel.Controls.Add(httpsProxy, 1, 2);
                    }
                    #endregion

                    #region No proxy
                    {
                        panel.Controls.Add(new Label { Text = "No proxy", TextAlign = ContentAlignment.BottomLeft, Width = PercentWidth(15) }, 0, 3);

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "URL starting with this will not use any proxy", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        noProxy = new TextBox { Width = PercentWidth(75), Text = proxiesOptions.ContainsKey("no_proxy") ? (string)proxiesOptions["no_proxy"] : string.Empty };
                        tooltip.SetToolTip(noProxy, "Default system NO_PROXY will be used if not set.");
                        noProxy.TextChanged += NoProxy_TextChanged;
                        panel.Controls.Add(noProxy, 1, 3);
                    }
                    #endregion

                    layout.Controls.Add(panel, 0, 3);
                }

                {
                    var panel = new TableLayoutPanel { AutoSize = true };

                    #region Headers

                    var nameLabel = new Label { Text = "Header name", Width = PercentWidth(20) };
                    panel.Controls.Add(nameLabel, 0, 1);

                    var valueLabel = new Label { Text = "Header value", Width = PercentWidth(65) };
                    panel.Controls.Add(valueLabel, 1, 1);

                    headersPanel = new TableLayoutPanel { AutoSize = true };
                    panel.Controls.Add(headersPanel, 0, 2);
                    panel.SetColumnSpan(headersPanel, 3);

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of the header field", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        headerName = new TextBox { Text = string.Empty, Width = PercentWidth(20) };
                        tooltip.SetToolTip(headerName, "Sent in every request on this service.");
                        headerName.TextChanged += HeaderName_TextChanged;
                        headerName.KeyDown += HeaderName_KeyDown;
                        panel.Controls.Add(headerName, 0, 3);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Value of the header field", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        headerValue = new TextBox { Text = string.Empty, Width = PercentWidth(65) };
                        tooltip.SetToolTip(headerValue, "Sent in every request on this service.");
                        headerValue.TextChanged += HeaderValue_TextChanged;
                        headerValue.KeyDown += HeaderValue_KeyDown;
                        panel.Controls.Add(headerValue, 1, 3);
                    }
                    addHeader = new AddButton(PercentWidth(5));
                    addHeader.Click += AddHeader_Click;
                    panel.Controls.Add(addHeader, 2, 3);

                    #endregion

                    layout.Controls.Add(panel, 0, 4);
                }

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
            servicePanel.service.Caching["result_caching_time"] = ((NumericUpDown)sender).Value;
            maxNbresults.Enabled = ((NumericUpDown)sender).Value > 0;
        }

        private void CachingMaxNumber_TextChanged(object sender, EventArgs e)
        {
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

        private void Host_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.OpenAPI.Remove("host");
            else
                servicePanel.service.OpenAPI["host"] = ((TextBox)sender).Text;
        }

        private void Patch_CheckedChanged(object sender, EventArgs e)
        {
            SelectedMethodsChanged("patch", ((CheckBox)sender).Checked);
        }

        private void Delete_CheckedChanged(object sender, EventArgs e)
        {
            SelectedMethodsChanged("delete", ((CheckBox)sender).Checked);
        }

        private void Put_CheckedChanged(object sender, EventArgs e)
        {
            SelectedMethodsChanged("put", ((CheckBox)sender).Checked);
        }

        private void Post_CheckedChanged(object sender, EventArgs e)
        {
            SelectedMethodsChanged("post", ((CheckBox)sender).Checked);
        }

        private void Get_CheckedChanged(object sender, EventArgs e)
        {
            SelectedMethodsChanged("get", ((CheckBox)sender).Checked);
        }

        private void SelectedMethodsChanged(string method, bool selected)
        {
            List<string> selectedMethods = (List<string>)servicePanel.service.OpenAPI["selected_methods"];
            if (selected)
            {
                if (!selectedMethods.Contains(method))
                    selectedMethods.Add(method);
            }
            else
            {
                if (selectedMethods.Contains(method))
                    selectedMethods.Remove(method);
            }
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
            var panel = new TableLayoutPanel { AutoSize = true };

            panel.Controls.Add(new Label { Name = "tagLabel", Text = value, Width = PercentWidth(50) }, 0, 1);

            panel.Controls.Add(new RadioButton { Text = "excluded", Width = PercentWidth(15), Checked = excluded }, 1, 1);

            var tagSelected = new RadioButton { Name = "tagSelected", Text = "selected", Width = PercentWidth(15), Checked = !excluded };
            tagSelected.CheckedChanged += TagSelected_CheckedChanged;
            panel.Controls.Add(tagSelected, 2, 1);

            var remove = new DeleteButton(PercentWidth(5));
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
            var panel = new TableLayoutPanel { AutoSize = true };

            panel.Controls.Add(new Label { Name = "operationIDLabel", Text = value, Width = PercentWidth(50) }, 0, 1);

            panel.Controls.Add(new RadioButton { Text = "excluded", Width = PercentWidth(15), Checked = excluded }, 1, 1);

            var operationIDSelected = new RadioButton { Name = "operationIDSelected", Text = "selected", Width = PercentWidth(15), Checked = !excluded };
            operationIDSelected.CheckedChanged += OperationIDSelected_CheckedChanged;
            panel.Controls.Add(operationIDSelected, 2, 1);

            var remove = new DeleteButton(PercentWidth(5));
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
            var panel = new TableLayoutPanel { AutoSize = true };

            panel.Controls.Add(new Label { Name = "parameterLabel", Text = value, Width = PercentWidth(50) }, 0, 1);

            panel.Controls.Add(new RadioButton { Text = "excluded", Width = PercentWidth(15), Checked = excluded }, 1, 1);

            var parameterSelected = new RadioButton { Name = "parameterSelected", Text = "selected", Width = PercentWidth(15), Checked = !excluded };
            parameterSelected.CheckedChanged += ParameterSelected_CheckedChanged;
            panel.Controls.Add(parameterSelected, 2, 1);

            var remove = new DeleteButton(PercentWidth(5));
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
            var headers = (IDictionary<string, object>)servicePanel.service.Network["headers"];
            return headers.ContainsKey(value);
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
            var headers = (IDictionary<string, object>)servicePanel.service.Network["headers"];
            headers.Add(headerName.Text, headerValue.Text);

            AddHeader(headerName.Text, headerValue.Text);

            headerName.Text = string.Empty;
            headerValue.Text = string.Empty;
        }

        private void AddHeader(string name, string value)
        {
            var panel = new TableLayoutPanel { AutoSize = true };

            panel.Controls.Add(new Label { Name = "headerNameLabel", Text = name, Width = PercentWidth(20) }, 0, 1);

            var valueTextBox = new TextBox { Text = value, Width = PercentWidth(65) };
            valueTextBox.TextChanged += ExistingHeaderValue_TextChanged;
            panel.Controls.Add(valueTextBox, 1, 1);

            var remove = new DeleteButton(PercentWidth(5));
            remove.Click += RemoveHeader_Click;
            panel.Controls.Add(remove, 2, 1);

            headersPanel.Controls.Add(panel);
            headersPanel.SetColumnSpan(panel, 3);
        }

        private void ExistingHeaderValue_TextChanged(object sender, EventArgs e)
        {
            var valueTextBox = (TextBox)sender;
            Label headerNameLabel = (Label)valueTextBox.Parent.Controls.Find("headerNameLabel", false)[0];

            var headers = (IDictionary<string, object>)servicePanel.service.Network["headers"];
            headers[headerNameLabel.Text] = valueTextBox.Text;
        }

        private void RemoveHeader_Click(object sender, EventArgs e)
        {
            var panel = ((DeleteButton)sender).Parent;
            Label headerNameLabel = (Label)panel.Controls.Find("headerNameLabel", false)[0];

            var headers = (IDictionary<string, object>)servicePanel.service.Network["headers"];
            headers.Remove(headerNameLabel.Text);

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
            var panel = new TableLayoutPanel { AutoSize = true };

            panel.Controls.Add(new Label { Name = "oauth2ParamNameLabel", Text = name, Width = PercentWidth(25) }, 0, 1);

            var valueTextBox = new TextBox { Text = value, Width = PercentWidth(60) };
            valueTextBox.TextChanged += OAuth2ParamValue_TextChanged;
            panel.Controls.Add(valueTextBox, 1, 1);

            var remove = new DeleteButton(PercentWidth(5));
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
