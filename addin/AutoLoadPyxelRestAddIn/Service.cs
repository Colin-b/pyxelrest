using log4net;
using System.Collections.Generic;
using YamlDotNet.RepresentationModel;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class Service
    {
        private static readonly ILog Log = LogManager.GetLogger("Service");

        private static readonly string OPEN_API_PROPERTY = "open_api";
        private static readonly string PROXIES_PROPERTY = "proxies";
        private static readonly string METHODS_PROPERTY = "methods";
        private static readonly string OAUTH2_PROPERTY = "oauth2";
        private static readonly string API_KEY_PROPERTY = "api_key";
        private static readonly string BASIC_PROPERTY = "basic";
        private static readonly string NTLM_PROPERTY = "ntlm";
        private static readonly string UDF_RETURN_TYPES_PROPERTY = "udf_return_types";
        private static readonly string MAX_RETRIES_PROPERTY = "max_retries";
        private static readonly string HEADERS_PROPERTY = "headers";
        private static readonly string CONNECT_TIMEOUT_PROPERTY = "connect_timeout";
        private static readonly string READ_TIMEOUT_PROPERTY = "read_timeout";
        private static readonly string DESCRIPTION_PROPERTY = "description";
        private static readonly string SKIP_UPDATE_FOR_PROPERTY = "skip_update_for";

        private static readonly string GET = "get";
        private static readonly string POST = "post";
        private static readonly string PUT = "put";
        private static readonly string DELETE = "delete";
        private static readonly string PATCH = "patch";
        private static readonly string OPTIONS = "options";
        private static readonly string HEAD = "head";

        private static readonly string VBA_COMPATIBLE = "vba_compatible";
        private static readonly string AUTO_EXPAND = "auto_expand";

        internal readonly string Name;
        private string description;
        private IList<string> skipUpdateFor;
        public IDictionary<string, object> OpenAPI;
        public IDictionary<string, object> Proxies;

        public bool Get;
        public bool Post;
        public bool Put;
        public bool Delete;
        public bool Patch;
        public bool Options;
        public bool Head;

        public IDictionary<string, object> OAuth2;
        public string ApiKey;
        public IDictionary<string, object> Basic;
        public IDictionary<string, object> Ntlm;

        public bool VBACompatible;
        public bool AutoExpand;

        public int MaxRetries;
        public IDictionary<string, object> Headers;
        public decimal ConnectTimeout;
        public decimal ReadTimeout;

        public Service(string name)
        {
            Name = name;
        }

        public override string ToString()
        {
            return Name;
        }

        public string Description()
        {
            if (string.IsNullOrEmpty(description))
                return Name;
            return string.Format("{0} ({1})", description, Name);
        }

        private YamlNode GetProperty(YamlMappingNode parent, string name)
        {
            YamlNode value;
            if (parent.Children.TryGetValue(new YamlScalarNode(name), out value))
                return value;
            return null;
        }

        private IDictionary<string, object> ToDict(YamlMappingNode node)
        {
            var dict = new Dictionary<string, object>();
            foreach(var item in node.Children)
            {
                string key = ((YamlScalarNode)item.Key).Value;
                if (item.Value.NodeType == YamlNodeType.Sequence)
                    dict.Add(key, ToList((YamlSequenceNode)item.Value));
                else
                    dict.Add(key, ((YamlScalarNode)item.Value).Value);
            }
            return dict;
        }

        private IEnumerable<KeyValuePair<YamlNode, YamlNode>> FromDict(IDictionary<string, object> items)
        {
            var nodes = new List<KeyValuePair<YamlNode, YamlNode>>();
            foreach (var item in items)
            {
                if (IsGenericList(item.Value))
                {
                    var listValue = (IList<string>)item.Value;
                    if (listValue.Count > 0)
                        nodes.Add(new KeyValuePair<YamlNode, YamlNode>(new YamlScalarNode(item.Key), new YamlSequenceNode(FromList(listValue))));
                }
                else
                {
                    nodes.Add(new KeyValuePair<YamlNode, YamlNode>(new YamlScalarNode(item.Key), new YamlScalarNode(item.Value.ToString())));
                }
            }
            return nodes;
        }

        private static bool IsGenericList(object obj)
        {
            var objectType = obj.GetType();
            return (objectType.IsGenericType && (objectType.GetGenericTypeDefinition() == typeof(List<>)));
        }

        private IList<string> ToList(YamlSequenceNode node)
        {
            var list = new List<string>();
            foreach (var item in node.Children)
                list.Add(((YamlScalarNode)item).Value);
            return list;
        }

        private IEnumerable<YamlNode> FromList(IList<string> items)
        {
            var nodes = new List<YamlNode>();
            foreach (var item in items)
                nodes.Add(new YamlScalarNode(item));
            return nodes;
        }

        internal void UpdateFrom(Service updated)
        {
            skipUpdateFor = updated.skipUpdateFor;

            if (!skipUpdateFor.Contains(OPEN_API_PROPERTY))
                OpenAPI = updated.OpenAPI;

            if (!skipUpdateFor.Contains(DESCRIPTION_PROPERTY))
                description = updated.description;

            if (!skipUpdateFor.Contains(PROXIES_PROPERTY))
                Proxies = updated.Proxies;

            if (!skipUpdateFor.Contains(METHODS_PROPERTY))
            {
                Get = updated.Get;
                Post = updated.Post;
                Put = updated.Put;
                Delete = updated.Delete;
                Patch = updated.Patch;
                Options = updated.Options;
                Head = updated.Head;
            }

            if (!skipUpdateFor.Contains(OAUTH2_PROPERTY))
                OAuth2 = updated.OAuth2;

            if (!skipUpdateFor.Contains(API_KEY_PROPERTY))
                ApiKey = updated.ApiKey;

            if (!skipUpdateFor.Contains(BASIC_PROPERTY))
                Basic = updated.Basic;

            if (!skipUpdateFor.Contains(NTLM_PROPERTY))
                Ntlm = updated.Ntlm;

            if (!skipUpdateFor.Contains(UDF_RETURN_TYPES_PROPERTY))
            {
                VBACompatible = updated.VBACompatible;
                AutoExpand = updated.AutoExpand;
            }

            if (!skipUpdateFor.Contains(MAX_RETRIES_PROPERTY))
                MaxRetries = updated.MaxRetries;

            if (!skipUpdateFor.Contains(HEADERS_PROPERTY))
                Headers = updated.Headers;

            if (!skipUpdateFor.Contains(CONNECT_TIMEOUT_PROPERTY))
                ConnectTimeout = updated.ConnectTimeout;

            if (!skipUpdateFor.Contains(READ_TIMEOUT_PROPERTY))
                ReadTimeout = updated.ReadTimeout;
        }

        internal void FromConfig(YamlMappingNode section)
        {
            var openAPI = (YamlMappingNode) GetProperty(section, OPEN_API_PROPERTY);
            OpenAPI = openAPI == null ? new Dictionary<string, object>() : ToDict(openAPI);

            var description = (YamlScalarNode)GetProperty(section, DESCRIPTION_PROPERTY);
            this.description = description == null ? string.Empty : description.Value;

            var skipUpdateForNode = (YamlSequenceNode)GetProperty(section, SKIP_UPDATE_FOR_PROPERTY);
            skipUpdateFor = skipUpdateForNode == null ? new List<string>() : ToList(skipUpdateForNode);

            var proxies = (YamlMappingNode)GetProperty(section, PROXIES_PROPERTY);
            Proxies = proxies == null ? new Dictionary<string, object>() : ToDict(proxies);

            var methodsNode = (YamlSequenceNode)GetProperty(section, METHODS_PROPERTY);
            IList<string> methods = methodsNode == null ? DefaultMethods() : ToList(methodsNode);
            Get = methods.Contains(GET);
            Post = methods.Contains(POST);
            Put = methods.Contains(PUT);
            Delete = methods.Contains(DELETE);
            Patch = methods.Contains(PATCH);
            Options = methods.Contains(OPTIONS);
            Head = methods.Contains(HEAD);

            var oauth2 = (YamlMappingNode)GetProperty(section, OAUTH2_PROPERTY);
            OAuth2 = oauth2 == null ? new Dictionary<string, object>() : ToDict(oauth2);

            var apiKey = (YamlScalarNode)GetProperty(section, API_KEY_PROPERTY);
            ApiKey = apiKey == null ? string.Empty : apiKey.Value;

            var basic = (YamlMappingNode)GetProperty(section, BASIC_PROPERTY);
            Basic = basic == null ? new Dictionary<string, object>() : ToDict(basic);

            var ntlm = (YamlMappingNode)GetProperty(section, NTLM_PROPERTY);
            Ntlm = ntlm == null ? new Dictionary<string, object>() : ToDict(ntlm);

            var udfReturnTypesNode = (YamlSequenceNode)GetProperty(section, UDF_RETURN_TYPES_PROPERTY);
            IList<string> udfReturnTypes = udfReturnTypesNode == null ? DefaultUdfReturnTypes() : ToList(udfReturnTypesNode);
            VBACompatible = udfReturnTypes.Contains(VBA_COMPATIBLE);
            AutoExpand = udfReturnTypes.Contains(AUTO_EXPAND);

            var maxRetries = (YamlScalarNode)GetProperty(section, MAX_RETRIES_PROPERTY);
            MaxRetries = maxRetries == null ? 5 : int.Parse(maxRetries.Value);

            var headers = (YamlMappingNode)GetProperty(section, HEADERS_PROPERTY);
            Headers = headers == null ? new Dictionary<string, object>() : ToDict(headers);

            var connectTimeout = (YamlScalarNode)GetProperty(section, CONNECT_TIMEOUT_PROPERTY);
            ConnectTimeout = connectTimeout == null ? 1 : decimal.Parse(connectTimeout.Value);

            var readTimeout = (YamlScalarNode)GetProperty(section, READ_TIMEOUT_PROPERTY);
            ReadTimeout = readTimeout == null ? 0 : decimal.Parse(readTimeout.Value);
        }

        internal YamlMappingNode ToConfig()
        {
            var section = new YamlMappingNode();

            if (OpenAPI != null && OpenAPI.Count > 0)
                section.Add(new YamlScalarNode(OPEN_API_PROPERTY), new YamlMappingNode(FromDict(OpenAPI)));

            if (!string.IsNullOrEmpty(description))
                section.Add(new YamlScalarNode(DESCRIPTION_PROPERTY), new YamlScalarNode(description));

            if (skipUpdateFor != null && skipUpdateFor.Count > 0)
                section.Add(new YamlScalarNode(SKIP_UPDATE_FOR_PROPERTY), new YamlSequenceNode(FromList(skipUpdateFor)));

            if (Proxies != null && Proxies.Count > 0)
                section.Add(new YamlScalarNode(PROXIES_PROPERTY), new YamlMappingNode(FromDict(Proxies)));

            var methods = GetMethods();
            if (methods != null && methods.Count > 0)
                section.Add(new YamlScalarNode(METHODS_PROPERTY), new YamlSequenceNode(FromList(methods)));

            if (OAuth2 != null && OAuth2.Count > 0)
                section.Add(new YamlScalarNode(OAUTH2_PROPERTY), new YamlMappingNode(FromDict(OAuth2)));

            if (!string.IsNullOrEmpty(ApiKey))
                section.Add(new YamlScalarNode(API_KEY_PROPERTY), new YamlScalarNode(ApiKey));

            if (Basic != null && Basic.Count > 0)
                section.Add(new YamlScalarNode(BASIC_PROPERTY), new YamlMappingNode(FromDict(Basic)));

            if (Ntlm != null && Ntlm.Count > 0)
                section.Add(new YamlScalarNode(NTLM_PROPERTY), new YamlMappingNode(FromDict(Ntlm)));

            var udfReturnTypes = GetUdfReturnTypes();
            if (udfReturnTypes != null && udfReturnTypes.Count > 0)
                section.Add(new YamlScalarNode(UDF_RETURN_TYPES_PROPERTY), new YamlSequenceNode(FromList(udfReturnTypes)));

            if (MaxRetries != 5)
                section.Add(new YamlScalarNode(MAX_RETRIES_PROPERTY), new YamlScalarNode(MaxRetries.ToString()));

            if (Headers != null && Headers.Count > 0)
                section.Add(new YamlScalarNode(HEADERS_PROPERTY), new YamlMappingNode(FromDict(Headers)));

            if (ConnectTimeout != 1)
                section.Add(new YamlScalarNode(CONNECT_TIMEOUT_PROPERTY), new YamlScalarNode(ConnectTimeout.ToString()));

            if (ReadTimeout > 0)
                section.Add(new YamlScalarNode(READ_TIMEOUT_PROPERTY), new YamlScalarNode(ReadTimeout.ToString()));

            return section;
        }

        internal void Default()
        {
            OpenAPI = new Dictionary<string, object>();
            description = "";
            skipUpdateFor = new List<string>();
            Proxies = new Dictionary<string, object>();

            Get = true;
            Post = true;
            Put = true;
            Delete = true;
            Patch = true;
            Options = true;
            Head = true;

            OAuth2 = new Dictionary<string, object>();
            ApiKey = "";
            Basic = new Dictionary<string, object>();
            Ntlm = new Dictionary<string, object>();

            VBACompatible = false;
            AutoExpand = true;

            MaxRetries = 5;
            Headers = new Dictionary<string, object>();
            ConnectTimeout = 1;
            ReadTimeout = 0;
        }

        private IList<string> GetMethods()
        {
            var list = new List<string>();
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
            var list = new List<string>();
            if (VBACompatible)
                list.Add(VBA_COMPATIBLE);
            if (AutoExpand)
                list.Add(AUTO_EXPAND);
            return list;
        }

        private IList<string> DefaultMethods()
        {
            return new List<string> { GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD };
        }

        private IList<string> DefaultUdfReturnTypes()
        {
            return new List<string> { AUTO_EXPAND };
        }
    }
}
