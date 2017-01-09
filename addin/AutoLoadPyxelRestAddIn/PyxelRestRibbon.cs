using System;
using Microsoft.Office.Tools.Ribbon;
using System.Windows.Forms;
using Opulos.Core.UI;
using System.Drawing;
using IniParser;
using IniParser.Model;
using System.Collections.Generic;
using System.Text;
using log4net;

namespace AutoLoadPyxelRestAddIn
{
    public partial class PyxelRestRibbon
    {
        private static readonly string UDF_IMPORT_FAILURE_MSG = 
            "User Defined Functions cannot be loaded.\n"+
            "Please check that you trust access to Visual Basic Project\n";

        private void PyxelRestRibbon_Load(object sender, RibbonUIEventArgs e)
        {
            importButton.Click += ImportUserDefinedFunctions;
            configureButton.Click += ConfigureServices;
        }

        private void ConfigureServices(object sender, RibbonControlEventArgs e)
        {
            if(DialogResult.Yes == new ServiceConfigurationFrame().ShowDialog())
            {
                if (!Globals.ThisAddIn.ImportUserDefinedFunctions())
                    MessageBox.Show(
                        UDF_IMPORT_FAILURE_MSG,
                        "Import failed",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Warning);
            }
        }

        private void ImportUserDefinedFunctions(object sender, RibbonControlEventArgs e)
        {
            if(!Globals.ThisAddIn.ImportUserDefinedFunctions())
                MessageBox.Show(
                    UDF_IMPORT_FAILURE_MSG, 
                    "Import failed",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
        }
    }

    public partial class ServiceConfigurationFrame : Form
    {
        private static readonly ILog Log = LogManager.GetLogger("ServiceConfigurationFrame");

        private Accordion accordion;
        private TextBox newServiceName;
        private Button addServiceButton;
        private List<Service> services = new List<Service>();
        private Button saveButton;

        public ServiceConfigurationFrame()
        {
            try
            {
                InitializeComponent();
                LoadServices();
            }
            catch (Exception e)
            {
                Log.Error("Unable to create configuration frame.", e);
                throw e;
            }
        }

        private void InitializeComponent()
        {
            Icon = Properties.Resources.settings_8_16;
            AutoSize = true;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Text = "Configure PyxelRest Services";
            MaximumSize = new Size(800, 600);
            AutoScroll = true;

            TableLayoutPanel layout = new TableLayoutPanel();
            layout.AutoSize = true;

            #region Services
            accordion = new Accordion();
            accordion.CheckBoxMargin = new Padding(2);
            accordion.ContentMargin = new Padding(15, 5, 15, 5);
            accordion.ContentPadding = new Padding(1);
            accordion.Insets = new Padding(5);
            accordion.ControlBackColor = Color.Transparent;
            accordion.ContentBackColor = Color.Transparent;
            accordion.AutoSize = true;
            layout.Controls.Add(accordion);
            #endregion

            #region New Service
            TableLayoutPanel newServicePanel = new TableLayoutPanel();
            newServicePanel.AutoSize = true;
            newServicePanel.Dock = DockStyle.Fill;
            newServiceName = new TextBox();
            newServiceName.Dock = DockStyle.Fill;
            newServiceName.AutoSize = true;
            newServiceName.TextChanged += NewServiceName_TextChanged;
            newServicePanel.Controls.Add(newServiceName, 0, 0);
            addServiceButton = new Button();
            addServiceButton.Text = "Enter service name to create a new configuration";
            addServiceButton.ForeColor = Color.DarkBlue;
            addServiceButton.BackColor = Color.LightGray;
            addServiceButton.Dock = DockStyle.Fill;
            addServiceButton.AutoSize = true;
            addServiceButton.Click += AddServiceSection;
            addServiceButton.Enabled = false;
            newServicePanel.Controls.Add(addServiceButton, 0, 1);
            layout.Controls.Add(newServicePanel);
            #endregion

            #region Save
            saveButton = new Button();
            saveButton.Text = "Save Configuration";
            saveButton.ForeColor = Color.DarkGreen;
            saveButton.BackColor = Color.LightGreen;
            saveButton.DialogResult = DialogResult.Yes;
            saveButton.Dock = DockStyle.Fill;
            saveButton.AutoSize = true;
            saveButton.Click += Save;
            layout.Controls.Add(saveButton);
            #endregion

            Controls.Add(layout);
        }

