using System.Collections.Generic;
using YamlDotNet.RepresentationModel;

namespace PyxelRestAddIn
{
    public sealed class Service
    {
        private static readonly string OPEN_API_PROPERTY = "open_api";
        private static readonly string NETWORK_PROPERTY = "network";
        private static readonly string METHODS_PROPERTY = "methods";
        private static readonly string AUTH_PROPERTY = "auth";
        private static readonly string FORMULAS_PROPERTY = "formulas";
        private static readonly string HEADERS_PROPERTY = "headers";
        private static readonly string DESCRIPTION_PROPERTY = "description";
        private static readonly string SKIP_UPDATE_FOR_PROPERTY = "skip_update_for";
        private static readonly string PYTHON_MODULES_PROPERTY = "python_modules";
        private static readonly string CACHING_PROPERTY = "caching";

        private static readonly string GET = "get";
        private static readonly string POST = "post";
        private static readonly string PUT = "put";
        private static readonly string DELETE = "delete";
        private static readonly string PATCH = "patch";
        private static readonly string OPTIONS = "options";
        private static readonly string HEAD = "head";

        internal readonly string Name;
        private string description;
        private IList<string> skipUpdateFor;
        public IList<string> PythonModules;
        public IDictionary<string, object> OpenAPI;
        public IDictionary<string, object> Caching;

        public bool Get;
        public bool Post;
        public bool Put;
        public bool Delete;
        public bool Patch;
        public bool Options;
        public bool Head;

        public IDictionary<string, object> Auth;
        public IDictionary<string, object> Formulas;
        public IDictionary<string, object> Headers;
        public IDictionary<string, object> Network;

        public Service(string name)
        {
            Name = name;
        }

        public override string ToString()
        {
            return Description();
        }

        public string Description()
        {
            if (string.IsNullOrEmpty(description))
                return Name;
            return string.Format("{0} - {1}", Name, description);
        }

