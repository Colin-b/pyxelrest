using log4net;
using Opulos.Core.UI;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text.RegularExpressions;
using System.Windows.Forms;

namespace AutoLoadPyxelRestAddIn
{

    public partial class ServiceConfigurationForm : Form
    {
        private static readonly ILog Log = LogManager.GetLogger("ServiceConfigurationForm");

        internal static readonly string DEFAULT_SECTION = "DEFAULT";
        /// <summary>
        /// Minimum inactivity interval to wait before checking for host validity.
        /// Avoid preventing the user from typing a long url straightfully.
        /// This interval is in milliseconds.
        /// </summary>
        private static readonly int CHECK_HOST_INTERVAL_MS = 500;
        internal static readonly int CHECK_HOST_INTERVAL_TICKS = CHECK_HOST_INTERVAL_MS * 10000;
        private static readonly Regex SERVICE_NAME_UNALLOWED_CHARACTERS = new Regex("[^a-zA-Z_]+[^a-zA-Z_0-9]*");

        internal Accordion accordion;
        private ComboBox addServiceList;
        private Button addServiceButton;
        private List<ServicePanel> services = new List<ServicePanel>();
        private List<Service> upToDateServices = new List<Service>();
        private Button saveButton;
        private readonly Timer hostReachabilityTimer;
        internal readonly Configuration configuration;
        internal readonly Configuration upToDateConfiguration;

        public ServiceConfigurationForm()
        {
            hostReachabilityTimer = StartHostReachabilityTimer();
            InitializeComponent();
            FormClosed += ServiceConfigurationForm_FormClosed;
            configuration = new Configuration();
            try
            {
                LoadServices();
            }
            catch (Exception e)
            {
                Log.Error("Unable to load services.", e);
            }
            try
            {
                upToDateConfiguration = new Configuration(ThisAddIn.GetSetting("PathToUpToDateConfigurations"));
                LoadUpToDateServices();
            }
            catch (Exception e)
            {
                Log.Error("Unable to load up to date services.", e);
            }
        }

        public static void UpdateServices()
        {
            try
            {
                Configuration configuration = new Configuration();
                List<Service> configuredServices = configuration.Load();

                Configuration upToDateConfiguration = new Configuration(ThisAddIn.GetSetting("PathToUpToDateConfigurations"));
                List<Service> upToDateServices = upToDateConfiguration.Load();

                if (upToDateServices.Count > 0)
                {
                    foreach (Service service in configuredServices)
                    {
                        Service upToDateService = upToDateServices.Find(s => s.Name.Equals(service.Name));
                        if (upToDateService != null)
                            service.UpdateFrom(upToDateService);
                    }

                    configuration.Save();
                }
            }
            catch (Exception ex)
            {
                Log.Error("Unable to keep services configuration up to date.", ex);
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

        private void ServiceConfigurationForm_FormClosed(object sender, FormClosedEventArgs e)
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
            StartPosition = FormStartPosition.CenterParent;

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

            addServiceList = new ComboBox();
            addServiceList.Dock = DockStyle.Fill;
            addServiceList.AutoSize = true;
            addServiceList.TextChanged += AddServiceList_TextChanged;
            addServiceList.KeyDown += AddServiceList_KeyDown;
            newServicePanel.Controls.Add(addServiceList, 0, 0);

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

        private void AddServiceList_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addServiceButton.Enabled)
                        addServiceButton.PerformClick();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void AddServiceList_TextChanged(object sender, EventArgs e)
        {
            if (addServiceList.Text.Length > 0)
                CheckNonEmptyServiceName();
            else
                InvalidateEmptyServiceName();
        }

        private void AddServiceSection(object sender, EventArgs e)
        {
            string serviceName = addServiceList.Text;
            Service service = upToDateServices.Find(s => s.Name.Equals(serviceName));
            if (service == null)  // Service is unknown, new one
            {
                service = configuration.AddDefaultService(serviceName);
            }
            else  // Service corresponds to an up to date service 
            {
                addServiceList.Items.Remove(service);
                configuration.AddService(service);
            }
            addServiceList.Text = "";
            InvalidateEmptyServiceName();
            ServicePanel panel = new ServicePanel(this, service);
            displayService(panel, true);
        }

        private void CheckNonEmptyServiceName()
        {
            if (IsServiceNameValid())
                CheckValidatedServiceName();
            else
                InvalidateServiceName();
        }

        private bool IsServiceNameValid()
        {
            string validatedServiceName = SERVICE_NAME_UNALLOWED_CHARACTERS.Replace(addServiceList.Text, "");
            return addServiceList.Text.Equals(validatedServiceName);
        }

        private void CheckValidatedServiceName()
        {
            if (services.Exists(s => s.Exists(addServiceList.Text)))
                InvalidateDuplicatedServiceName();
            else
                ValidateServiceName();
        }

        private void InvalidateEmptyServiceName()
        {
            addServiceButton.Enabled = false;
            addServiceButton.Text = "Enter service name to create a new configuration";
            addServiceButton.BackColor = Color.LightGray;
        }

        private void InvalidateServiceName()
        {
            addServiceButton.Enabled = false;
            addServiceButton.Text = "Service name only allows alphanumeric characters";
            addServiceButton.BackColor = Color.OrangeRed;
        }

        private void InvalidateDuplicatedServiceName()
        {
            addServiceButton.Enabled = false;
            addServiceButton.Text = addServiceList.Text + " configuration already exists";
            addServiceButton.BackColor = Color.OrangeRed;
        }

        private void ValidateServiceName()
        {
            addServiceButton.Enabled = true;
            addServiceButton.Text = "Add " + addServiceList.Text + " configuration";
            addServiceButton.BackColor = Color.LightBlue;
        }

        private void LoadServices()
        {
            services.Clear();
            foreach (Service service in configuration.Load())
            {
                ServicePanel panel = new ServicePanel(this, service);
                displayService(panel, false);
            }
        }

        private void LoadUpToDateServices()
        {
            addServiceList.Items.Clear();
            upToDateServices.Clear();
            upToDateServices.AddRange(upToDateConfiguration.Load());

            foreach (Service service in upToDateServices)
            {
                ServicePanel configurationService = services.Find(s => s.Exists(service.Name));
                if (configurationService != null)
                    configurationService.UpdateFrom(service);
                else
                    addServiceList.Items.Add(service);
            }

            if (upToDateServices.Count > 0)
                configuration.Save();
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

        private void Save(object sender, EventArgs e)
        {
            try
            {
                configuration.Save();
            }
            catch (Exception ex)
            {
                Log.Error("Unable to save services.", ex);
            }
        }

        internal void Removed(ServicePanel service)
        {
            services.Remove(service);
            Service removedService = upToDateServices.Find(s => service.Exists(s.Name));
            if (removedService != null)
                addServiceList.Items.Add(removedService);
            saveButton.Enabled = IsValid();
        }

        internal void ServiceUpdated()
        {
            saveButton.Enabled = IsValid();
        }
    }
}