        private void NewServiceName_TextChanged(object sender, EventArgs e)
        {
            newServiceName.Text = newServiceName.Text.Replace(' ', '_');
            if (newServiceName.TextLength > 0)
            {
                string newService = newServiceName.Text;
                bool alreadyExists = services.Exists(s => s.HasName(newService));
                addServiceButton.Enabled = !alreadyExists;
                if (alreadyExists)
                {
                    addServiceButton.Text = newService + " configuration already exists";
                    addServiceButton.BackColor = Color.OrangeRed;
                }
                else
                {
                    addServiceButton.Text = "Add " + newService + " configuration";
                    addServiceButton.BackColor = Color.LightBlue;
                }
            }
            else
            {
                addServiceButton.Enabled = false;
                addServiceButton.Text = "Enter service name to create a new configuration";
                addServiceButton.BackColor = Color.LightGray;
            }
        }

        private void LoadServices()
        {
            services.Clear();

            var parser = new FileIniDataParser();
            string configurationFilePath = GetConfigurationFilePath();
            if (configurationFilePath == null)
            {
                Log.Error("Configuration cannot be loaded as configuration file path cannot be found.");
                return;
            }

            IniData config = parser.ReadFile(configurationFilePath);

            foreach (var section in config.Sections)
            {
                if ("DEFAULT".Equals(section.SectionName))
                    continue;
                displayService(new Service(this, section, config), false);
            }
        }

        private void displayService(Service service, bool expanded)
        {
            service.Added(accordion, expanded);
            services.Add(service);
            saveButton.Enabled = IsValid();
        }

        private bool IsValid()
        {
            foreach (Service service in services)
                if (!service.IsValid())
                    return false;
            return true;
        }

        private string GetConfigurationFilePath()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if (appDataFolder != null)
                return System.IO.Path.Combine(appDataFolder, "pyxelrest", "configuration.ini");
            return null;
        }

        private void AddServiceSection(object sender, EventArgs e)
        {
            displayService(new Service(this, newServiceName.Text), true);
            Log.InfoFormat("Adding configuration for {0} service.", newServiceName.Text);
            newServiceName.Text = "";
        }

        private void Save(object sender, EventArgs e)
        {
            var parser = new FileIniDataParser();
            string configurationFilePath = GetConfigurationFilePath();
            if(configurationFilePath == null)
            {
                Log.Error("Configuration cannot be saved as configuration file path cannot be found.");
                return;
            }
            IniData config = parser.ReadFile(configurationFilePath);

            config.Sections.Clear();
            foreach (Service service in services)
                config.Sections.Add(service.ToSection());
            parser.WriteFile(configurationFilePath, config);
            Log.Info("Services configuration updated.");
        }

        internal void Removed(Service service)
        {
            Log.InfoFormat("Removing '{0}' service configuration.", service);
            services.Remove(service);
            saveButton.Enabled = IsValid();
        }

        internal void Updated(Service service)
        {
            saveButton.Enabled = IsValid();
        }
    }

    public sealed class Service
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private static readonly string GET = "get";
        private static readonly string POST = "post";
        private static readonly string PUT = "put";
        private static readonly string DELETE = "delete";

        private readonly string Name;
        private readonly TableLayoutPanel servicePanel;
        private TextBox hostTextBox;
        private TextBox swaggerBasePathTextBox;
        private CheckBox get;
        private CheckBox post;
        private CheckBox put;
        private CheckBox delete;
        private CheckBox checkbox;

        private readonly ServiceConfigurationFrame configurationFrame;

        public Service(ServiceConfigurationFrame configurationFrame, SectionData section, IniData config)
        {
            this.configurationFrame = configurationFrame;
            string[] defaultMethods = config["DEFAULT"] == null ? new string[0] : config["DEFAULT"]["methods"].Split(',');
            string defaultSwaggerBasePath = config["DEFAULT"] == null ? "" : config["DEFAULT"]["swaggerBasePath"];

            Name = section.SectionName;

            servicePanel = DefaultPanel();
            hostTextBox.Text = config[section.SectionName]["host"];
            swaggerBasePathTextBox.Text = config[section.SectionName]["swaggerBasePath"] ?? defaultSwaggerBasePath;
            string[] methods = config[section.SectionName]["methods"].Split(',') ?? defaultMethods;
            for (int i = 0; i < methods.Length; i++)
                methods[i] = methods[i].Trim();
            get.Checked = Array.Exists(methods, s => GET.Equals(s));
            post.Checked = Array.Exists(methods, s => POST.Equals(s));
            put.Checked = Array.Exists(methods, s => PUT.Equals(s));
            delete.Checked = Array.Exists(methods, s => DELETE.Equals(s));
        }

