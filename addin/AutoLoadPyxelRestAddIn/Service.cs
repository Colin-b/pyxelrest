using log4net;
using System;
using System.Text;
using YamlDotNet.RepresentationModel;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class Service
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private static readonly string SWAGGER_URL_PROPERTY = "swagger_url";
        private static readonly string PROXIES_PROPERTY = "proxies";
        private static readonly string SERVICE_HOST_PROPERTY = "service_host";
        private static readonly string METHODS_PROPERTY = "methods";
        private static readonly string OAUTH2_PROPERTY = "oauth2";
        private static readonly string API_KEY_PROPERTY = "api_key";
        private static readonly string BASIC_PROPERTY = "basic";
        private static readonly string NTLM_PROPERTY = "ntlm";
        private static readonly string UDF_RETURN_TYPES_PROPERTY = "udf_return_types";
        private static readonly string RELY_ON_DEFINITIONS_PROPERTY = "rely_on_definitions";
        private static readonly string MAX_RETRIES_PROPERTY = "max_retries";
        private static readonly string HEADERS_PROPERTY = "headers";
        private static readonly string CONNECT_TIMEOUT_PROPERTY = "connect_timeout";
        private static readonly string READ_TIMEOUT_PROPERTY = "read_timeout";
        private static readonly string SWAGGER_READ_TIMEOUT_PROPERTY = "swagger_read_timeout";
        private static readonly string TAGS_PROPERTY = "tags";

        private static readonly string GET = "get";
        private static readonly string POST = "post";
        private static readonly string PUT = "put";
        private static readonly string DELETE = "delete";
        private static readonly string PATCH = "patch";
        private static readonly string OPTIONS = "options";
        private static readonly string HEAD = "head";

        private static readonly string SYNCHRONOUS = "synchronous";
        private static readonly string ASYNCHRONOUS = "asynchronous";

        internal readonly string Name;
        public string SwaggerUrl;
        public string Proxies;
        public string ServiceHost;

        public bool Get;
        public bool Post;
        public bool Put;
        public bool Delete;
        public bool Patch;
        public bool Options;
        public bool Head;

        public string OAuth2;
        public string ApiKey;
        public string Basic;
        public string Ntlm;

        public bool Synchronous;
        public bool Asynchronous;

        public bool RelyOnDefinitions;
        public int MaxRetries;
        public string Headers;
        public float ConnectTimeout;
        public float? ReadTimeout;
        public float SwaggerReadTimeout;
        public string Tags;

        public Service(string name)
        {
            Name = name;
        }

        internal void UpdateFrom(Service updated)
        {
            SwaggerUrl = updated.SwaggerUrl;
            Proxies = updated.Proxies;
            ServiceHost = updated.ServiceHost;

            Get = updated.Get;
            Post = updated.Post;
            Put = updated.Put;
            Delete = updated.Delete;
            Patch = updated.Patch;
            Options = updated.Options;
            Head = updated.Head;

            OAuth2 = updated.OAuth2;
            ApiKey = updated.ApiKey;
            Basic = updated.Basic;
            Ntlm = updated.Ntlm;

            Synchronous = updated.Synchronous;
            Asynchronous = updated.Asynchronous;

            RelyOnDefinitions = updated.RelyOnDefinitions;
            MaxRetries = updated.MaxRetries;
            Headers = updated.Headers;
            ConnectTimeout = updated.ConnectTimeout;
            ReadTimeout = updated.ReadTimeout;
            SwaggerReadTimeout = updated.SwaggerReadTimeout;
            Tags = updated.Tags;
        }

        public override string ToString()
        {
            return Name;
        }

        private YamlNode GetProperty(YamlMappingNode parent, string name)
        {
            return parent.Children[new YamlScalarNode(name)];
        }

        internal void FromConfig(YamlMappingNode section)
        {
            YamlScalarNode swaggerUrl = (YamlScalarNode) GetProperty(section, SWAGGER_URL_PROPERTY);
            SwaggerUrl = swaggerUrl == null ? string.Empty : swaggerUrl.Value;

            YamlMappingNode proxies = (YamlMappingNode)GetProperty(section, PROXIES_PROPERTY);
            Proxies = proxies == null ? string.Empty : string.Empty;

            YamlScalarNode serviceHost = (YamlScalarNode)GetProperty(section, SERVICE_HOST_PROPERTY);
            ServiceHost = serviceHost == null ? string.Empty : serviceHost.Value;

            YamlSequenceNode methodsNode = (YamlSequenceNode)GetProperty(section, METHODS_PROPERTY);
            string[] methods = methodsNode == null ? DefaultMethods() : new string[0];
            Get = Array.Exists(methods, s => GET.Equals(s));
            Post = Array.Exists(methods, s => POST.Equals(s));
            Put = Array.Exists(methods, s => PUT.Equals(s));
            Delete = Array.Exists(methods, s => DELETE.Equals(s));
            Patch = Array.Exists(methods, s => PATCH.Equals(s));
            Options = Array.Exists(methods, s => OPTIONS.Equals(s));
            Head = Array.Exists(methods, s => HEAD.Equals(s));

            YamlMappingNode oauth2 = (YamlMappingNode)GetProperty(section, OAUTH2_PROPERTY);
            OAuth2 = oauth2 == null ? string.Empty : string.Empty;

            YamlScalarNode apiKey = (YamlScalarNode)GetProperty(section, API_KEY_PROPERTY);
            ApiKey = apiKey == null ? string.Empty : swaggerUrl.Value;

            YamlMappingNode basic = (YamlMappingNode)GetProperty(section, BASIC_PROPERTY);
            Basic = basic == null ? string.Empty : string.Empty;

            YamlMappingNode ntlm = (YamlMappingNode)GetProperty(section, NTLM_PROPERTY);
            Ntlm = ntlm == null ? string.Empty : string.Empty;

            YamlSequenceNode udfReturnTypesNode = (YamlSequenceNode)GetProperty(section, UDF_RETURN_TYPES_PROPERTY);
            string[] udfReturnTypes = udfReturnTypesNode == null ? DefaultUdfReturnTypes() : new string[0];
            Synchronous = Array.Exists(udfReturnTypes, s => SYNCHRONOUS.Equals(s));
            Asynchronous = Array.Exists(udfReturnTypes, s => ASYNCHRONOUS.Equals(s));
            
            YamlScalarNode relyOnDefinitions = (YamlScalarNode)GetProperty(section, RELY_ON_DEFINITIONS_PROPERTY);
            RelyOnDefinitions = relyOnDefinitions == null ? false : bool.Parse(relyOnDefinitions.Value);

            YamlScalarNode maxRetries = (YamlScalarNode)GetProperty(section, MAX_RETRIES_PROPERTY);
            MaxRetries = maxRetries == null ? 5 : int.Parse(maxRetries.Value);

            YamlMappingNode headers = (YamlMappingNode)GetProperty(section, HEADERS_PROPERTY);
            Headers = headers == null ? string.Empty : string.Empty;

            YamlScalarNode connectTimeout = (YamlScalarNode)GetProperty(section, CONNECT_TIMEOUT_PROPERTY);
            ConnectTimeout = connectTimeout == null ? 1 : float.Parse(connectTimeout.Value);

            YamlScalarNode readTimeout = (YamlScalarNode)GetProperty(section, READ_TIMEOUT_PROPERTY);
            ReadTimeout = readTimeout == null ? (float?)null : float.Parse(readTimeout.Value);

            YamlScalarNode swaggerReadTimeout = (YamlScalarNode)GetProperty(section, SWAGGER_READ_TIMEOUT_PROPERTY);
            SwaggerReadTimeout = swaggerReadTimeout == null ? 5 : float.Parse(swaggerReadTimeout.Value);

            YamlSequenceNode tags = (YamlSequenceNode)GetProperty(section, TAGS_PROPERTY);
            Tags = tags == null ? string.Empty : string.Empty;
        }

        internal YamlMappingNode ToConfig()
        {
            YamlMappingNode section = new YamlMappingNode();

            if (!string.IsNullOrEmpty(SwaggerUrl))
                section.Add(new YamlScalarNode(SWAGGER_URL_PROPERTY), new YamlScalarNode(SwaggerUrl));

            if (!string.IsNullOrEmpty(Proxies))
                section.Add(new YamlScalarNode(PROXIES_PROPERTY), new YamlMappingNode(Proxies));

            if (!string.IsNullOrEmpty(ServiceHost))
                section.Add(new YamlScalarNode(SERVICE_HOST_PROPERTY), new YamlScalarNode(ServiceHost));

            section.Add(new YamlScalarNode(METHODS_PROPERTY), new YamlSequenceNode(GetMethods()));

            if (!string.IsNullOrEmpty(OAuth2))
                section.Add(new YamlScalarNode(OAUTH2_PROPERTY), new YamlMappingNode(OAuth2));

            if (!string.IsNullOrEmpty(ApiKey))
                section.Add(new YamlScalarNode(API_KEY_PROPERTY), new YamlScalarNode(ApiKey));

            if (!string.IsNullOrEmpty(Basic))
                section.Add(new YamlScalarNode(BASIC_PROPERTY), new YamlMappingNode(Basic));

            if (!string.IsNullOrEmpty(Ntlm))
                section.Add(new YamlScalarNode(NTLM_PROPERTY), new YamlMappingNode(Ntlm));

            section.Add(new YamlScalarNode(UDF_RETURN_TYPES_PROPERTY), new YamlSequenceNode(GetUdfReturnTypes()));

            section.Add(new YamlScalarNode(RELY_ON_DEFINITIONS_PROPERTY), new YamlScalarNode(RelyOnDefinitions.ToString()));

            section.Add(new YamlScalarNode(MAX_RETRIES_PROPERTY), new YamlScalarNode(MaxRetries.ToString()));

            if (!string.IsNullOrEmpty(Headers))
                section.Add(new YamlScalarNode(HEADERS_PROPERTY), new YamlMappingNode(Headers));

            section.Add(new YamlScalarNode(CONNECT_TIMEOUT_PROPERTY), new YamlScalarNode(ConnectTimeout.ToString()));

            if (ReadTimeout.HasValue)
                section.Add(new YamlScalarNode(READ_TIMEOUT_PROPERTY), new YamlScalarNode(ReadTimeout.Value.ToString()));

            section.Add(new YamlScalarNode(SWAGGER_READ_TIMEOUT_PROPERTY), new YamlScalarNode(SwaggerReadTimeout.ToString()));

            if (!string.IsNullOrEmpty(Tags))
                section.Add(new YamlScalarNode(TAGS_PROPERTY), new YamlSequenceNode(Tags));

            return section;
        }

        internal void Default()
        {
            SwaggerUrl = "";
            Proxies = "";
            ServiceHost = "";

            Get = true;
            Post = true;
            Put = true;
            Delete = true;
            Patch = true;
            Options = true;
            Head = true;

            OAuth2 = "";
            ApiKey = "";
            Basic = "";
            Ntlm = "";

            Synchronous = false;
            Asynchronous = true;

            RelyOnDefinitions = false;
            MaxRetries = 5;
            Headers = "";
            ConnectTimeout = 1;
            ReadTimeout = null;
            SwaggerReadTimeout = 5;
            Tags = "";
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
            if (Patch)
                AppendMethod(sb, PATCH);
            if (Options)
                AppendMethod(sb, OPTIONS);
            if (Head)
                AppendMethod(sb, HEAD);
            return sb.ToString();
        }

        private string GetUdfReturnTypes()
        {
            StringBuilder sb = new StringBuilder();
            if (Synchronous)
                sb.Append(SYNCHRONOUS);
            if (Asynchronous)
                AppendMethod(sb, ASYNCHRONOUS);
            return sb.ToString();
        }

        private void AppendMethod(StringBuilder sb, string method)
        {
            if (sb.Length > 0)
                sb.Append(", ");
            sb.Append(method);
        }

        private string[] DefaultMethods()
        {
            return new string[] { GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD };
        }

        private string[] DefaultUdfReturnTypes()
        {
            return new string[] { ASYNCHRONOUS };
        }
    }
}
