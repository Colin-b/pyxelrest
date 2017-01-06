using System;
using Microsoft.Office.Tools.Ribbon;
using System.Windows.Forms;
using Opulos.Core.UI;
using System.Drawing;
using IniParser;
using IniParser.Model;
using System.Collections.Generic;

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
        private Accordion accordion;
        private TextBox newServiceName;
        private Button addServiceButton;
        private List<Service> services = new List<Service>();
        private Button saveButton;

        public ServiceConfigurationFrame()
        {
            InitializeComponent();
            LoadServices();
        }

        private void InitializeComponent()
        {
            AutoSize = true;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Text = "Configure PyxelRest Services";
            MaximumSize = new Size(800, 600);
            AutoScroll = true;

            TableLayoutPanel layout = new TableLayoutPanel();
            layout.AutoSize = true;

            accordion = new Accordion();
            accordion.CheckBoxMargin = new Padding(2);
            accordion.ContentMargin = new Padding(15, 5, 15, 5);
            accordion.ContentPadding = new Padding(1);
            accordion.Insets = new Padding(5);
            accordion.ControlBackColor = Color.Transparent;
            accordion.ContentBackColor = Color.Transparent;
            accordion.AutoSize = true;
            layout.Controls.Add(accordion);

            TableLayoutPanel newServicePanel = new TableLayoutPanel();
            newServicePanel.AutoSize = true;
            newServicePanel.Dock = DockStyle.Fill;
            newServiceName = new TextBox();
            newServiceName.Dock = DockStyle.Fill;
            newServiceName.AutoSize = true;
            newServiceName.TextChanged += NewServiceName_TextChanged;
            newServicePanel.Controls.Add(newServiceName, 0, 0);
            addServiceButton = new Button();
            addServiceButton.Text = "Create a new service";
            addServiceButton.Dock = DockStyle.Fill;
            addServiceButton.AutoSize = true;
            addServiceButton.Click += AddServiceSection;
            addServiceButton.Enabled = false;
            newServicePanel.Controls.Add(addServiceButton, 0, 1);
            layout.Controls.Add(newServicePanel);

            saveButton = new Button();
            saveButton.Text = "Save Configuration";
            saveButton.DialogResult = DialogResult.Yes;
            saveButton.Dock = DockStyle.Fill;
            saveButton.AutoSize = true;
            saveButton.Click += Save;
            layout.Controls.Add(saveButton);

            Controls.Add(layout);
        }

        private void NewServiceName_TextChanged(object sender, EventArgs e)
        {
            if(newServiceName.TextLength > 0)
                addServiceButton.Enabled = !services.Exists(s => newServiceName.Text.Equals(s.Name));
            else
                addServiceButton.Enabled = false;
        }

        private void LoadServices()
        {
            var parser = new FileIniDataParser();
            IniData config = parser.ReadFile(GetConfigurationFilePath());

            services.Clear();

            foreach (var section in config.Sections)
            {
                if ("DEFAULT".Equals(section.SectionName))
                    continue;
                displayService(new Service(section, config), false);
            }
        }

        private void displayService(Service service, bool expanded)
        {
            service.AddEventHandler(ValidateSaveButton);
            service.Added(accordion, services, expanded);
            saveButton.Enabled = IsValid();
        }

        private void ValidateSaveButton(object sender, EventArgs e)
        {
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
            displayService(new Service(newServiceName.Text), true);
        }

        private void Save(object sender, EventArgs e)
        {
            var parser = new FileIniDataParser();
            string configurationFilePath = GetConfigurationFilePath();
            IniData config = parser.ReadFile(configurationFilePath);

            config.Sections.Clear();
            foreach (Service service in services)
                config.Sections.Add(service.ToSection());
            parser.WriteFile(configurationFilePath, config);
        }
    }

    public sealed class Service
    {
        public string Name;
        public TableLayoutPanel servicePanel;

        private TextBox hostTextBox;
        private TextBox swaggerBasePathTextBox;
        private TextBox methodsTextBox;
        private List<Service> services;
        private CheckBox checkbox;

        public Service(SectionData section, IniData config)
        {
            string defaultMethods = config["DEFAULT"] == null ? null : config["DEFAULT"]["methods"];
            string defaultSwaggerBasePath = config["DEFAULT"] == null ? null : config["DEFAULT"]["swaggerBasePath"];

            Name = section.SectionName;

            servicePanel = DefaultPanel();
            hostTextBox.Text = config[section.SectionName]["host"];
            swaggerBasePathTextBox.Text = config[section.SectionName]["swaggerBasePath"] ?? defaultSwaggerBasePath;
            methodsTextBox.Text = config[section.SectionName]["methods"] ?? defaultMethods;
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
            methods.Value = methodsTextBox.Text;
            section.Keys.SetKeyData(methods);

            return section;
        }

        public Service(string name)
        {
            Name = name;

            servicePanel = DefaultPanel();
            swaggerBasePathTextBox.Text = "/";
            methodsTextBox.Text = "get, post, put, delete";
        }

        private TableLayoutPanel DefaultPanel()
        {
            TableLayoutPanel servicePanel = new TableLayoutPanel { Dock = DockStyle.Fill, Padding = new Padding(5) };
            servicePanel.TabStop = true;

            servicePanel.Controls.Add(new Label { Width = 120, Text = "Host", TextAlign = ContentAlignment.BottomLeft }, 0, 0);
            hostTextBox = new TextBox() { Width = 300, Text = "" };
            servicePanel.Controls.Add(hostTextBox, 1, 0);

            servicePanel.Controls.Add(new Label { Width = 120, Text = "Swagger Base Path", TextAlign = ContentAlignment.BottomLeft }, 0, 1);
            swaggerBasePathTextBox = new TextBox() { Width = 300, Text = "" };
            servicePanel.Controls.Add(swaggerBasePathTextBox, 1, 1);

            servicePanel.Controls.Add(new Label { Width = 120, Text = "Methods", TextAlign = ContentAlignment.BottomLeft }, 0, 2);
            methodsTextBox = new TextBox() { Width = 300, Text = "" };
            servicePanel.Controls.Add(methodsTextBox, 1, 2);

            Button deleteButton = new Button() { Text = "Delete Service" };
            deleteButton.Dock = DockStyle.Fill;
            deleteButton.AutoSize = true;
            deleteButton.Click += DeleteButton_Click;
            servicePanel.Controls.Add(deleteButton);
            servicePanel.SetColumnSpan(deleteButton, 2);

            return servicePanel;
        }

        public bool IsValid()
        {
            return hostTextBox.TextLength > 0 && swaggerBasePathTextBox.TextLength > 0;
        }

        internal void AddEventHandler(Action<object, EventArgs> validateSaveButton)
        {
            hostTextBox.TextChanged += new EventHandler(validateSaveButton);
            swaggerBasePathTextBox.TextChanged += new EventHandler(validateSaveButton);
        }

        internal void Added(Accordion accordion, List<Service> services, bool expanded)
        {
            this.services = services;
            checkbox = accordion.Add(servicePanel, Name, open: expanded);
            services.Add(this);
        }

        private void DeleteButton_Click(object sender, EventArgs e)
        {
            checkbox.Visible = false;
            services.Remove(this);
        }
    }
}
