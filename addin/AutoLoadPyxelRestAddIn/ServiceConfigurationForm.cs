using log4net;
using Opulos.Core.UI;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
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
        private ComboBox serviceNameField;
        private PictureBox addServiceButton;
        private List<ServicePanel> services = new List<ServicePanel>();
        private List<Service> upToDateServices = new List<Service>();
        private Button saveButton;
        private readonly Timer hostReachabilityTimer;
        private readonly string configurationFilePath;
        internal readonly Configuration configuration;
        internal readonly Configuration upToDateConfiguration;

        public ServiceConfigurationForm()
        {
            hostReachabilityTimer = StartHostReachabilityTimer();
            InitializeComponent();
            FormClosed += ServiceConfigurationForm_FormClosed;
            try
            {
                configurationFilePath = Configuration.GetDefaultConfigFilePath();
                configuration = new Configuration(configurationFilePath);
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

        internal static void UpdateServices()
        {
            try
            {
                string configurationFilePath = Configuration.GetDefaultConfigFilePath();
                Configuration configuration = new Configuration(configurationFilePath);
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

                    configuration.Save(configurationFilePath);
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

            var layout = new TableLayoutPanel { AutoSize = true };

            #region Services
            accordion = new Accordion { CheckBoxMargin = new Padding(2), ContentMargin = new Padding(15, 5, 15, 5), ContentPadding = new Padding(1), Insets = new Padding(5), ControlBackColor = Color.Transparent, ContentBackColor = Color.Transparent, AutoSize = true };
            layout.Controls.Add(accordion);
            #endregion

            #region New Service
            var newServicePanel = new TableLayoutPanel { Width=520, Height=30 };

            serviceNameField = new ComboBox { Width=480 };
            serviceNameField.TextChanged += ServiceNameField_TextChanged;
            serviceNameField.KeyDown += ServiceNameField_KeyDown;
            newServicePanel.Controls.Add(serviceNameField, 0, 0);

            addServiceButton = new AddButton();
            addServiceButton.Click += AddServiceSection;
            newServicePanel.Controls.Add(addServiceButton, 1, 0);

            layout.Controls.Add(newServicePanel);
            #endregion

            #region Save
            saveButton = new Button { ForeColor = Color.DarkGreen, BackColor = Color.LightGreen, DialogResult = DialogResult.Yes, Dock = DockStyle.Fill, Text = "Save Configuration" };
            saveButton.Click += Save;
            layout.Controls.Add(saveButton);
            #endregion

            Controls.Add(layout);
        }

        private void ServiceNameField_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addServiceButton.Enabled)
                        AddServiceSection();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
                    break;
                default:
                    // Allow all other characters
                    break;
            }
        }

        private void ServiceNameField_TextChanged(object sender, EventArgs e)
        {
            addServiceButton.Enabled = IsServiceNameValid();
        }

        private bool IsServiceNameValid()
        {
            string validatedServiceName = SERVICE_NAME_UNALLOWED_CHARACTERS.Replace(serviceNameField.Text, "");
            return serviceNameField.Text.Length > 0 && serviceNameField.Text.Equals(validatedServiceName) && !services.Exists(s => s.Exists(serviceNameField.Text));
        }

        private void AddServiceSection(object sender, EventArgs e)
        {
            AddServiceSection();
        }

        private void AddServiceSection()
        {
            string serviceName = serviceNameField.Text;
            Service service = upToDateServices.Find(s => s.Name.Equals(serviceName));
            if (service == null)  // Service is unknown, new one
            {
                service = configuration.AddDefaultService(serviceName);
            }
            else  // Service corresponds to an up to date service 
            {
                serviceNameField.Items.Remove(service);
                configuration.AddService(service);
            }
            serviceNameField.Text = "";
            addServiceButton.Enabled = false;
            ServicePanel panel = new ServicePanel(this, service);
            DisplayService(panel, true);

        }

        private void LoadServices()
        {
            services.Clear();
            foreach (Service service in configuration.Load())
            {
                ServicePanel panel = new ServicePanel(this, service);
                DisplayService(panel, false);
            }
        }

        private void LoadUpToDateServices()
        {
            serviceNameField.Items.Clear();
            upToDateServices.Clear();
            upToDateServices.AddRange(upToDateConfiguration.Load());

            foreach (Service service in upToDateServices)
            {
                ServicePanel configurationService = services.Find(s => s.Exists(service.Name));
                if (configurationService != null)
                    configurationService.UpdateFrom(service);
                else
                    serviceNameField.Items.Add(service);
            }

            if (upToDateServices.Count > 0)
                configuration.Save(configurationFilePath);
        }

        private void DisplayService(ServicePanel service, bool expanded)
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
                configuration.Save(configurationFilePath);
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
                serviceNameField.Items.Add(removedService);
            saveButton.Enabled = IsValid();
        }

        internal void ServiceUpdated()
        {
            saveButton.Enabled = IsValid();
        }
    }
}
