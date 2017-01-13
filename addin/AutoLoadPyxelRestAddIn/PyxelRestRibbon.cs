using System;
using Microsoft.Office.Tools.Ribbon;
using System.Windows.Forms;
using Opulos.Core.UI;
using System.Drawing;
using System.Collections.Generic;
using log4net;
using System.Net;

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
            if (DialogResult.Yes == new ServiceConfigurationFrame().ShowDialog())
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

        internal static readonly string DEFAULT_SECTION = "DEFAULT";
        /// <summary>
        /// Minimum inactivity interval to wait before checking for host validity.
        /// Avoid preventing the user from typing a long url straightfully.
        /// This interval is in milliseconds.
        /// </summary>
        private static readonly int CHECK_HOST_INTERVAL_MS = 500;
        internal static readonly int CHECK_HOST_INTERVAL_TICKS = CHECK_HOST_INTERVAL_MS * 10000;

        internal Accordion accordion;
        private TextBox newServiceName;
        private Button addServiceButton;
        private List<ServicePanel> services = new List<ServicePanel>();
        private Button saveButton;
        private readonly Timer hostReachabilityTimer;
        internal readonly Configuration configuration;

        public ServiceConfigurationFrame()
        {
            hostReachabilityTimer = StartHostReachabilityTimer();
            InitializeComponent();
            FormClosed += ServiceConfigurationFrame_FormClosed;
            configuration = new Configuration();
            try
            {
                LoadServices();
            }
            catch (Exception e)
            {
                Log.Error("Unable to load services.", e);
            }
        }

        private Timer StartHostReachabilityTimer()
        {
            Timer hostReachabilityTimer = new Timer();
            hostReachabilityTimer.Tick += HostReachabilityTimer_Tick;
            hostReachabilityTimer.Interval = CHECK_HOST_INTERVAL_MS;
            hostReachabilityTimer.Start();
            return hostReachabilityTimer;
        }

        private void ServiceConfigurationFrame_FormClosed(object sender, FormClosedEventArgs e)
        {
            hostReachabilityTimer.Stop();
        }

        private void HostReachabilityTimer_Tick(object sender, EventArgs e)
        {
            foreach (ServicePanel service in services)
                service.CheckHostReachability();
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
            newServiceName.KeyDown += NewServiceName_KeyDown;
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

        private void NewServiceName_KeyDown(object sender, KeyEventArgs e)
        {
            switch(e.KeyCode)
            {
                case Keys.Enter:
                    if (addServiceButton.Enabled)
                        addServiceButton.PerformClick();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                // As Service name will be used as UDF prefix, value should be a valid Excel one
                // This is why the following characters are forbidden
                case Keys.Space:
                    e.SuppressKeyPress = true;
                    break;
                default:
                    // Allow any other character
                    break;

            }
        }

        private void NewServiceName_TextChanged(object sender, EventArgs e)
        {
            if (newServiceName.TextLength > 0)
            {
                string newService = newServiceName.Text;
                bool alreadyExists = services.Exists(s => s.Exists(newService));
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
            foreach(Service service in configuration.Load())
            {
                ServicePanel panel = new ServicePanel(this, service);
                displayService(panel, false);
            }
        }

        private void displayService(ServicePanel service, bool expanded)
        {
            service.Display(expanded);
            services.Add(service);
            saveButton.Enabled = IsValid();
        }

        private bool IsValid()
        {
            foreach (ServicePanel service in services)
                if (!service.IsValid())
                    return false;
            return true;
        }

        private void AddServiceSection(object sender, EventArgs e)
        {
            Service newService = configuration.AddDefaultService(newServiceName.Text);
            ServicePanel panel = new ServicePanel(this, newService);
            displayService(panel, true);
            newServiceName.Text = "";
        }

        private void Save(object sender, EventArgs e)
        {
            configuration.Save();
        }

        internal void Removed(ServicePanel service)
        {
            services.Remove(service);
            saveButton.Enabled = IsValid();
        }

        internal void ServiceUpdated()
        {
            saveButton.Enabled = IsValid();
        }
    }

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

        private readonly ServiceConfigurationFrame configurationFrame;
        private long? swaggerUrlModificationTicks;

        public ServicePanel(ServiceConfigurationFrame configurationFrame, Service service)
        {
            this.configurationFrame = configurationFrame;
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
            long actualTicks = DateTime.UtcNow.Ticks;
            if (swaggerUrlModificationTicks != null && actualTicks >= swaggerUrlModificationTicks + ServiceConfigurationFrame.CHECK_HOST_INTERVAL_TICKS)
            {
                swaggerUrlTextBox.BackColor = IsSwaggerReachable() ? Color.LightGreen : Color.Red;
                swaggerUrlModificationTicks = null;
            }
        }

        internal bool Exists(string serviceName)
        {
            return service.Name.Equals(serviceName);
        }

        internal void Display(bool expanded)
        {
            checkbox = configurationFrame.accordion.Add(servicePanel, service.Name, open: expanded);
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
            configurationFrame.ServiceUpdated();
            swaggerUrlModificationTicks = DateTime.UtcNow.Ticks;
        }

        private void DeleteButton_Click(object sender, EventArgs e)
        {
            checkbox.Visible = false;
            configurationFrame.configuration.Remove(service);
            configurationFrame.Removed(this);
        }

        private bool IsSwaggerReachable()
        {
            HttpWebResponse response = ConnectTo(swaggerUrlTextBox.Text);
            return response != null && response.StatusCode == HttpStatusCode.OK;
        }

        private HttpWebResponse ConnectTo(string url)
        {
            try
            {
                Uri urlCheck = new Uri(url);
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(urlCheck);
                request.Timeout = 500;
                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                response.Close();
                return response;
            }
            catch (WebException e)
            {
                HttpWebResponse response = (HttpWebResponse)e.Response;
                if (response != null)
                    response.Close();
                return response;
            }
            catch (Exception)
            {
                return null;
            }
        }
    }
}
