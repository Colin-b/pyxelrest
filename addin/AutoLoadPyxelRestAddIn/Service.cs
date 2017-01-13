using IniParser.Model;
using log4net;
using System;
using System.Text;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class Service
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private static readonly string SWAGGER_URL_PROPERTY = "swagger_url";
        private static readonly string PROXY_URL_PROPERTY = "proxy_url";
        private static readonly string METHODS_PROPERTY = "methods";

        private static readonly string GET = "get";
        private static readonly string POST = "post";
        private static readonly string PUT = "put";
        private static readonly string DELETE = "delete";

        internal readonly string Name;
        public string SwaggerUrl;
        public string ProxyUrl;
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
            ProxyUrl = serviceConfig.ContainsKey(PROXY_URL_PROPERTY) ? serviceConfig[PROXY_URL_PROPERTY] : DefaultProxyUrl(defaultConfig);
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

            if(!string.IsNullOrEmpty(ProxyUrl)) {
                KeyData proxyUrl = new KeyData(PROXY_URL_PROPERTY);
                proxyUrl.Value = this.ProxyUrl;
                section.Keys.SetKeyData(proxyUrl);
            }

            KeyData methods = new KeyData(METHODS_PROPERTY);
            methods.Value = GetMethods();
            section.Keys.SetKeyData(methods);

            return section;
        }

        internal void Default()
        {
            SwaggerUrl = "";
            ProxyUrl = "";
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

        private string DefaultProxyUrl(KeyDataCollection defaultConfig)
        {
            if (defaultConfig == null || !defaultConfig.ContainsKey(PROXY_URL_PROPERTY))
                return string.Empty;
            return defaultConfig[PROXY_URL_PROPERTY];
        }
    }
}
