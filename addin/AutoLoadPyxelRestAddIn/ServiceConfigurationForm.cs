using log4net;
using Opulos.Core.UI;
using System;
using System.Collections.Generic;
using System.Diagnostics;
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
        private ToolTip addServiceTooltip;
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
                upToDateConfiguration = new Configuration(ThisAddIn.GetSetting("PathToUpToDateConfigurations"), false);
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
                var configuration = new Configuration(configurationFilePath);
                List<Service> configuredServices = configuration.Load();

                var upToDateConfiguration = new Configuration(ThisAddIn.GetSetting("PathToUpToDateConfigurations"), false);
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
                            InstallPythonModules(service.PythonModules);
                            updated = true;
                        }
                    }

                    if (updated)
                        configuration.Save(configurationFilePath);
                }
            }
            catch (Exception ex)
            {
                Log.Error("Unable to keep services configuration up to date.", ex);
            }
        }

        private static void InstallPythonModules(IList<string> pythonModules)
        {
            if (pythonModules == null || pythonModules.Count == 0)
                return;

            string pythonPath = ThisAddIn.GetSetting("PathToPython");
            if (!File.Exists(pythonPath))
                throw new Exception(string.Format("Path to Python '{0}' cannot be found.", pythonPath));

            string commandLine = "-m pip install ";
            foreach (string pythonModule in pythonModules)
                commandLine += string.Format("{0} ", pythonModule);
            commandLine += "--upgrade";

            Log.Debug("Install python modules...");
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
            serviceNameTooltip.SetToolTip(serviceNameField, "Value should only contains alpha numeric characters. eg: my_service");
            serviceNameField.TextChanged += ServiceNameField_TextChanged;
            serviceNameField.KeyDown += ServiceNameField_KeyDown;
            newServicePanel.Controls.Add(serviceNameField, 0, 0);

            addServiceTooltip = new ToolTip { ToolTipTitle = "Add a new service configuration", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

            addServiceButton = new AddButton();
            addServiceTooltip.SetToolTip(addServiceButton, "Do not forget to save once configured.");
            addServiceButton.Click += AddServiceSection;
            newServicePanel.Controls.Add(addServiceButton, 1, 0);

            layout.Controls.Add(newServicePanel);
            #endregion

            #region Save
            {
                ToolTip tooltip = new ToolTip { ToolTipTitle = "Save modifications", UseFading = true, UseAnimation = true, IsBalloon = true, ShowAlways = true, ReshowDelay = 0 };

                saveButton = new Button { Enabled = false, DialogResult = DialogResult.Yes, Dock = DockStyle.Fill, Text = "Save Configuration" };
                tooltip.SetToolTip(saveButton, "User defined functions will be automatically reloaded.");
                saveButton.Click += Save;
                layout.Controls.Add(saveButton);
            }
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
            var serviceName = selectedService == null ? serviceNameField.Text : selectedService.Name;

            addServiceButton.Enabled = IsServiceNameValid(serviceName);
            if (addServiceButton.Enabled)
            {
                addServiceTooltip.ToolTipTitle = string.Format("Add {0} service configuration", serviceName);
            }
        }

        private bool IsServiceNameValid(string serviceName)
        {
            string validatedServiceName = SERVICE_NAME_UNALLOWED_CHARACTERS.Replace(serviceName, "");
            return serviceName.Length > 0 && serviceName.Equals(validatedServiceName) && !services.Exists(s => s.Exists(serviceName));
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
                configuration.Save(configurationFilePath);
        }

        private void DisplayService(ServicePanel service, bool expanded)
        {
            service.Display(expanded);
            services.Add(service);
            UpdateSaveButtonState();
        }

        private void UpdateSaveButtonState()
        {
            if (IsValid())
            {
                saveButton.Enabled = true;
                saveButton.ForeColor = Color.DarkGreen;
                saveButton.BackColor = Color.LightGreen;
            }
            else
            {
                saveButton.Enabled = false;
                saveButton.ForeColor = Color.Black;
                saveButton.BackColor = Color.FromArgb(255, 240, 240, 240);
            }
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
                foreach (ServicePanel service in services)
                    InstallPythonModules(service.service.PythonModules);
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
            UpdateSaveButtonState();
        }

        internal void ServiceUpdated()
        {
            UpdateSaveButtonState();
        }
    }
}
