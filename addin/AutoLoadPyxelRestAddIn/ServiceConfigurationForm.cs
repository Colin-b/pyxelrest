using log4net;
using Opulos.Core.UI;
using System;
using System.Collections.Generic;
using System.Drawing;
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

        internal Accordion accordion;
        private TextBox newServiceName;
        private Button addServiceButton;
        private List<ServicePanel> services = new List<ServicePanel>();
        private Button saveButton;
        private readonly Timer hostReachabilityTimer;
        internal readonly Configuration configuration;

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
            switch (e.KeyCode)
            {
                case Keys.Enter:
                    if (addServiceButton.Enabled)
                        addServiceButton.PerformClick();
                    e.SuppressKeyPress = true; // Avoid trying to input "enter" (resulting in a failure sound on windows)
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
            foreach (Service service in configuration.Load())
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
}