        public Service(ServiceConfigurationFrame configurationFrame, string name)
        {
            this.configurationFrame = configurationFrame;
            Name = name;

            servicePanel = DefaultPanel();
            swaggerBasePathTextBox.Text = "/";
            get.Checked = true;
            post.Checked = true;
            put.Checked = true;
            delete.Checked = true;
        }

        public SectionData ToSection()
        {
            SectionData section = new SectionData(Name);
            section.Keys = new KeyDataCollection();

            KeyData host = new KeyData("host");
            host.Value = hostTextBox.Text;
            section.Keys.SetKeyData(host);

            KeyData swaggerBasePath = new KeyData("swaggerBasePath");
            swaggerBasePath.Value = swaggerBasePathTextBox.Text;
            section.Keys.SetKeyData(swaggerBasePath);

            KeyData methods = new KeyData("methods");
            methods.Value = GetMethods();
            section.Keys.SetKeyData(methods);

            return section;
        }

        private string GetMethods()
        {
            StringBuilder sb = new StringBuilder();
            if (get.Checked)
                sb.Append(GET);
            if (post.Checked)
                AppendMethod(sb, POST);
            if (put.Checked)
                AppendMethod(sb, PUT);
            if (delete.Checked)
                AppendMethod(sb, DELETE);
            return sb.ToString();
        }

        private void AppendMethod(StringBuilder sb, string method)
        {
            if (sb.Length > 0)
                sb.Append(", ");
            sb.Append(method);
        }

        private TableLayoutPanel DefaultPanel()
        {
            TableLayoutPanel servicePanel = new TableLayoutPanel { Dock = DockStyle.Fill, Padding = new Padding(5) };
            servicePanel.TabStop = true;

            servicePanel.Controls.Add(new Label { Width = 120, Text = "Host (mandatory)", TextAlign = ContentAlignment.BottomLeft }, 0, 0);
            hostTextBox = new TextBox();
            hostTextBox.Dock = DockStyle.Fill;
            hostTextBox.AutoSize = true;
            hostTextBox.TextChanged += HostTextBox_TextChanged;
            servicePanel.Controls.Add(hostTextBox, 1, 0);

            servicePanel.Controls.Add(new Label { Width = 120, Text = "Swagger Base Path", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            swaggerBasePathTextBox = new TextBox();
            swaggerBasePathTextBox.Dock = DockStyle.Fill;
            swaggerBasePathTextBox.AutoSize = true;
            servicePanel.Controls.Add(swaggerBasePathTextBox, 1, 1);

            servicePanel.Controls.Add(new Label { Width = 120, Text = "Methods", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            TableLayoutPanel methodsPanel = new TableLayoutPanel();
            methodsPanel.Dock = DockStyle.Fill;
            methodsPanel.AutoSize = true;
            get = new CheckBox();
            get.Text = "get";
            methodsPanel.Controls.Add(get, 0, 0);
            post = new CheckBox();
            post.Text = "post";
            methodsPanel.Controls.Add(post, 1, 0);
            put = new CheckBox();
            put.Text = "put";
            methodsPanel.Controls.Add(put, 2, 0);
            delete = new CheckBox();
            delete.Text = "delete";
            methodsPanel.Controls.Add(delete, 3, 0);
            servicePanel.Controls.Add(methodsPanel, 1, 2);

            Button deleteButton = new Button() { Text = "Delete " + Name + " Configuration" };
            deleteButton.Dock = DockStyle.Fill;
            deleteButton.ForeColor = Color.White;
            deleteButton.BackColor = Color.MediumOrchid;
            deleteButton.AutoSize = true;
            deleteButton.Click += DeleteButton_Click;
            servicePanel.Controls.Add(deleteButton);
            servicePanel.SetColumnSpan(deleteButton, 2);

            return servicePanel;
        }

        private void HostTextBox_TextChanged(object sender, EventArgs e)
        {
            configurationFrame.Updated(this);
        }

        public bool IsValid()
        {
            return hostTextBox.TextLength > 0;
        }

        internal void Added(Accordion accordion, bool expanded)
        {
            checkbox = accordion.Add(servicePanel, Name, open: expanded);
        }

        private void DeleteButton_Click(object sender, EventArgs e)
        {
            checkbox.Visible = false;
            configurationFrame.Removed(this);
        }

        public override string ToString()
        {
            return Name;
        }

        internal bool HasName(string serviceName)
        {
            return Name.Equals(serviceName);
        }
    }
}
