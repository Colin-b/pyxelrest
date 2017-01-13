using IniParser;
using IniParser.Model;
using log4net;
using System;
using System.Collections.Generic;
using System.Text;

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
                return System.IO.Path.Combine(appDataFolder, "pyxelrest", "configuration.ini");
            return null;
        }

        internal void Remove(Service service)
        {
            Log.InfoFormat("Removing '{0}' service configuration.", service);
            services.Remove(service);
        }
    }

    public sealed class Service
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private static readonly string SWAGGER_URL_PROPERTY = "swagger_url";
        private static readonly string METHODS_PROPERTY = "methods";

        private static readonly string GET = "get";
        private static readonly string POST = "post";
        private static readonly string PUT = "put";
        private static readonly string DELETE = "delete";

        internal readonly string Name;
        public string SwaggerUrl;
        public bool Get;
        public bool Post;
        public bool Put;
        public bool Delete;

        public Service(string name)
        {
            Name = name;
        }

        public override string ToString()
        {
            return Name;
        }

        internal void FromConfig(IniData config)
        {
            KeyDataCollection serviceConfig = config[Name];
            KeyDataCollection defaultConfig = config[Configuration.DEFAULT_SECTION];
            SwaggerUrl = serviceConfig[SWAGGER_URL_PROPERTY];
            string[] methods = serviceConfig.ContainsKey(METHODS_PROPERTY) ? serviceConfig[METHODS_PROPERTY].Split(',') : DefaultMethods(defaultConfig);
            for (int i = 0; i < methods.Length; i++)
                methods[i] = methods[i].Trim();
            Get = Array.Exists(methods, s => GET.Equals(s));
            Post = Array.Exists(methods, s => POST.Equals(s));
            Put = Array.Exists(methods, s => PUT.Equals(s));
            Delete = Array.Exists(methods, s => DELETE.Equals(s));
        }

        internal SectionData ToConfig()
        {
            SectionData section = new SectionData(Name);
            section.Keys = new KeyDataCollection();

            KeyData swaggerUrl = new KeyData(SWAGGER_URL_PROPERTY);
            swaggerUrl.Value = this.SwaggerUrl;
            section.Keys.SetKeyData(swaggerUrl);

            KeyData methods = new KeyData(METHODS_PROPERTY);
            methods.Value = GetMethods();
            section.Keys.SetKeyData(methods);

            return section;
        }

        internal void Default()
        {
            SwaggerUrl = "";
            Get = true;
            Post = true;
            Put = true;
            Delete = true;
        }

        private string GetMethods()
        {
            StringBuilder sb = new StringBuilder();
            if (Get)
                sb.Append(GET);
            if (Post)
                AppendMethod(sb, POST);
            if (Put)
                AppendMethod(sb, PUT);
            if (Delete)
                AppendMethod(sb, DELETE);
            return sb.ToString();
        }

        private void AppendMethod(StringBuilder sb, string method)
        {
            if (sb.Length > 0)
                sb.Append(", ");
            sb.Append(method);
        }

        private string[] DefaultMethods(KeyDataCollection defaultConfig)
        {
            if (defaultConfig == null || !defaultConfig.ContainsKey(METHODS_PROPERTY))
                return new string[0];
            return defaultConfig[METHODS_PROPERTY].Split(',');
        }
    }
}
