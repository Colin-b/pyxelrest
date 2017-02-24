using IniParser;
using IniParser.Model;
using log4net;
using System;
using System.Collections.Generic;

namespace AutoLoadPyxelRestAddIn
{
    class Configuration
    {
        private static readonly ILog Log = LogManager.GetLogger("Configuration");

        internal static readonly string DEFAULT_SECTION = "DEFAULT";

        private readonly List<Service> services = new List<Service>();

        public List<Service> Load()
        {
            var parser = new FileIniDataParser();
            string configurationFilePath = GetConfigurationFilePath();
            if (configurationFilePath == null)
            {
                Log.Error("Configuration cannot be loaded as configuration file path cannot be found.");
                return services;
            }

            IniData config = parser.ReadFile(configurationFilePath);

            foreach (var section in config.Sections)
            {
                if (DEFAULT_SECTION.Equals(section.SectionName))
                    continue;
                try
                {
                    Service service = AddService(section.SectionName);
                    service.FromConfig(config);
                }
                catch (Exception e)
                {
                    Log.Error(string.Format("Unable to load '{0}' service configuration", section.SectionName), e);
                }
            }
            return services;
        }

        public void Save()
        {
            var parser = new FileIniDataParser();
            string configurationFilePath = GetConfigurationFilePath();
            if (configurationFilePath == null)
            {
                Log.Error("Configuration cannot be saved as configuration file path cannot be found.");
                return;
            }
            IniData config = parser.ReadFile(configurationFilePath);

            config.Sections.Clear();
            foreach (Service service in services)
                config.Sections.Add(service.ToConfig());
            parser.WriteFile(configurationFilePath, config);
            Log.Info("Services configuration updated.");
        }

        internal Service AddDefaultService(string name)
        {
            Service service = AddService(name);
            service.Default();
            Log.InfoFormat("Adding new configuration for '{0}' service.", service);
            return service;
        }

        private Service AddService(string name)
        {
            Service service = new Service(name);
            services.Add(service);
            return service;
        }

        private string GetConfigurationFilePath()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if (appDataFolder != null)
                return System.IO.Path.Combine(appDataFolder, "pyxelrest", "configuration", "services.ini");
            return null;
        }

        internal void Remove(Service service)
        {
            Log.InfoFormat("Removing '{0}' service configuration.", service);
            services.Remove(service);
        }
    }
}
