﻿using IniParser.Model;
using log4net;
using System;
using System.Globalization;
using System.Text;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class Service
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private static readonly string SWAGGER_URL_PROPERTY = "swagger_url";
        private static readonly string PROXY_URL_PROPERTY = "proxy_url";
        private static readonly string SERVICE_HOST_PROPERTY = "service_host";
        private static readonly string METHODS_PROPERTY = "methods";
        private static readonly string TAGS_PROPERTY = "tags";
        private static readonly string CONNECT_TIMEOUT_PROPERTY = "connect_timeout";
        private static readonly string READ_TIMEOUT_PROPERTY = "read_timeout";
        private static readonly string SECURITY_DETAILS_PROPERTY = "security_details";
        private static readonly string ADVANCED_CONFIGURATION_PROPERTY = "advanced_configuration";

        private static readonly string GET = "get";
        private static readonly string POST = "post";
        private static readonly string PUT = "put";
        private static readonly string DELETE = "delete";

        internal readonly string Name;
        public string SwaggerUrl;
        public string ProxyUrl;
        public string ServiceHost;
        public bool Get;
        public bool Post;
        public bool Put;
        public bool Delete;
        public string Tags;
        public float? ConnectTimeout;
        public float? ReadTimeout;
        public string SecurityDetails;
        public string AdvancedConfiguration;

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
            ProxyUrl = serviceConfig.ContainsKey(PROXY_URL_PROPERTY) ? serviceConfig[PROXY_URL_PROPERTY] : DefaultProxyUrl(defaultConfig);
            ServiceHost = serviceConfig.ContainsKey(SERVICE_HOST_PROPERTY) ? serviceConfig[SERVICE_HOST_PROPERTY] : string.Empty;
            string[] methods = serviceConfig.ContainsKey(METHODS_PROPERTY) ? serviceConfig[METHODS_PROPERTY].Split(',') : DefaultMethods(defaultConfig);
            for (int i = 0; i < methods.Length; i++)
                methods[i] = methods[i].Trim();
            Get = Array.Exists(methods, s => GET.Equals(s));
            Post = Array.Exists(methods, s => POST.Equals(s));
            Put = Array.Exists(methods, s => PUT.Equals(s));
            Delete = Array.Exists(methods, s => DELETE.Equals(s));
            Tags = serviceConfig.ContainsKey(TAGS_PROPERTY) ? serviceConfig[TAGS_PROPERTY] : string.Empty;
            ConnectTimeout = GetFloatProperty(serviceConfig, CONNECT_TIMEOUT_PROPERTY, 1);
            ReadTimeout = GetFloatProperty(serviceConfig, READ_TIMEOUT_PROPERTY, null);
            SecurityDetails = serviceConfig.ContainsKey(SECURITY_DETAILS_PROPERTY) ? serviceConfig[SECURITY_DETAILS_PROPERTY] : string.Empty;
            AdvancedConfiguration = serviceConfig.ContainsKey(ADVANCED_CONFIGURATION_PROPERTY) ? serviceConfig[ADVANCED_CONFIGURATION_PROPERTY] : string.Empty;
        }

        private float? GetFloatProperty(KeyDataCollection serviceConfig, string property, float? defaultValue)
        {
            if (serviceConfig.ContainsKey(property))
            {
                float parsed;
                if (float.TryParse(serviceConfig[property], NumberStyles.AllowDecimalPoint, CultureInfo.InvariantCulture, out parsed))
                    return parsed;
            }
            return defaultValue;
        }

        internal SectionData ToConfig()
        {
            SectionData section = new SectionData(Name);
            section.Keys = new KeyDataCollection();

            KeyData swaggerUrl = new KeyData(SWAGGER_URL_PROPERTY);
            swaggerUrl.Value = SwaggerUrl;
            section.Keys.SetKeyData(swaggerUrl);

            if(!string.IsNullOrEmpty(ProxyUrl)) {
                KeyData proxyUrl = new KeyData(PROXY_URL_PROPERTY);
                proxyUrl.Value = ProxyUrl;
                section.Keys.SetKeyData(proxyUrl);
            }

            if (!string.IsNullOrEmpty(ServiceHost))
            {
                KeyData serviceHost = new KeyData(SERVICE_HOST_PROPERTY);
                serviceHost.Value = ServiceHost;
                section.Keys.SetKeyData(serviceHost);
            }

            KeyData methods = new KeyData(METHODS_PROPERTY);
            methods.Value = GetMethods();
            section.Keys.SetKeyData(methods);

            if (!string.IsNullOrEmpty(Tags))
            {
                KeyData tags = new KeyData(TAGS_PROPERTY);
                tags.Value = Tags;
                section.Keys.SetKeyData(tags);
            }

            if (ConnectTimeout.HasValue)
            {
                KeyData connectTimeout = new KeyData(CONNECT_TIMEOUT_PROPERTY);
                connectTimeout.Value = ConnectTimeout.Value.ToString(CultureInfo.InvariantCulture);
                section.Keys.SetKeyData(connectTimeout);
            }

            if (ReadTimeout.HasValue)
            {
                KeyData readTimeout = new KeyData(READ_TIMEOUT_PROPERTY);
                readTimeout.Value = ReadTimeout.Value.ToString(CultureInfo.InvariantCulture);
                section.Keys.SetKeyData(readTimeout);
            }

            if (!string.IsNullOrEmpty(SecurityDetails))
            {
                KeyData securityDetails = new KeyData(SECURITY_DETAILS_PROPERTY);
                securityDetails.Value = SecurityDetails;
                section.Keys.SetKeyData(securityDetails);
            }

            if (!string.IsNullOrEmpty(AdvancedConfiguration))
            {
                KeyData advancedConfiguration = new KeyData(ADVANCED_CONFIGURATION_PROPERTY);
                advancedConfiguration.Value = AdvancedConfiguration;
                section.Keys.SetKeyData(advancedConfiguration);
            }

            return section;
        }

        internal void Default()
        {
            SwaggerUrl = "";
            ProxyUrl = "";
            ServiceHost = "";
            Get = true;
            Post = true;
            Put = true;
            Delete = true;
            Tags = "";
            ConnectTimeout = 1;
            ReadTimeout = null;
            SecurityDetails = "";
            AdvancedConfiguration = "";
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

        private string DefaultProxyUrl(KeyDataCollection defaultConfig)
        {
            if (defaultConfig == null || !defaultConfig.ContainsKey(PROXY_URL_PROPERTY))
                return string.Empty;
            return defaultConfig[PROXY_URL_PROPERTY];
        }
    }
}
