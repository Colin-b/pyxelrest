using log4net;
using Microsoft.Win32;
using Opulos.Core.UI;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace PyxelRestAddIn
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
        private static readonly RegexStringValidator SERVICE_NAME_VALIDATOR = new RegexStringValidator(@"^[a-zA-Z_]+[a-zA-Z_0-9]*$");
        private static string ConfigurationFilePath = null;

        internal Accordion accordion;
        private ComboBox serviceNameField;
        private ToolTip addServiceTooltip;
        private PictureBox addServiceButton;
        private List<ServicePanel> services = new List<ServicePanel>();
        private List<Service> upToDateServices = new List<Service>();
        private readonly Timer hostReachabilityTimer;
        internal readonly Configuration configuration;
        internal readonly Configuration upToDateConfiguration;

        public ServiceConfigurationForm(string pathToUpToDateConfigurations)
        {
            hostReachabilityTimer = StartHostReachabilityTimer();
            InitializeComponent();
            FormClosed += ServiceConfigurationForm_FormClosed;
            try
            {
                configuration = new Configuration(ConfigurationFilePath);
                LoadServices();
            }
            catch (Exception e)
            {
                Log.Error("Unable to load services.", e);
            }
            try
            {
                upToDateConfiguration = new Configuration(pathToUpToDateConfigurations, false);
                LoadUpToDateServices();
            }
            catch (Exception e)
            {
                Log.Error("Unable to load up to date services.", e);
            }
        }

        internal static void UpdateServices(string pathToUpToDateConfigurations)
        {
            try
            {
                string installLocation = (string)Registry.GetValue(@"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest", "InstallLocation", null);
                ConfigurationFilePath = installLocation == null ? null : Path.Combine(installLocation, "configuration", "services.yml");
                var configuration = new Configuration(ConfigurationFilePath);
                List<Service> configuredServices = configuration.Load();

                var upToDateConfiguration = new Configuration(pathToUpToDateConfigurations, false);
                List<Service> upToDateServices = upToDateConfiguration.Load();

                if (upToDateServices.Count > 0)
                {
                    bool updated = false;

                    foreach (Service service in configuredServices)
                    {
                        Service upToDateService = upToDateServices.Find(s => s.Name.Equals(service.Name));
                        if (upToDateService != null)
                        {
                            service.UpdateFrom(upToDateService);
                            updated = true;
                        }
                    }

                    if (updated)
                    {
                        configuration.Save(ConfigurationFilePath);
                        InstallPythonModules(configuration.pythonModules);
                    }
                }
            }
            catch (Exception ex)
            {
                Log.Error("Unable to keep services configuration up to date.", ex);
            }
        }

        private static void InstallPythonModules(ISet<string> pythonModules)
        {
            if (pythonModules.Count == 0)
                return;

            string pythonPath = ThisAddIn.GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                throw new Exception(string.Format("Extra python modules cannot be installed as python cannot be found in '{0}'.", pythonPath));

            string commandLine = "-m pip install ";
            foreach (string pythonModule in pythonModules)
                commandLine += string.Format("{0} ", pythonModule);
            commandLine += "--upgrade";

            Log.Debug("Install python modules...");
            Log.Debug(pythonPath);
            Process installModules = new Process();
            installModules.StartInfo.FileName = pythonPath;
            installModules.StartInfo.Arguments = commandLine;
            installModules.StartInfo.UseShellExecute = false;
            installModules.StartInfo.CreateNoWindow = true;
            installModules.Start();
        }

        private Timer StartHostReachabilityTimer()
        {
            var timer = new Timer { Interval = CHECK_HOST_INTERVAL_MS };
            timer.Tick += HostReachabilityTimer_Tick;
            timer.Start();
            return timer;
        }

        private void ServiceConfigurationForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            hostReachabilityTimer.Stop();
            if (configuration.modified)
            {
                configuration.modified = false;
                InstallPythonModules(configuration.pythonModules);
                DialogResult = DialogResult.Yes;
            }
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

            var serviceNameTooltip = new ToolTip { ToolTipTitle = "Enter service name", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

            serviceNameField = new ComboBox { Width=480 };
            serviceNameTooltip.SetToolTip(serviceNameField, "Value should only contains alpha numeric characters, numbers or underscore but cannot start with a number. eg: my_service2");
            serviceNameField.TextChanged += ServiceNameField_TextChanged;
            serviceNameField.KeyDown += ServiceNameField_KeyDown;
            newServicePanel.Controls.Add(serviceNameField, 0, 0);

            addServiceTooltip = new ToolTip { ToolTipTitle = "Add a new service configuration", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

            addServiceButton = new AddButton(20);
            addServiceTooltip.SetToolTip(addServiceButton, "Do not forget to save once configured.");
            addServiceButton.Click += AddServiceSection;
            newServicePanel.Controls.Add(addServiceButton, 1, 0);

            layout.Controls.Add(newServicePanel);
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
            var selectedService = (Service)serviceNameField.SelectedItem;
            // Add selected drop down item instantly
            if (selectedService != null)
            {
                AddServiceSection();
            }
            // Otherwise requires a user action to make sure service name is definitive
            else
            {
                var serviceName = serviceNameField.Text;

                addServiceButton.Enabled = IsServiceNameValid(serviceName);
                if (addServiceButton.Enabled)
                {
                    addServiceTooltip.ToolTipTitle = string.Format("Add {0} service configuration", serviceName);
                }
            }
        }

        private bool IsServiceNameValid(string serviceName)
        {
            try
            {
                SERVICE_NAME_VALIDATOR.Validate(serviceName);
                return !services.Exists(s => s.Exists(serviceName));
            }
            catch (ArgumentException)
            {
                return false;
            }
        }

        private void AddServiceSection(object sender, EventArgs e)
        {
            AddServiceSection();
        }

        private void AddServiceSection()
        {
            var selectedService = (Service)serviceNameField.SelectedItem;
            if (selectedService == null)  // Allow to specify existing service by typing name instead of selecting it
                selectedService = upToDateServices.Find(service => serviceNameField.Text.Equals(service.Name));

            if (selectedService == null)  // Service is unknown, new one
            {
                selectedService = configuration.AddDefaultService(serviceNameField.Text);
            }
            else  // Service corresponds to an up to date service 
            {
                serviceNameField.Items.Remove(selectedService);
                configuration.AddService(selectedService);
            }
            serviceNameField.Text = "";
            addServiceButton.Enabled = false;
            DisplayService(new ServicePanel(this, selectedService), true);
            Save();
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

            bool updated = false;

            foreach (Service service in upToDateServices)
            {
                ServicePanel configurationService = services.Find(s => s.Exists(service.Name));
                if (configurationService != null)
                {
                    configurationService.UpdateFrom(service);
                    updated = true;
                }
                else
                    serviceNameField.Items.Add(service);
            }

            if (updated)
                Save();
        }

        private void DisplayService(ServicePanel service, bool expanded)
        {
            service.Display(expanded);
            services.Add(service);
        }

        private bool IsValid()
        {
            foreach (ServicePanel service in services)
                if (!service.IsValid())
                    return false;
            return true;
        }

        private void Save()
        {
            if (IsValid())
            {
                try
                {
                    configuration.Save(ConfigurationFilePath);
                }
                catch (Exception ex)
                {
                    Log.Error("Unable to save services.", ex);
                }
            }
        }

        internal void ServiceRemoved(ServicePanel service)
        {
            services.Remove(service);
            Service removedService = upToDateServices.Find(s => service.Exists(s.Name));
            if (removedService != null)
                serviceNameField.Items.Add(removedService);
            Save();
        }

        internal void ServiceUpdated()
        {
            Save();
        }
    }
}
