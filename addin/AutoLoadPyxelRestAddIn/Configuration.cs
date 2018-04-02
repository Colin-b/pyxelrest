using IniParser;
using IniParser.Model;
using log4net;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;

namespace AutoLoadPyxelRestAddIn
{
    class Configuration
    {
        private static readonly ILog Log = LogManager.GetLogger("Configuration");

        internal static readonly string DEFAULT_SECTION = "DEFAULT";

        private readonly List<Service> services = new List<Service>();

        private readonly string configurationFilePath;
        private readonly IniData iniConfiguration;

        public Configuration()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            configurationFilePath = (appDataFolder != null) ? System.IO.Path.Combine(appDataFolder, "pyxelrest", "configuration", "services.ini") : null;
        }

        public Configuration(string filePath)
        {
            if (string.IsNullOrEmpty(filePath))
                configurationFilePath = null;
            else
            {
                try
                {
                    FileAttributes attributes = File.GetAttributes(filePath);
                    if (attributes.HasFlag(FileAttributes.Directory)) // Directory
                    {
                        // TODO 
                    }
                    else // File
                    {
                        var parser = new FileIniDataParser();
                        iniConfiguration = parser.ReadFile(filePath);
                    }
                }
                catch (ArgumentException) // URL
                {
                    HttpWebResponse response = UrlChecker.ConnectTo(filePath, null, close: false);
                    if (response == null || response.StatusCode != HttpStatusCode.OK)
                    {
                        string details = response == null ? "" : response.StatusDescription;
                        Log.ErrorFormat("Configuration cannot be loaded from {0}: {1}.", filePath, details);
                        iniConfiguration = null;
                    }
                    else
                    {
                        Log.InfoFormat("Configuration loaded from {0}: {1}.", filePath, response.StatusDescription);
                        var parser = new FileIniDataParser();
                        iniConfiguration = parser.ReadData(new StreamReader(response.GetResponseStream()));
                    }
                }
            }
        }

        private IniData LoadFile(string filePath)
        {
            var parser = new FileIniDataParser();
            return parser.ReadFile(filePath);
        }

        public List<Service> Load()
        {
            services.Clear();
            if (configurationFilePath == null && iniConfiguration == null)
            {
                Log.Error("Configuration cannot be loaded as configuration file path cannot be found.");
                return services;
            }

            IniData config = configurationFilePath == null ? iniConfiguration : LoadFile(configurationFilePath);

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
            if (configurationFilePath == null)
            {
                Log.Error("Configuration cannot be saved as configuration file path cannot be found.");
                return;
            }

            var parser = new FileIniDataParser();
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

        internal void AddService(Service service)
        {
            services.Add(service);
        }

        internal void Remove(Service service)
        {
            Log.InfoFormat("Removing '{0}' service configuration.", service);
            services.Remove(service);
        }
    }
}
