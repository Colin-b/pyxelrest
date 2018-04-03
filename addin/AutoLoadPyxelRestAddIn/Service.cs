using log4net;
using System;
using System.Collections.Generic;
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
        public IDictionary<string, string> Proxies;
        public string ServiceHost;

        public bool Get;
        public bool Post;
        public bool Put;
        public bool Delete;
        public bool Patch;
        public bool Options;
        public bool Head;

        public IDictionary<string, string> OAuth2;
        public string ApiKey;
        public IDictionary<string, string> Basic;
        public IDictionary<string, string> Ntlm;

        public bool Synchronous;
        public bool Asynchronous;

        public bool RelyOnDefinitions;
        public int MaxRetries;
        public IDictionary<string, string> Headers;
        public float ConnectTimeout;
        public float? ReadTimeout;
        public float SwaggerReadTimeout;
        public IList<string> Tags;

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
            YamlNode value;
            if (parent.Children.TryGetValue(new YamlScalarNode(name), out value))
                return value;
            return null;
        }

        private IDictionary<string, string> ToDict(YamlMappingNode node)
        {
            Dictionary<string, string> dict = new Dictionary<string, string>();
            foreach(var item in node.Children)
            {
                string key = ((YamlScalarNode)item.Key).Value;
                string value = ((YamlScalarNode)item.Value).Value;
                dict.Add(key, value);
            }
            return dict;
        }

        private IEnumerable<KeyValuePair<YamlNode, YamlNode>> FromDict(IDictionary<string, string> items)
        {
            List<KeyValuePair<YamlNode, YamlNode>> nodes = new List<KeyValuePair<YamlNode, YamlNode>>();
            foreach (var item in items)
            {
                nodes.Add(new KeyValuePair<YamlNode, YamlNode>(new YamlScalarNode(item.Key), new YamlScalarNode(item.Value)));
            }
            return nodes;
        }

        private IList<string> ToList(YamlSequenceNode node)
        {
            List<string> list = new List<string>();
            foreach (var item in node.Children)
            {
                list.Add(((YamlScalarNode)item).Value);
            }
            return list;
        }

        private IEnumerable<YamlNode> FromList(IList<string> items)
        {
            List<YamlNode> nodes = new List<YamlNode>();
            foreach (var item in items)
            {
                nodes.Add(new YamlScalarNode(item));
            }
            return nodes;
        }

        internal void FromConfig(YamlMappingNode section)
        {
            YamlScalarNode swaggerUrl = (YamlScalarNode) GetProperty(section, SWAGGER_URL_PROPERTY);
            SwaggerUrl = swaggerUrl == null ? string.Empty : swaggerUrl.Value;

            YamlMappingNode proxies = (YamlMappingNode)GetProperty(section, PROXIES_PROPERTY);
            Proxies = proxies == null ? new Dictionary<string, string>() : ToDict(proxies);

            YamlScalarNode serviceHost = (YamlScalarNode)GetProperty(section, SERVICE_HOST_PROPERTY);
            ServiceHost = serviceHost == null ? string.Empty : serviceHost.Value;

            YamlSequenceNode methodsNode = (YamlSequenceNode)GetProperty(section, METHODS_PROPERTY);
            IList<string> methods = methodsNode == null ? DefaultMethods() : ToList(methodsNode);
            Get = methods.Contains(GET);
            Post = methods.Contains(POST);
            Put = methods.Contains(PUT);
            Delete = methods.Contains(DELETE);
            Patch = methods.Contains(PATCH);
            Options = methods.Contains(OPTIONS);
            Head = methods.Contains(HEAD);

            YamlMappingNode oauth2 = (YamlMappingNode)GetProperty(section, OAUTH2_PROPERTY);
            OAuth2 = oauth2 == null ? new Dictionary<string, string>() : ToDict(oauth2);

            YamlScalarNode apiKey = (YamlScalarNode)GetProperty(section, API_KEY_PROPERTY);
            ApiKey = apiKey == null ? string.Empty : apiKey.Value;

            YamlMappingNode basic = (YamlMappingNode)GetProperty(section, BASIC_PROPERTY);
            Basic = basic == null ? new Dictionary<string, string>() : ToDict(basic);

            YamlMappingNode ntlm = (YamlMappingNode)GetProperty(section, NTLM_PROPERTY);
            Ntlm = ntlm == null ? new Dictionary<string, string>() : ToDict(ntlm);

            YamlSequenceNode udfReturnTypesNode = (YamlSequenceNode)GetProperty(section, UDF_RETURN_TYPES_PROPERTY);
            IList<string> udfReturnTypes = udfReturnTypesNode == null ? DefaultUdfReturnTypes() : ToList(udfReturnTypesNode);
            Synchronous = udfReturnTypes.Contains(SYNCHRONOUS);
            Asynchronous = udfReturnTypes.Contains(ASYNCHRONOUS);
            
            YamlScalarNode relyOnDefinitions = (YamlScalarNode)GetProperty(section, RELY_ON_DEFINITIONS_PROPERTY);
            RelyOnDefinitions = relyOnDefinitions == null ? false : bool.Parse(relyOnDefinitions.Value);

            YamlScalarNode maxRetries = (YamlScalarNode)GetProperty(section, MAX_RETRIES_PROPERTY);
            MaxRetries = maxRetries == null ? 5 : int.Parse(maxRetries.Value);

            YamlMappingNode headers = (YamlMappingNode)GetProperty(section, HEADERS_PROPERTY);
            Headers = headers == null ? new Dictionary<string, string>() : ToDict(headers);

            YamlScalarNode connectTimeout = (YamlScalarNode)GetProperty(section, CONNECT_TIMEOUT_PROPERTY);
            ConnectTimeout = connectTimeout == null ? 1 : float.Parse(connectTimeout.Value);

            YamlScalarNode readTimeout = (YamlScalarNode)GetProperty(section, READ_TIMEOUT_PROPERTY);
            ReadTimeout = readTimeout == null ? (float?)null : float.Parse(readTimeout.Value);

            YamlScalarNode swaggerReadTimeout = (YamlScalarNode)GetProperty(section, SWAGGER_READ_TIMEOUT_PROPERTY);
            SwaggerReadTimeout = swaggerReadTimeout == null ? 5 : float.Parse(swaggerReadTimeout.Value);

            YamlSequenceNode tags = (YamlSequenceNode)GetProperty(section, TAGS_PROPERTY);
            Tags = tags == null ? new List<string>() : ToList(tags);
        }

        internal YamlMappingNode ToConfig()
        {
            YamlMappingNode section = new YamlMappingNode();

            if (!string.IsNullOrEmpty(SwaggerUrl))
                section.Add(new YamlScalarNode(SWAGGER_URL_PROPERTY), new YamlScalarNode(SwaggerUrl));

            if (Proxies != null && Proxies.Count > 0)
                section.Add(new YamlScalarNode(PROXIES_PROPERTY), new YamlMappingNode(FromDict(Proxies)));

            if (!string.IsNullOrEmpty(ServiceHost))
                section.Add(new YamlScalarNode(SERVICE_HOST_PROPERTY), new YamlScalarNode(ServiceHost));

            section.Add(new YamlScalarNode(METHODS_PROPERTY), new YamlSequenceNode(FromList(GetMethods())));

            if (OAuth2 != null && OAuth2.Count > 0)
                section.Add(new YamlScalarNode(OAUTH2_PROPERTY), new YamlMappingNode(FromDict(OAuth2)));

            if (!string.IsNullOrEmpty(ApiKey))
                section.Add(new YamlScalarNode(API_KEY_PROPERTY), new YamlScalarNode(ApiKey));

            if (Basic != null && Basic.Count > 0)
                section.Add(new YamlScalarNode(BASIC_PROPERTY), new YamlMappingNode(FromDict(Basic)));

            if (Ntlm != null && Ntlm.Count > 0)
                section.Add(new YamlScalarNode(NTLM_PROPERTY), new YamlMappingNode(FromDict(Ntlm)));

            section.Add(new YamlScalarNode(UDF_RETURN_TYPES_PROPERTY), new YamlSequenceNode(FromList(GetUdfReturnTypes())));

            section.Add(new YamlScalarNode(RELY_ON_DEFINITIONS_PROPERTY), new YamlScalarNode(RelyOnDefinitions.ToString()));

            section.Add(new YamlScalarNode(MAX_RETRIES_PROPERTY), new YamlScalarNode(MaxRetries.ToString()));

            if (Headers != null && Headers.Count > 0)
                section.Add(new YamlScalarNode(HEADERS_PROPERTY), new YamlMappingNode(FromDict(Headers)));

            section.Add(new YamlScalarNode(CONNECT_TIMEOUT_PROPERTY), new YamlScalarNode(ConnectTimeout.ToString()));

            if (ReadTimeout.HasValue)
                section.Add(new YamlScalarNode(READ_TIMEOUT_PROPERTY), new YamlScalarNode(ReadTimeout.Value.ToString()));

            section.Add(new YamlScalarNode(SWAGGER_READ_TIMEOUT_PROPERTY), new YamlScalarNode(SwaggerReadTimeout.ToString()));

            if (Tags != null && Tags.Count > 0)
                section.Add(new YamlScalarNode(TAGS_PROPERTY), new YamlSequenceNode(FromList(Tags)));

            return section;
        }

        internal void Default()
        {
            SwaggerUrl = "";
            Proxies = new Dictionary<string, string>();
            ServiceHost = "";

            Get = true;
            Post = true;
            Put = true;
            Delete = true;
            Patch = true;
            Options = true;
            Head = true;

            OAuth2 = new Dictionary<string, string>();
            ApiKey = "";
            Basic = new Dictionary<string, string>();
            Ntlm = new Dictionary<string, string>();

            Synchronous = false;
            Asynchronous = true;

            RelyOnDefinitions = false;
            MaxRetries = 5;
            Headers = new Dictionary<string, string>();
            ConnectTimeout = 1;
            ReadTimeout = null;
            SwaggerReadTimeout = 5;
            Tags = new List<string>();
        }

        private IList<string> GetMethods()
        {
            IList<string> list = new List<string>();
            if (Get)
                list.Add(GET);
            if (Post)
                list.Add(POST);
            if (Put)
                list.Add(PUT);
            if (Delete)
                list.Add(DELETE);
            if (Patch)
                list.Add(PATCH);
            if (Options)
                list.Add(OPTIONS);
            if (Head)
                list.Add(HEAD);
            return list;
        }

        private IList<string> GetUdfReturnTypes()
        {
            IList<string> list = new List<string>();
            if (Synchronous)
                list.Add(SYNCHRONOUS);
            if (Asynchronous)
                list.Add(ASYNCHRONOUS);
            return list;
        }

        private IList<string> DefaultMethods()
        {
            return new List<string> { GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD };
        }

        private IList<string> DefaultUdfReturnTypes()
        {
            return new List<string> { ASYNCHRONOUS };
        }
    }
}
