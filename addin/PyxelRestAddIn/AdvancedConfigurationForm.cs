using System;
using System.Collections.Generic;
using System.Diagnostics;
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

        private GroupBox apiKeyDefinitionAuthGroup;
        private ComboBox apiKeyDefinitionAuthLocation;
        private TextBox apiKeyDefinitionAuthName;

        private TableLayoutPanel oauth2ParamsPanel;
        private TextBox oauth2ParamName;
        private TextBox oauth2ParamValue;
        private AddButton addOAuth2Param;

        private Dictionary<string, string[]> oauth2ToolTips = new Dictionary<string, string[]>
        {
            {"timeout", new string[] { "Maximum number of seconds to wait for the authentication response to be received", "Wait for 1 minute (60 seconds) by default." } },
            {"header_name", new string[] { "Name of the header in which the OAuth2 token will be sent", "Use 'Authorization' header by default." } },
            {"header_value", new string[] { "Format in which the OAuth2 token will be sent", "'{token}' will be replaced by the actual token. 'Bearer {token}' by default." } },
        };

        private TextBox ntlmUsername;
        private TextBox ntlmPassword;

        private CheckBox dynamicArrayFormulasLockExcel;
        private TextBox dynamicArrayFormulasPrefix;
        private NumericUpDown dynamicArrayFormulasCacheDuration;
        private NumericUpDown dynamicArrayFormulasCacheSize;

        private CheckBox legacyArrayFormulasLockExcel;
        private TextBox legacyArrayFormulasPrefix;
        private NumericUpDown legacyArrayFormulasCacheDuration;
        private NumericUpDown legacyArrayFormulasCacheSize;

        private TextBox vbaCompatibleFormulasPrefix;
        private NumericUpDown vbaCompatibleFormulasCacheDuration;
        private NumericUpDown vbaCompatibleFormulasCacheSize;

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

            foreach (var oauth2Item in (IDictionary<string, object>)servicePanel.service.Auth["oauth2"])
                AddOAuth2Param(oauth2Item.Key, oauth2Item.Value.ToString());
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

                #region Description
                {
                    var panel = new GroupBox { Text = "Description", AutoSize = true };

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = string.Format("Short description of {0}", servicePanel.service.Name), UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var description = new TextBox { Location = new Point(PercentWidth(3), PercentWidth(3)), Text = servicePanel.service.description, Width = PercentWidth(75) };
                        tooltip.SetToolTip(description, "Used only in the add-in configure screen for information.");
                        description.TextChanged += Description_TextChanged;
                        panel.Controls.Add(description);
                    }

                    layout.Controls.Add(panel);
                    layout.SetColumnSpan(panel, 5);
                }
                #endregion

                #region Formulas headers
                {

                    layout.Controls.Add(new Label { Width = PercentWidth(5), Text = "Prefix", TextAlign = ContentAlignment.BottomLeft }, 1, 1);
                    layout.Controls.Add(new Label { Width = PercentWidth(10), Text = "Cache duration", TextAlign = ContentAlignment.BottomLeft }, 2, 1);
                    layout.Controls.Add(new Label { Width = PercentWidth(8), Text = "Cache Size", TextAlign = ContentAlignment.BottomLeft }, 3, 1);
                }
                #endregion

                #region Dynamic array formulas
                {
                    Dictionary<string, object> dynamicArrayFormulasOptions = servicePanel.service.Formulas.ContainsKey("dynamic_array") ? (Dictionary<string, object>)servicePanel.service.Formulas["dynamic_array"] : new Dictionary<string, object>();
                    IDictionary<string, object> dynamicArrayFormulasCacheOptions = dynamicArrayFormulasOptions.ContainsKey("cache") ? (Dictionary<string, object>)dynamicArrayFormulasOptions["cache"] : new Dictionary<string, object>();

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate dynamic array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var dynamicArrayFormulas = new CheckBox { Text = "Dynamic array", Checked = dynamicArrayFormulasOptions.Count > 0, Width = PercentWidth(15) };
                        tooltip.SetToolTip(dynamicArrayFormulas, "If your version of Microsoft Excel supports dynamic array formulas, results will be spilled.\nOtherwise results will only fill selected cells.");
                        dynamicArrayFormulas.CheckedChanged += DynamicArrayFormulas_CheckedChanged;
                        layout.Controls.Add(dynamicArrayFormulas, 0, 2);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Prefix used in front of dynamic array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var prefix = dynamicArrayFormulasOptions.ContainsKey("prefix") ? (string)dynamicArrayFormulasOptions["prefix"] : "{name}_";
                        dynamicArrayFormulasPrefix = new TextBox { Text = prefix, Width = PercentWidth(20) };
                        tooltip.SetToolTip(dynamicArrayFormulasPrefix, string.Format("{{name}} will be replaced by {0}", servicePanel.service.Name));
                        dynamicArrayFormulasPrefix.TextChanged += DynamicArrayFormulasPrefix_TextChanged;
                        dynamicArrayFormulasPrefix.Enabled = dynamicArrayFormulasOptions.Count > 0;
                        layout.Controls.Add(dynamicArrayFormulasPrefix, 1, 2);
                    }
                    int cacheDuration = dynamicArrayFormulasCacheOptions.ContainsKey("duration") ? int.Parse(dynamicArrayFormulasCacheOptions["duration"].ToString()) : (int)Service.DefaultFormulasCache["duration"];
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Number of seconds during which a GET request will return previous result.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        dynamicArrayFormulasCacheDuration = new NumericUpDown { Maximum = int.MaxValue, Value = cacheDuration };
                        tooltip.SetToolTip(dynamicArrayFormulasCacheDuration, "Always send a new request by default (0 seconds means that caching is disabled).");
                        dynamicArrayFormulasCacheDuration.TextChanged += DynamicArrayFormulasCacheDuration_TextChanged;
                        dynamicArrayFormulasCacheDuration.Enabled = dynamicArrayFormulasOptions.Count > 0;
                        layout.Controls.Add(dynamicArrayFormulasCacheDuration, 2, 2);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of results to store in cache.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        int cacheSize = dynamicArrayFormulasCacheOptions.ContainsKey("size") ? int.Parse(dynamicArrayFormulasCacheOptions["size"].ToString()) : (int)Service.DefaultFormulasCache["size"];
                        dynamicArrayFormulasCacheSize = new NumericUpDown { Maximum = int.MaxValue, Value = cacheSize };
                        tooltip.SetToolTip(dynamicArrayFormulasCacheSize, "Store the last 100 results by default (if caching is enabled).");
                        dynamicArrayFormulasCacheSize.TextChanged += DynamicArrayFormulasCacheSize_TextChanged;
                        dynamicArrayFormulasCacheSize.Enabled = dynamicArrayFormulasOptions.Count > 0 && cacheDuration > 0;
                        layout.Controls.Add(dynamicArrayFormulasCacheSize, 3, 2);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Lock Microsoft Excel while waiting for results", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var synchronousChecked = dynamicArrayFormulasOptions.ContainsKey("lock_excel") ? (bool)dynamicArrayFormulasOptions["lock_excel"] : false;
                        dynamicArrayFormulasLockExcel = new CheckBox { Text = "Wait for dynamic array result", Checked = synchronousChecked, Width = PercentWidth(22) };
                        tooltip.SetToolTip(dynamicArrayFormulasLockExcel, "Uncheck to still be able to use Microsoft Excel while waiting for results.");
                        dynamicArrayFormulasLockExcel.CheckedChanged += DynamicArrayFormulasLockExcel_CheckedChanged;
                        dynamicArrayFormulasLockExcel.Enabled = dynamicArrayFormulasOptions.Count > 0;
                        layout.Controls.Add(dynamicArrayFormulasLockExcel, 4, 2);
                    }
                }
                #endregion

                #region Legacy array formulas
                {
                    Dictionary<string, object> legacyArrayFormulasOptions = servicePanel.service.Formulas.ContainsKey("legacy_array") ? (Dictionary<string, object>)servicePanel.service.Formulas["legacy_array"] : new Dictionary<string, object>();
                    IDictionary<string, object> legacyArrayFormulasCacheOptions = legacyArrayFormulasOptions.ContainsKey("cache") ? (Dictionary<string, object>)legacyArrayFormulasOptions["cache"] : new Dictionary<string, object>();

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate legacy array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var legacyArrayFormulas = new CheckBox { Text = "Legacy array", Checked = legacyArrayFormulasOptions.Count > 0, Width = PercentWidth(20) };
                        tooltip.SetToolTip(legacyArrayFormulas, "If your version of Microsoft Excel does not supports dynamic array formulas, use this to spill results.");
                        legacyArrayFormulas.CheckedChanged += LegacyArrayFormulas_CheckedChanged;
                        layout.Controls.Add(legacyArrayFormulas, 0, 3);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Prefix used in front of legacy array formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var prefix = legacyArrayFormulasOptions.ContainsKey("prefix") ? (string)legacyArrayFormulasOptions["prefix"] : "legacy_{name}_";
                        legacyArrayFormulasPrefix = new TextBox { Text = prefix, Width = PercentWidth(20) };
                        tooltip.SetToolTip(legacyArrayFormulasPrefix, string.Format("{{name}} will be replaced by {0}", servicePanel.service.Name));
                        legacyArrayFormulasPrefix.TextChanged += LegacyArrayFormulasPrefix_TextChanged;
                        legacyArrayFormulasPrefix.Enabled = legacyArrayFormulasOptions.Count > 0;
                        layout.Controls.Add(legacyArrayFormulasPrefix, 1, 3);
                    }
                    int cacheDuration = legacyArrayFormulasOptions.ContainsKey("duration") ? int.Parse(legacyArrayFormulasOptions["duration"].ToString()) : (int)Service.DefaultFormulasCache["duration"];
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Number of seconds during which a GET request will return previous result.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        legacyArrayFormulasCacheDuration = new NumericUpDown { Maximum = int.MaxValue, Value = cacheDuration };
                        tooltip.SetToolTip(legacyArrayFormulasCacheDuration, "Always send a new request by default (0 seconds means that caching is disabled).");
                        legacyArrayFormulasCacheDuration.TextChanged += LegacyArrayFormulasCacheDuration_TextChanged;
                        legacyArrayFormulasCacheDuration.Enabled = legacyArrayFormulasOptions.Count > 0;
                        layout.Controls.Add(legacyArrayFormulasCacheDuration, 2, 3);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of results to store in cache.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        int cacheSize = legacyArrayFormulasOptions.ContainsKey("size") ? int.Parse(legacyArrayFormulasOptions["size"].ToString()) : (int)Service.DefaultFormulasCache["size"];
                        legacyArrayFormulasCacheSize = new NumericUpDown { Maximum = int.MaxValue, Value = cacheSize };
                        tooltip.SetToolTip(legacyArrayFormulasCacheSize, "Store the last 100 results by default (if caching is enabled).");
                        legacyArrayFormulasCacheSize.TextChanged += LegacyArrayFormulasCacheSize_TextChanged;
                        legacyArrayFormulasCacheSize.Enabled = legacyArrayFormulasOptions.Count > 0 && cacheDuration > 0;
                        layout.Controls.Add(legacyArrayFormulasCacheSize, 3, 3);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Lock Microsoft Excel while waiting for results", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var synchronousChecked = legacyArrayFormulasOptions.ContainsKey("lock_excel") ? (bool)legacyArrayFormulasOptions["lock_excel"] : false;
                        legacyArrayFormulasLockExcel = new CheckBox { Text = "Wait for legacy array result", Checked = synchronousChecked, Width = PercentWidth(30) };
                        tooltip.SetToolTip(legacyArrayFormulasLockExcel, "Uncheck to still be able to use Microsoft Excel while waiting for results.");
                        legacyArrayFormulasLockExcel.CheckedChanged += LegacyArrayFormulasLockExcel_CheckedChanged;
                        legacyArrayFormulasLockExcel.Enabled = legacyArrayFormulasOptions.Count > 0;
                        layout.Controls.Add(legacyArrayFormulasLockExcel, 4, 3);
                    }
                }
                #endregion

                #region Visual Basic compatible formulas
                {
                    Dictionary<string, object> vbaCompatibleFormulasOptions = servicePanel.service.Formulas.ContainsKey("vba_compatible") ? (Dictionary<string, object>)servicePanel.service.Formulas["vba_compatible"] : new Dictionary<string, object>();
                    IDictionary<string, object> vbaCompatibleFormulasCacheOptions = vbaCompatibleFormulasOptions.ContainsKey("cache") ? (Dictionary<string, object>)vbaCompatibleFormulasOptions["cache"] : new Dictionary<string, object>();

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Generate VBA compatible formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var vbaCompatibleFormulas = new CheckBox { Text = "Visual basic", Checked = vbaCompatibleFormulasOptions.Count > 0, Width = PercentWidth(20) };
                        tooltip.SetToolTip(vbaCompatibleFormulas, "Use this formula behavior if you want to call it using Visual Basic for Applications (VBA).");
                        vbaCompatibleFormulas.CheckedChanged += VBACompatibleFormulas_CheckedChanged;
                        layout.Controls.Add(vbaCompatibleFormulas, 0, 4);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Prefix used in front of VBA compatible formulas", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var prefix = vbaCompatibleFormulasOptions.ContainsKey("prefix") ? (string)vbaCompatibleFormulasOptions["prefix"] : "vba_{name}_";
                        vbaCompatibleFormulasPrefix = new TextBox { Text = prefix, Width = PercentWidth(20) };
                        tooltip.SetToolTip(vbaCompatibleFormulasPrefix, string.Format("{{name}} will be replaced by {0}", servicePanel.service.Name));
                        vbaCompatibleFormulasPrefix.TextChanged += VBACompatibleFormulasPrefix_TextChanged;
                        vbaCompatibleFormulasPrefix.Enabled = vbaCompatibleFormulasOptions.Count > 0;
                        layout.Controls.Add(vbaCompatibleFormulasPrefix, 1, 4);
                    }
                    int cacheDuration = vbaCompatibleFormulasCacheOptions.ContainsKey("duration") ? int.Parse(vbaCompatibleFormulasCacheOptions["duration"].ToString()) : (int)Service.DefaultFormulasCache["duration"];
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Number of seconds during which a GET request will return previous result.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        vbaCompatibleFormulasCacheDuration = new NumericUpDown { Maximum = int.MaxValue, Value = cacheDuration };
                        tooltip.SetToolTip(vbaCompatibleFormulasCacheDuration, "Always send a new request by default (0 seconds means that caching is disabled).");
                        vbaCompatibleFormulasCacheDuration.TextChanged += VBACompatibleFormulasCacheDuration_TextChanged;
                        vbaCompatibleFormulasCacheDuration.Enabled = vbaCompatibleFormulasOptions.Count > 0;
                        layout.Controls.Add(vbaCompatibleFormulasCacheDuration, 2, 4);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of results to store in cache.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        int cacheSize = vbaCompatibleFormulasCacheOptions.ContainsKey("size") ? int.Parse(vbaCompatibleFormulasCacheOptions["size"].ToString()) : (int)Service.DefaultFormulasCache["size"];
                        vbaCompatibleFormulasCacheSize = new NumericUpDown { Maximum = int.MaxValue, Value = cacheSize };
                        tooltip.SetToolTip(vbaCompatibleFormulasCacheSize, "Store the last 100 results by default (if caching is enabled).");
                        vbaCompatibleFormulasCacheSize.TextChanged += VBACompatibleFormulasCacheSize_TextChanged;
                        vbaCompatibleFormulasCacheSize.Enabled = vbaCompatibleFormulasOptions.Count > 0 && cacheDuration > 0;
                        layout.Controls.Add(vbaCompatibleFormulasCacheSize, 3, 4);
                    }
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


                    #region Methods
                    {
                        var panel = new GroupBox { AutoSize = true, Text = "Methods" };
                        List<string> selectedMethods = (List<string>)servicePanel.service.OpenAPI["selected_methods"];

                        var get = new CheckBox { Location = new Point(PercentWidth(3), PercentWidth(3)), Text = "get", Checked = selectedMethods.Contains("get"), Width = PercentWidth(11) };
                        get.CheckedChanged += Get_CheckedChanged;
                        panel.Controls.Add(get);
                        var post = new CheckBox { Location = new Point(get.Location.X + get.Width, get.Location.Y), Text = "post", Checked = selectedMethods.Contains("post"), Width = PercentWidth(11) };
                        post.CheckedChanged += Post_CheckedChanged;
                        panel.Controls.Add(post);
                        var put = new CheckBox { Location = new Point(post.Location.X + post.Width, get.Location.Y), Text = "put", Checked = selectedMethods.Contains("put"), Width = PercentWidth(11) };
                        put.CheckedChanged += Put_CheckedChanged;
                        panel.Controls.Add(put);
                        var patch = new CheckBox { Location = new Point(put.Location.X + put.Width, get.Location.Y), Text = "patch", Checked = selectedMethods.Contains("patch"), Width = PercentWidth(11) };
                        patch.CheckedChanged += Patch_CheckedChanged;
                        panel.Controls.Add(patch);
                        var delete = new CheckBox { Location = new Point(patch.Location.X + patch.Width, get.Location.Y), Text = "delete", Checked = selectedMethods.Contains("delete"), Width = PercentWidth(11) };
                        delete.CheckedChanged += Delete_CheckedChanged;
                        panel.Controls.Add(delete);

                        layout.Controls.Add(panel);
                    }
                    #endregion

                    {
                        var panel = new TableLayoutPanel { AutoSize = true };

                        {
                            panel.Controls.Add(new Label { Text = "Host" }, 0, 1);
                            panel.Controls.Add(new Label { Text = "Definition read timeout", Width = PercentWidth(15) }, 1, 1);
                        }

                        {
                            #region Host
                            {
                                ToolTip tooltip = new ToolTip { ToolTipTitle = "Root URL of the server", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                var host = new TextBox { Width = PercentWidth(70), Text = servicePanel.service.Network.ContainsKey("host") ? servicePanel.service.Network["host"].ToString() : string.Empty };
                                tooltip.SetToolTip(host, "Usefull when host is not provided in the OpenAPI definition and API is behind a reverse proxy.");
                                host.TextChanged += Host_TextChanged;
                                panel.Controls.Add(host, 0, 2);
                            }
                            #endregion

                            #region OpenAPI Definition read timeout
                            {
                                ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when requesting an OpenAPI definition", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                var openAPIDefinitionReadTimeout = new NumericUpDown { Dock = DockStyle.Fill, Maximum = int.MaxValue, Value = servicePanel.service.OpenAPI.ContainsKey("definition_read_timeout") ? decimal.Parse(servicePanel.service.OpenAPI["definition_read_timeout"].ToString()) : 5 };
                                tooltip.SetToolTip(openAPIDefinitionReadTimeout, "Wait for 5 seconds by default.");
                                openAPIDefinitionReadTimeout.ValueChanged += OpenAPIDefinitionReadTimeout_ValueChanged;
                                panel.Controls.Add(openAPIDefinitionReadTimeout, 1, 2);
                            }
                            #endregion
                        }

                        layout.Controls.Add(panel);
                    }

                    #region Tags
                    {
                        GroupBox groupBox = new GroupBox { AutoSize = true, Text = "Tags" };

                        var addPanel = new TableLayoutPanel { AutoSize = true, Location = new Point(PercentWidth(3), PercentWidth(3)), Height = PercentWidth(5) };

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

                        groupBox.Controls.Add(addPanel);
                        
                        tagsPanel = new TableLayoutPanel { AutoSize = true, Location = new Point(addPanel.Location.X, addPanel.Location.Y + addPanel.Height), Height = 0 };
                        groupBox.Controls.Add(tagsPanel);

                        layout.Controls.Add(groupBox);
                    }
                    #endregion

                    #region Operation IDs
                    {
                        GroupBox groupBox = new GroupBox { AutoSize = true, Text = "Operation IDs" };

                        var addPanel = new TableLayoutPanel { AutoSize = true, Location = new Point(PercentWidth(3), PercentWidth(3)), Height = PercentWidth(5) };

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

                        groupBox.Controls.Add(addPanel);

                        operationIDsPanel = new TableLayoutPanel { AutoSize = true, Location = new Point(addPanel.Location.X, addPanel.Location.Y + addPanel.Height), Height = 0 };
                        groupBox.Controls.Add(operationIDsPanel);

                        layout.Controls.Add(groupBox);
                    }
                    #endregion

                    #region Parameters
                    {
                        GroupBox groupBox = new GroupBox { AutoSize = true, Text = "Parameters" };

                        var addPanel = new TableLayoutPanel { AutoSize = true, Location = new Point(PercentWidth(3), PercentWidth(3)), Height = PercentWidth(5) };

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

                        groupBox.Controls.Add(addPanel);

                        parametersPanel = new TableLayoutPanel { AutoSize = true, Location = new Point(addPanel.Location.X, addPanel.Location.Y + addPanel.Height), Height = 0 };
                        groupBox.Controls.Add(parametersPanel);

                        layout.Controls.Add(groupBox);
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

                    #region OpenAPI definition authentication settings
                    {
                        var definitionAuths = (Dictionary<string, object>)servicePanel.service.OpenAPI["definition_retrieval_auths"];
                        IDictionary<string, object> definitionApiKeyAuth = definitionAuths.ContainsKey("api_key") ? (Dictionary<string, object>)definitionAuths["api_key"] : new Dictionary<string, object>();

                        var panel = new TableLayoutPanel { AutoSize = true };

                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Authenticate to retrieve OpenAPI definition", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var useAuthForDefinition = new CheckBox { Width = PercentWidth(75), Text = "Use API key to retrieve the OpenAPI definition", Checked = definitionApiKeyAuth.Count > 0 };
                        tooltip.SetToolTip(useAuthForDefinition, "Check to use this API key when retrieving the OpenAPI definition.");
                        useAuthForDefinition.CheckedChanged += UseApiKeyAuthForDefinition_CheckedChanged;
                        panel.Controls.Add(useAuthForDefinition);

                        {
                            apiKeyDefinitionAuthGroup = new GroupBox { AutoSize = true, Text = "OpenAPI definition retrieval" };
                            var apiKeyDefinitionAuthPanel = new TableLayoutPanel { AutoSize = true, Location = new Point(PercentWidth(3), PercentWidth(3)) };

                            bool inQuery = definitionApiKeyAuth.ContainsKey("query_parameter_name");

                            {
                                apiKeyDefinitionAuthPanel.Controls.Add(new Label { Text = "Location", Width = PercentWidth(20) }, 0, 1);
                                apiKeyDefinitionAuthPanel.Controls.Add(new Label { Text = "Name", Width = PercentWidth(40) }, 1, 1);
                            }
                            {
                                ToolTip apiKeyTooltip = new ToolTip { ToolTipTitle = "API key location", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                apiKeyDefinitionAuthLocation = new ComboBox { Dock = DockStyle.Fill, AutoCompleteMode = AutoCompleteMode.SuggestAppend, DropDownStyle = ComboBoxStyle.DropDownList, AutoCompleteSource = AutoCompleteSource.ListItems };
                                apiKeyDefinitionAuthLocation.Items.AddRange(new string[] { "Header", "Query" });
                                apiKeyDefinitionAuthLocation.SelectedItem = inQuery ? "Query" : "Header";
                                apiKeyTooltip.SetToolTip(apiKeyDefinitionAuthLocation, "Location to use to send this API key when retrieving the OpenAPI definition.");
                                apiKeyDefinitionAuthLocation.TextChanged += ApiKeyLocation_TextChanged;
                                apiKeyDefinitionAuthPanel.Controls.Add(apiKeyDefinitionAuthLocation, 0, 2);
                            }
                            {
                                var name = useAuthForDefinition.Checked ? (string)definitionApiKeyAuth[inQuery ? "query_parameter_name" : "header_name"] : string.Empty;
                                ToolTip apiKeyTooltip = new ToolTip { ToolTipTitle = "API key name", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                                apiKeyDefinitionAuthName = new TextBox { Text = name, Dock = DockStyle.Fill };
                                apiKeyTooltip.SetToolTip(apiKeyDefinitionAuthName, "Name of the header or query parameter used to store API key when retrieving the OpenAPI definition.");
                                apiKeyDefinitionAuthName.TextChanged += ApiKeyName_TextChanged;
                                apiKeyDefinitionAuthPanel.Controls.Add(apiKeyDefinitionAuthName, 1, 2);
                            }
                            apiKeyDefinitionAuthGroup.Visible = useAuthForDefinition.Checked;
                            apiKeyDefinitionAuthGroup.Enabled = useAuthForDefinition.Checked;

                            apiKeyDefinitionAuthGroup.Controls.Add(apiKeyDefinitionAuthPanel);
                            panel.Controls.Add(apiKeyDefinitionAuthGroup);
                        }

                        layout.Controls.Add(panel);
                    }
                    #endregion

                    #region API Key
                    {
                        var panel = new GroupBox { AutoSize = true, Text = "API key" };
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "API key", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var apiKey = new TextBox { Location = new Point(PercentWidth(3), PercentWidth(3)), Width = PercentWidth(75), Text = (string)servicePanel.service.Auth["api_key"] };
                        tooltip.SetToolTip(apiKey, "Only used when required.");
                        apiKey.TextChanged += ApiKey_TextChanged;
                        panel.Controls.Add(apiKey);
                        layout.Controls.Add(panel);
                    }
                    #endregion

                    tab.Controls.Add(layout);
                    authTabs.TabPages.Add(tab);
                }
                #endregion

                #region OAuth2 settings
                {
                    var tab = new TabPage { Text = "OAuth2", AutoScroll = true };
                    oauth2ParamsPanel = new TableLayoutPanel { AutoSize = true };
                    var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];

                    #region Table header
                    {
                        var nameLabel = new LinkLabel { Width = PercentWidth(25), Text = "requests_auth parameter name" };
                        nameLabel.Links.Add(0, 13, "https://colin-b.github.io/requests_auth/#oauth-2");
                        nameLabel.LinkClicked += Label_LinkClicked;
                        oauth2ParamsPanel.Controls.Add(nameLabel, 0, 1);
                        var valueLabel = new LinkLabel { Width = PercentWidth(60), Text = "requests_auth parameter value" };
                        valueLabel.Links.Add(0, 13, "https://colin-b.github.io/requests_auth/#oauth-2");
                        valueLabel.LinkClicked += Label_LinkClicked;
                        oauth2ParamsPanel.Controls.Add(valueLabel, 1, 1);
                    }
                    #endregion

                    #region Add row to table
                    {
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of parameter to be sent when requesting the authorization.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            oauth2ParamName = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                            tooltip.SetToolTip(oauth2ParamName, "Parameter will be sent in query.");
                            oauth2ParamName.TextChanged += Oauth2ParamName_TextChanged;
                            oauth2ParamName.KeyDown += Oauth2ParamName_KeyDown;
                            oauth2ParamsPanel.Controls.Add(oauth2ParamName, 0, 2);
                        }
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Value of parameter to be sent when requesting the authorization.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            oauth2ParamValue = new TextBox { Text = string.Empty, Dock = DockStyle.Fill };
                            tooltip.SetToolTip(oauth2ParamValue, "Parameter will be sent in query.");
                            oauth2ParamValue.TextChanged += Oauth2ParamValue_TextChanged;
                            oauth2ParamValue.KeyDown += Oauth2ParamValue_KeyDown;
                            oauth2ParamsPanel.Controls.Add(oauth2ParamValue, 1, 2);
                        }
                        addOAuth2Param = new AddButton(PercentWidth(5));
                        addOAuth2Param.Click += AddOAuth2Param_Click;
                        oauth2ParamsPanel.Controls.Add(addOAuth2Param, 2, 2);
                    }
                    #endregion
                    oauth2ParamsPanel.RowCount += 2;

                    tab.Controls.Add(oauth2ParamsPanel);
                    authTabs.TabPages.Add(tab);
                }
                #endregion

                #region Basic Authentication settings
                {
                    var tab = new TabPage("Basic");
                    var layout = new TableLayoutPanel { AutoSize = true };
                    var basicOptions = (IDictionary<string, object>)servicePanel.service.Auth["basic"];

                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(40), Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
                        layout.Controls.Add(new Label { Width = PercentWidth(40), Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 1, 1);
                    }

                    {
                        #region Username
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "User name.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var userName = new TextBox { Text = (string)basicOptions["username"], Dock = DockStyle.Fill };
                            tooltip.SetToolTip(userName, "Used only if basic authentication is required.");
                            userName.TextChanged += BasicUsername_TextChanged;
                            layout.Controls.Add(userName, 0, 2);
                        }
                        #endregion

                        #region Password
                        {

                            ToolTip tooltip = new ToolTip { ToolTipTitle = "User password to be used if needed.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var password = new TextBox { UseSystemPasswordChar = true, Text = (string)basicOptions["password"], Dock = DockStyle.Fill };
                            tooltip.SetToolTip(password, "Used only if basic authentication is required.");
                            password.TextChanged += BasicPassword_TextChanged;
                            layout.Controls.Add(password, 1, 2);
                        }
                        #endregion
                    }

                    tab.Controls.Add(layout);
                    authTabs.TabPages.Add(tab);
                }
                #endregion

                #region NTLM Authentication settings
                {
                    var tab = new TabPage("Microsoft Windows");
                    var layout = new TableLayoutPanel { AutoSize = true };
                    var ntlmOptions = (IDictionary<string, object>)servicePanel.service.Auth["ntlm"];
                    var userName = ntlmOptions.ContainsKey("username") ? (string)ntlmOptions["username"] : string.Empty;
                    var password = ntlmOptions.ContainsKey("password") ? (string)ntlmOptions["password"] : string.Empty;

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Use current credentials.", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var useLoggedInCredentials = new CheckBox { Width = PercentWidth(40), Text = "Login as current user", Checked = (ntlmOptions.Count > 0 && password.Length == 0 && userName.Length == 0) };
                        tooltip.SetToolTip(useLoggedInCredentials, "Use current Microsoft Windows credentials.");
                        useLoggedInCredentials.CheckedChanged += UseLoggedInCredentials_CheckedChanged;
                        layout.Controls.Add(useLoggedInCredentials, 0, 1);
                        layout.SetColumnSpan(useLoggedInCredentials, 2);
                    }

                    {
                        layout.Controls.Add(new Label { Width = PercentWidth(40), Text = "Username", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
                        layout.Controls.Add(new Label { Width = PercentWidth(40), Text = "Password", TextAlign = ContentAlignment.BottomLeft }, 1, 2);
                    }

                    {
                        #region Username
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "User name (including domain if needed).", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            ntlmUsername = new TextBox { Text = userName, Dock = DockStyle.Fill };
                            tooltip.SetToolTip(ntlmUsername, "To be set if service requires NTLM authentication.");
                            ntlmUsername.TextChanged += NtlmUsername_TextChanged;
                            layout.Controls.Add(ntlmUsername, 0, 3);
                        }
                        #endregion

                        #region Password
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "User password (including domain if needed).", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            ntlmPassword = new TextBox { UseSystemPasswordChar = true, Text = password, Dock = DockStyle.Fill };
                            tooltip.SetToolTip(ntlmPassword, "To be set if service requires NTLM authentication.");
                            ntlmPassword.TextChanged += NtlmPassword_TextChanged;
                            layout.Controls.Add(ntlmPassword, 1, 3);
                        }
                        #endregion
                    }

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

                #region SSL certificate verification
                {
                    var panel = new TableLayoutPanel { AutoSize = true };

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Enable SSL certificate verification", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        var verifyChecked = !networkOptions.ContainsKey("verify") || Convert.ToBoolean(networkOptions["verify"]);
                        var verifySSLCertificate = new CheckBox { Text = "Verify SSL certificate for https requests", Checked = verifyChecked, Width = PercentWidth(60) };
                        tooltip.SetToolTip(verifySSLCertificate, "Uncheck to disable SSL certificate validation.");
                        verifySSLCertificate.CheckedChanged += VerifySSLCertificate_CheckedChanged;
                        panel.Controls.Add(verifySSLCertificate, 0, 1);
                    }

                    layout.Controls.Add(panel);
                }
                #endregion

                {
                    var panel = new TableLayoutPanel { AutoSize = true };

                    {
                        panel.Controls.Add(new Label { Text = "Max retries", Width = PercentWidth(15) }, 0, 1);
                        panel.Controls.Add(new Label { Text = "Connect timeout", Width = PercentWidth(17) }, 1, 1);
                        panel.Controls.Add(new Label { Text = "Read timeout", Width = PercentWidth(15) }, 2, 1);
                    }

                    {
                        #region Max retries
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of time a request should be retried before considered as failed", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var maxRetries = new NumericUpDown { Maximum = int.MaxValue, Value = (int)networkOptions["max_retries"], Dock = DockStyle.Fill };
                            tooltip.SetToolTip(maxRetries, "Retry 5 times by default.");
                            maxRetries.ValueChanged += MaxRetries_ValueChanged;
                            panel.Controls.Add(maxRetries, 0, 2);
                        }
                        #endregion

                        #region Connect timeout
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when trying to reach the service", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var connectTimeout = new NumericUpDown { Maximum = int.MaxValue, Value = Convert.ToDecimal(networkOptions["connect_timeout"]), Dock = DockStyle.Fill };
                            tooltip.SetToolTip(connectTimeout, "Wait for 1 second by default.");
                            connectTimeout.ValueChanged += ConnectTimeout_ValueChanged;
                            panel.Controls.Add(connectTimeout, 1, 2);
                        }
                        #endregion

                        #region Read timeout
                        {
                            ToolTip tooltip = new ToolTip { ToolTipTitle = "Maximum number of seconds to wait when requesting the service", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                            var readTimeout = new NumericUpDown { Maximum = int.MaxValue, Value = Convert.ToDecimal(networkOptions["read_timeout"]), Dock = DockStyle.Fill };
                            tooltip.SetToolTip(readTimeout, "Wait for 5 seconds by default.");
                            readTimeout.ValueChanged += ReadTimeout_ValueChanged;
                            panel.Controls.Add(readTimeout, 2, 2);
                        }
                        #endregion
                    }

                    layout.Controls.Add(panel);
                }

                #region Proxies
                {
                    var groupBox = new GroupBox { AutoSize = true, Text = "Proxy" };
                    var panel = new TableLayoutPanel { AutoSize = true, Location = new Point(PercentWidth(3), PercentWidth(3)) };

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

                    groupBox.Controls.Add(panel);
                    layout.Controls.Add(groupBox);
                }
                #endregion

                #region Headers
                {
                    var groupBox = new GroupBox { AutoSize = true, Text = "Headers" };
                    var panel = new TableLayoutPanel { AutoSize = true, Location = new Point(PercentWidth(3), PercentWidth(3)) };


                    var nameLabel = new Label { Text = "Header name", Width = PercentWidth(20) };
                    panel.Controls.Add(nameLabel, 0, 1);

                    var valueLabel = new Label { Text = "Header value", Width = PercentWidth(65) };
                    panel.Controls.Add(valueLabel, 1, 1);

                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Name of the header field", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        headerName = new TextBox { Text = string.Empty, Width = PercentWidth(20) };
                        tooltip.SetToolTip(headerName, "Sent in every request on this service.");
                        headerName.TextChanged += HeaderName_TextChanged;
                        headerName.KeyDown += HeaderName_KeyDown;
                        panel.Controls.Add(headerName, 0, 2);
                    }
                    {
                        ToolTip tooltip = new ToolTip { ToolTipTitle = "Value of the header field", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                        headerValue = new TextBox { Text = string.Empty, Width = PercentWidth(65) };
                        tooltip.SetToolTip(headerValue, "Sent in every request on this service.");
                        headerValue.TextChanged += HeaderValue_TextChanged;
                        headerValue.KeyDown += HeaderValue_KeyDown;
                        panel.Controls.Add(headerValue, 1, 2);
                    }
                    addHeader = new AddButton(PercentWidth(5));
                    addHeader.Click += AddHeader_Click;
                    panel.Controls.Add(addHeader, 2, 2);

                    headersPanel = new TableLayoutPanel { AutoSize = true, Height=0 };
                    panel.Controls.Add(headersPanel, 0, 3);
                    panel.SetColumnSpan(headersPanel, 3);

                    groupBox.Controls.Add(panel);
                    layout.Controls.Add(groupBox);
                }
                #endregion

                tab.Controls.Add(layout);
                tabs.TabPages.Add(tab);
            }
            #endregion

            Controls.Add(tabs);
        }

        private void Label_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start((string)e.Link.LinkData);
        }

        #region Events

        private void Description_TextChanged(object sender, EventArgs e)
        {
            servicePanel.service.description = ((TextBox)sender).Text;
        }

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

        private void UseLoggedInCredentials_CheckedChanged(object sender, EventArgs e)
        {
            var useLoggedInCredentials = ((CheckBox)sender).Checked;
            var ntlmOptions = (IDictionary<string, object>)servicePanel.service.Auth["ntlm"];
            // Use NTLM authentication with logged in user credentials
            if (useLoggedInCredentials)
            {
                ntlmOptions["username"] = string.Empty;
                ntlmOptions["password"] = string.Empty;
                ntlmUsername.Text = string.Empty;
                ntlmPassword.Text = string.Empty;
                ntlmUsername.Enabled = false;
                ntlmPassword.Enabled = false;
            }
            else
            {
                ntlmUsername.Enabled = true;
                ntlmPassword.Enabled = true;
                var userName = ntlmUsername.Text;
                var password = ntlmPassword.Text;

                // Disable NTLM authentication
                if (string.IsNullOrEmpty(userName) && string.IsNullOrEmpty(password))
                {
                    ntlmOptions.Clear();
                }
                // Use NTLM authentication with custom credentials
                else
                {
                    ntlmOptions["username"] = userName;
                    ntlmOptions["password"] = password;
                }
            }
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

        private void Host_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(((TextBox)sender).Text))
                servicePanel.service.Network.Remove("host");
            else
                servicePanel.service.Network["host"] = ((TextBox)sender).Text;
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

        #region API key authentication
        private void UseApiKeyAuthForDefinition_CheckedChanged(object sender, EventArgs e)
        {
            var useApiKeyAuth = ((CheckBox)sender).Checked;
            apiKeyDefinitionAuthGroup.Visible = useApiKeyAuth;
            apiKeyDefinitionAuthGroup.Enabled = useApiKeyAuth;

            if (useApiKeyAuth)
            {
                var definitionAuths = (Dictionary<string, object>)servicePanel.service.OpenAPI["definition_retrieval_auths"];
                bool inQuery = (string)apiKeyDefinitionAuthLocation.SelectedItem == "Query";
                definitionAuths["api_key"] = new Dictionary<string, object> { { inQuery ? "query_parameter_name" : "header_name", apiKeyDefinitionAuthName.Text } };
            }
            else
            {
                var definitionAuths = (Dictionary<string, object>)servicePanel.service.OpenAPI["definition_retrieval_auths"];
                definitionAuths.Remove("api_key");
            }
        }

        private void ApiKeyName_TextChanged(object sender, EventArgs e)
        {
            var apiKeyDefinitionAuth = (IDictionary<string, object>)((IDictionary<string, object>)servicePanel.service.OpenAPI["definition_retrieval_auths"])["api_key"];
            if (apiKeyDefinitionAuth.ContainsKey("query_parameter_name"))
                apiKeyDefinitionAuth["query_parameter_name"] = ((TextBox)sender).Text;
            else
                apiKeyDefinitionAuth["header_name"] = ((TextBox)sender).Text;
        }

        private void ApiKeyLocation_TextChanged(object sender, EventArgs e)
        {
            var apiKeyDefinitionAuth = (IDictionary<string, object>)((IDictionary<string, object>)servicePanel.service.OpenAPI["definition_retrieval_auths"])["api_key"];
            if (apiKeyDefinitionAuth.ContainsKey("query_parameter_name"))
            {
                apiKeyDefinitionAuth["header_name"] = apiKeyDefinitionAuth["query_parameter_name"];
                apiKeyDefinitionAuth.Remove("query_parameter_name");
            }
            else
            {
                apiKeyDefinitionAuth["query_parameter_name"] = apiKeyDefinitionAuth["header_name"];
                apiKeyDefinitionAuth.Remove("header_name");
            }
        }

        private void ApiKey_TextChanged(object sender, EventArgs e)
        {
            servicePanel.service.Auth["api_key"] = ((TextBox)sender).Text;
        }
        #endregion

        private void LegacyArrayFormulas_CheckedChanged(object sender, EventArgs e)
        {
            bool legacyArrayFormulasChecked = ((CheckBox)sender).Checked;
            if (legacyArrayFormulasChecked)
            {
                servicePanel.service.Formulas["legacy_array"] = new Dictionary<string, object>();
                LegacyArrayFormulasLockExcel_CheckedChanged();
                LegacyArrayFormulasPrefix_TextChanged();
                LegacyArrayFormulasCacheDuration_TextChanged();
                LegacyArrayFormulasCacheSize_TextChanged();
            }
            else
            {
                servicePanel.service.Formulas.Remove("legacy_array");
            }

            legacyArrayFormulasLockExcel.Enabled = legacyArrayFormulasChecked;
            legacyArrayFormulasPrefix.Enabled = legacyArrayFormulasChecked;
            legacyArrayFormulasCacheDuration.Enabled = legacyArrayFormulasChecked;
            legacyArrayFormulasCacheSize.Enabled = legacyArrayFormulasChecked && legacyArrayFormulasCacheDuration.Value > 0;
        }

        private void LegacyArrayFormulasLockExcel_CheckedChanged(object sender, EventArgs e)
        {
            LegacyArrayFormulasLockExcel_CheckedChanged();
        }

        private void LegacyArrayFormulasPrefix_TextChanged(object sender, EventArgs e)
        {
            LegacyArrayFormulasPrefix_TextChanged();
        }

        private void LegacyArrayFormulasLockExcel_CheckedChanged()
        {
            AddValueToFormulasSubSection("legacy_array", "lock_excel", legacyArrayFormulasLockExcel.Checked);
        }

        private void LegacyArrayFormulasPrefix_TextChanged()
        {
            AddValueToFormulasSubSection("legacy_array", "prefix", legacyArrayFormulasPrefix.Text);
        }

        private void LegacyArrayFormulasCacheDuration_TextChanged(object sender, EventArgs e)
        {
            legacyArrayFormulasCacheSize.Enabled = ((NumericUpDown)sender).Value > 0;
            LegacyArrayFormulasCacheDuration_TextChanged();
        }

        private void LegacyArrayFormulasCacheDuration_TextChanged()
        {
            AddValueToFormulasCache("legacy_array", "duration", legacyArrayFormulasCacheDuration.Value);
        }

        private void LegacyArrayFormulasCacheSize_TextChanged(object sender, EventArgs e)
        {
            LegacyArrayFormulasCacheSize_TextChanged();
        }

        private void LegacyArrayFormulasCacheSize_TextChanged()
        {
            AddValueToFormulasCache("legacy_array", "size", legacyArrayFormulasCacheSize.Value);
        }

        private void DynamicArrayFormulas_CheckedChanged(object sender, EventArgs e)
        {
            bool dynamicArrayFormulasChecked = ((CheckBox)sender).Checked;
            if (dynamicArrayFormulasChecked)
            {
                servicePanel.service.Formulas["dynamic_array"] = new Dictionary<string, object>();
                DynamicArrayFormulasLockExcel_CheckedChanged();
                DynamicArrayFormulasPrefix_TextChanged();
                DynamicArrayFormulasCacheDuration_TextChanged();
                DynamicArrayFormulasCacheSize_TextChanged();
            }
            else
            {
                servicePanel.service.Formulas.Remove("dynamic_array");
            }

            dynamicArrayFormulasLockExcel.Enabled = dynamicArrayFormulasChecked;
            dynamicArrayFormulasPrefix.Enabled = dynamicArrayFormulasChecked;
            dynamicArrayFormulasCacheDuration.Enabled = dynamicArrayFormulasChecked;
            dynamicArrayFormulasCacheSize.Enabled = dynamicArrayFormulasChecked && dynamicArrayFormulasCacheDuration.Value > 0;
        }

        private void DynamicArrayFormulasLockExcel_CheckedChanged(object sender, EventArgs e)
        {
            DynamicArrayFormulasLockExcel_CheckedChanged();
        }

        private void DynamicArrayFormulasPrefix_TextChanged(object sender, EventArgs e)
        {
            DynamicArrayFormulasPrefix_TextChanged();
        }

        private void DynamicArrayFormulasLockExcel_CheckedChanged()
        {
            AddValueToFormulasSubSection("dynamic_array", "lock_excel", dynamicArrayFormulasLockExcel.Checked);
        }

        private void DynamicArrayFormulasPrefix_TextChanged()
        {
            AddValueToFormulasSubSection("dynamic_array", "prefix", dynamicArrayFormulasPrefix.Text);
        }

        private void DynamicArrayFormulasCacheDuration_TextChanged(object sender, EventArgs e)
        {
            dynamicArrayFormulasCacheSize.Enabled = ((NumericUpDown)sender).Value > 0;
            DynamicArrayFormulasCacheDuration_TextChanged();
        }

        private void DynamicArrayFormulasCacheDuration_TextChanged()
        {
            AddValueToFormulasCache("dynamic_array", "duration", dynamicArrayFormulasCacheDuration.Value);
        }

        private void DynamicArrayFormulasCacheSize_TextChanged(object sender, EventArgs e)
        {
            DynamicArrayFormulasCacheSize_TextChanged();
        }

        private void DynamicArrayFormulasCacheSize_TextChanged()
        {
            AddValueToFormulasCache("dynamic_array", "size", dynamicArrayFormulasCacheSize.Value);
        }

        private void VBACompatibleFormulas_CheckedChanged(object sender, EventArgs e)
        {
            bool vbaCompatibleFormulasChecked = ((CheckBox)sender).Checked;
            if (vbaCompatibleFormulasChecked)
            {
                servicePanel.service.Formulas["vba_compatible"] = new Dictionary<string, object>();
                AddValueToFormulasSubSection("vba_compatible", "lock_excel", true);
                VBACompatibleFormulasPrefix_TextChanged();
                VBACompatibleFormulasCacheDuration_TextChanged();
                VBACompatibleFormulasCacheSize_TextChanged();
            }
            else
            {
                servicePanel.service.Formulas.Remove("vba_compatible");
            }
            vbaCompatibleFormulasPrefix.Enabled = vbaCompatibleFormulasChecked;
            vbaCompatibleFormulasCacheDuration.Enabled = vbaCompatibleFormulasChecked;
            vbaCompatibleFormulasCacheSize.Enabled = vbaCompatibleFormulasChecked && vbaCompatibleFormulasCacheDuration.Value > 0;
        }

        private void VBACompatibleFormulasPrefix_TextChanged(object sender, EventArgs e)
        {
            VBACompatibleFormulasPrefix_TextChanged();
        }

        private void VBACompatibleFormulasPrefix_TextChanged()
        {
            AddValueToFormulasSubSection("vba_compatible", "prefix", vbaCompatibleFormulasPrefix.Text);
        }

        private void VBACompatibleFormulasCacheDuration_TextChanged(object sender, EventArgs e)
        {
            vbaCompatibleFormulasCacheSize.Enabled = ((NumericUpDown)sender).Value > 0;
            VBACompatibleFormulasCacheDuration_TextChanged();
        }

        private void VBACompatibleFormulasCacheDuration_TextChanged()
        {
            AddValueToFormulasCache("vba_compatible", "duration", vbaCompatibleFormulasCacheDuration.Value);
        }

        private void VBACompatibleFormulasCacheSize_TextChanged(object sender, EventArgs e)
        {
            VBACompatibleFormulasCacheSize_TextChanged();
        }

        private void VBACompatibleFormulasCacheSize_TextChanged()
        {
            AddValueToFormulasCache("vba_compatible", "size", vbaCompatibleFormulasCacheSize.Value);
        }

        private void AddValueToFormulasSubSection(string formulaType, string key, object value)
        {
            ((IDictionary<string, object>)servicePanel.service.Formulas[formulaType])[key] = value;
        }

        private void AddValueToFormulasCache(string formulaType, string key, object value)
        {
            var formulaOptions = (IDictionary<string, object>)servicePanel.service.Formulas[formulaType];
            if (!formulaOptions.ContainsKey("cache"))
                formulaOptions["cache"] = new Dictionary<string, object>();

            ((IDictionary<string, object>)formulaOptions["cache"])[key] = value;
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
            var row = oauth2ParamsPanel.RowCount + 1;
            oauth2ParamsPanel.Controls.Add(new Label { Text = name, Dock = DockStyle.Fill }, 0, row);

            Control valueTextBox;
            try
            {
                valueTextBox = new NumericUpDown { Width = PercentWidth(60), Maximum = int.MaxValue, Value = Convert.ToDecimal(value), Name = name };
            }
            catch (Exception)
            {
                valueTextBox = new TextBox { Width = PercentWidth(60), Text = value, Name = name  };
            }

            valueTextBox.TextChanged += OAuth2ParamValue_TextChanged;

            ToolTip tooltip = new ToolTip { UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };
            if (oauth2ToolTips.ContainsKey(name))
            {
                tooltip.ToolTipTitle = oauth2ToolTips[name][0];
                tooltip.SetToolTip(valueTextBox, oauth2ToolTips[name][1]);
            }
            else
            {
                tooltip.ToolTipTitle = string.Format("Value of {0} requests_auth parameter", name);
                tooltip.SetToolTip(valueTextBox, "Check requests_auth documentation for more details.");
            }

            oauth2ParamsPanel.Controls.Add(valueTextBox, 1, row);

            var remove = new DeleteButton(PercentWidth(5));
            remove.Name = row.ToString();
            remove.Click += RemoveOAuth2Param_Click;
            oauth2ParamsPanel.Controls.Add(remove, 2, row);
            oauth2ParamsPanel.RowCount += 1;
        }

        private void OAuth2ParamValue_TextChanged(object sender, EventArgs e)
        {
            var valueTextBox = (Control)sender;
            var paramName = valueTextBox.Name;

            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];

            if (valueTextBox is NumericUpDown valueNumericUpDown)
                oauth2Options[paramName] = valueNumericUpDown.Value;
            else
                oauth2Options[paramName] = valueTextBox.Text;
        }

        private void RemoveOAuth2Param_Click(object sender, EventArgs e)
        {
            int row = Convert.ToInt32(((Control)sender).Name);
            var paramName = oauth2ParamsPanel.GetControlFromPosition(1, row).Name;

            var oauth2Options = (IDictionary<string, object>)servicePanel.service.Auth["oauth2"];
            oauth2Options.Remove(paramName);

            oauth2ParamsPanel.Controls.Remove(oauth2ParamsPanel.GetControlFromPosition(0, row));
            oauth2ParamsPanel.Controls.Remove(oauth2ParamsPanel.GetControlFromPosition(1, row));
            oauth2ParamsPanel.Controls.Remove((Control)sender);
        }

        #endregion

        #endregion
    }
}