        private YamlNode GetProperty(YamlMappingNode parent, string name)
        {
            if (parent.Children.TryGetValue(new YamlScalarNode(name), out YamlNode value))
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
                else if (item.Value.NodeType == YamlNodeType.Mapping)
                    dict.Add(key, ToDict((YamlMappingNode)item.Value));
                else
                {
                    string strValue = ((YamlScalarNode)item.Value).Value;
                    if ("true".Equals(strValue) || "false".Equals(strValue))
                        dict.Add(key, "true".Equals(strValue));
                    else
                        dict.Add(key, strValue);
                }
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
                else if (IsGenericDict(item.Value))
                {
                    var dictValue = (IDictionary<string, object>)item.Value;
                    if (dictValue.Count > 0)
                        nodes.Add(new KeyValuePair<YamlNode, YamlNode>(new YamlScalarNode(item.Key), new YamlMappingNode(FromDict(dictValue))));
                }
                else if (typeof(bool) == item.Value.GetType())
                {
                    nodes.Add(new KeyValuePair<YamlNode, YamlNode>(new YamlScalarNode(item.Key), new YamlScalarNode((bool)item.Value ? "true" : "false")));
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

        private static bool IsGenericDict(object obj)
        {
            var objectType = obj.GetType();
            return objectType.IsGenericType && (objectType.GetGenericTypeDefinition() == typeof(Dictionary<,>));
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

            if (!skipUpdateFor.Contains(NETWORK_PROPERTY))
                Network = updated.Network;

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

            if (!skipUpdateFor.Contains(AUTH_PROPERTY))
                Auth = updated.Auth;

            if (!skipUpdateFor.Contains(FORMULAS_PROPERTY))
                Formulas = updated.Formulas;

            if (!skipUpdateFor.Contains(HEADERS_PROPERTY))
                Headers = updated.Headers;

            if (!skipUpdateFor.Contains(PYTHON_MODULES_PROPERTY))
                PythonModules = updated.PythonModules;

            if (!skipUpdateFor.Contains(CACHING_PROPERTY))
                Caching = updated.Caching;
        }

        internal void FromConfig(YamlMappingNode section)
        {
            var openAPI = (YamlMappingNode) GetProperty(section, OPEN_API_PROPERTY);
            OpenAPI = openAPI == null ? new Dictionary<string, object>() : ToDict(openAPI);

            var description = (YamlScalarNode)GetProperty(section, DESCRIPTION_PROPERTY);
            this.description = description == null ? string.Empty : description.Value;

            var skipUpdateForNode = (YamlSequenceNode)GetProperty(section, SKIP_UPDATE_FOR_PROPERTY);
            skipUpdateFor = skipUpdateForNode == null ? new List<string>() : ToList(skipUpdateForNode);

            var network = (YamlMappingNode)GetProperty(section, NETWORK_PROPERTY);
            Network = network == null ? new Dictionary<string, object>() : ToDict(network);
            AddDefault(Network, DefaultNetwork());

            var methodsNode = (YamlSequenceNode)GetProperty(section, METHODS_PROPERTY);
            IList<string> methods = methodsNode == null ? DefaultMethods() : ToList(methodsNode);
            Get = methods.Contains(GET);
            Post = methods.Contains(POST);
            Put = methods.Contains(PUT);
            Delete = methods.Contains(DELETE);
            Patch = methods.Contains(PATCH);
            Options = methods.Contains(OPTIONS);
            Head = methods.Contains(HEAD);

            var auth = (YamlMappingNode)GetProperty(section, AUTH_PROPERTY);
            Auth = auth == null ? new Dictionary<string, object>() : ToDict(auth);
            AddDefault(Auth, DefaultAuth());

            var formulas = (YamlMappingNode)GetProperty(section, FORMULAS_PROPERTY);
            Formulas = formulas == null ? DefaultFormulas() : ToDict(formulas);

            var headers = (YamlMappingNode)GetProperty(section, HEADERS_PROPERTY);
            Headers = headers == null ? new Dictionary<string, object>() : ToDict(headers);

            var pythonModulesNode = (YamlSequenceNode)GetProperty(section, PYTHON_MODULES_PROPERTY);
            PythonModules = pythonModulesNode == null ? new List<string>() : ToList(pythonModulesNode);

            var caching = (YamlMappingNode)GetProperty(section, CACHING_PROPERTY);
            Caching = caching == null ? new Dictionary<string, object>() : ToDict(caching);
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

            RemoveDefault(Network, DefaultNetwork());
            if (Network != null && Network.Count > 0)
                section.Add(new YamlScalarNode(NETWORK_PROPERTY), new YamlMappingNode(FromDict(Network)));

            var methods = GetMethods();
            if (methods != null && methods.Count > 0)
                section.Add(new YamlScalarNode(METHODS_PROPERTY), new YamlSequenceNode(FromList(methods)));

            RemoveDefault(Auth, DefaultAuth());
            if (Auth != null && Auth.Count > 0)
                section.Add(new YamlScalarNode(AUTH_PROPERTY), new YamlMappingNode(FromDict(Auth)));

            if (Formulas != null && Formulas.Count > 0)
                section.Add(new YamlScalarNode(FORMULAS_PROPERTY), new YamlMappingNode(FromDict(Formulas)));

            if (Headers != null && Headers.Count > 0)
                section.Add(new YamlScalarNode(HEADERS_PROPERTY), new YamlMappingNode(FromDict(Headers)));

            if (PythonModules != null && PythonModules.Count > 0)
                section.Add(new YamlScalarNode(PYTHON_MODULES_PROPERTY), new YamlSequenceNode(FromList(PythonModules)));

            if (Caching != null && Caching.Count > 0)
                section.Add(new YamlScalarNode(CACHING_PROPERTY), new YamlMappingNode(FromDict(Caching)));

            return section;
        }

        internal void Default()
        {
            OpenAPI = new Dictionary<string, object>();
            description = "";
            skipUpdateFor = new List<string>();
            Network = DefaultNetwork();

            Get = true;
            Post = true;
            Put = true;
            Delete = true;
            Patch = true;
            Options = true;
            Head = true;

            Auth = DefaultAuth();
            Formulas = DefaultFormulas();
            Headers = new Dictionary<string, object>();
            PythonModules = new List<string>();
            Caching = new Dictionary<string, object>();
        }

        private IDictionary<string, object> DefaultFormulas()
        {
            return new Dictionary<string, object>() { { "dynamic_array", new Dictionary<string, object>() { { "lock_excel", false } } } };
        }

        private IDictionary<string, object> DefaultNetwork()
        {
            return new Dictionary<string, object>() { { "max_retries", 5 }, { "connect_timeout", 1 }, { "read_timeout", 5 }, { "verify", true }, {"proxies", new Dictionary<string, object>() } };
        }

        private IDictionary<string, object> DefaultAuth()
        {
            return new Dictionary<string, object>() { { "oauth2", new Dictionary<string, object>() { { "timeout", 60 }, { "header_name", "Authorization" }, { "header_value", "Bearer {token}" } } }, { "basic", new Dictionary<string, object>() { { "username", string.Empty }, { "password", string.Empty } } }, { "ntlm", new Dictionary<string, object>() { { "username", string.Empty }, { "password", string.Empty } } }, { "api_key", string.Empty } };
        }

        private void AddDefault(IDictionary<string, object> fromConf, IDictionary<string, object> defaultConf)
        {
            foreach (var defaultItem in defaultConf)
            {
                if (!fromConf.ContainsKey(defaultItem.Key))
                {
                    fromConf[defaultItem.Key] = defaultItem.Value;
                }
                else if (IsGenericDict(defaultItem.Value))
                {
                    AddDefault((IDictionary<string, object>)fromConf[defaultItem.Key], (IDictionary<string, object>)defaultItem.Value);
                }
            }
        }

        private void RemoveDefault(IDictionary<string, object> fromConf, IDictionary<string, object> defaultConf)
        {
            foreach (var defaultItem in defaultConf)
            {
                if (fromConf.ContainsKey(defaultItem.Key))
                {
                    if (fromConf[defaultItem.Key].Equals(defaultItem.Value))
                    {
                        fromConf.Remove(defaultItem.Key);
                    }
                    else if (IsGenericDict(defaultItem.Value))
                    {
                        RemoveDefault((IDictionary<string, object>)fromConf[defaultItem.Key], (IDictionary<string, object>)defaultItem.Value);
                    }
                }
            }
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

        private IList<string> DefaultMethods()
        {
            return new List<string> { GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD };
        }
    }
}
