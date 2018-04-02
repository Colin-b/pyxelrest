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
        private readonly IniData config;

        public Configuration(string path)
        {
            if (string.IsNullOrEmpty(path))
            {
                Log.Warn("Configuration cannot be loaded as configuration path was not provided.");
                config = null;
            }
            else
            {
                config = LoadPath(path);
            }
        }

        public static string GetDefaultConfigFilePath()
        {
            string appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            return appDataFolder == null ? null : Path.Combine(appDataFolder, "pyxelrest", "configuration", "services.ini");
        }

        private IniData LoadPath(string path)
        {
            try
            {
                return File.GetAttributes(path).HasFlag(FileAttributes.Directory) ? LoadFolder(path) : LoadFile(path);
            }
            catch (ArgumentException)
            {
                return LoadUrl(path);
            }
        }

        private IniData LoadUrl(string fileUrl)
        {
            HttpWebResponse response = UrlChecker.ConnectTo(fileUrl, null, close: false);
            if (response == null || response.StatusCode != HttpStatusCode.OK)
            {
                string details = response == null ? "" : response.StatusDescription;
                Log.ErrorFormat("Configuration cannot be loaded from {0}: {1}.", fileUrl, details);
                return null;
            }

            Log.InfoFormat("Configuration loaded from {0}: {1}.", fileUrl, response.StatusDescription);
            var parser = new FileIniDataParser();
            return parser.ReadData(new StreamReader(response.GetResponseStream()));
        }

        private IniData LoadFile(string filePath)
        {
            var parser = new FileIniDataParser();
            return parser.ReadFile(filePath);
        }

        private IniData LoadFolder(string folderPath)
        {
            Log.Warn("Configuration cannot be loaded as configuration folder path loading is not yet implemented.");
            return null;  // TODO Add ability to load a folder content into a single ini data
        }

        public List<Service> Load()
        {
            services.Clear();
            if (config == null)
                return services;

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

        public void Save(string configurationFilePath)
        {
            if (configurationFilePath == null)
            {
                Log.Error("Configuration cannot be saved as configuration file path was not provided.");
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
