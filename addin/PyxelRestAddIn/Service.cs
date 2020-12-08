using System.Collections.Generic;
using System.Linq;
using YamlDotNet.RepresentationModel;

namespace PyxelRestAddIn
{
    public sealed class Service
    {
        private static readonly string SKIP_UPDATE_FOR_PROPERTY = "skip_update_for";
        private static readonly string DESCRIPTION_PROPERTY = "description";
        private static readonly string OPEN_API_PROPERTY = "open_api";
        private static readonly string NETWORK_PROPERTY = "network";
        private static readonly string AUTH_PROPERTY = "auth";
        private static readonly string FORMULAS_PROPERTY = "formulas";

        internal readonly string Name;
        private IList<string> skipUpdateFor;
        public string description;
        public IDictionary<string, object> OpenAPI;
        public IDictionary<string, object> Network;
        public IDictionary<string, object> Auth;
        public IDictionary<string, object> Formulas;

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

        internal IEnumerable<string> GetPythonModules()
        {
            var pythonModules = new List<string>();

            if (Network != null && Network.ContainsKey("verify"))
                pythonModules.Add("python-certifi-win32==1.*");

            if (Formulas != null)
            {
                foreach (var formula in Formulas)
                {
                    IDictionary<string, object> formulaOptions = (IDictionary<string, object>)formula.Value;
                    if (formulaOptions.ContainsKey("cache"))
                    {
                        IDictionary<string, object> formulaCache = (IDictionary<string, object>)formulaOptions["cache"];
                        if (formulaCache.ContainsKey("result_caching_time"))
                        {
                            pythonModules.Add("cachetools==4.*");
                            break;
                        }
                    }
                }
                
            }

            if (Auth != null && Auth.ContainsKey("ntlm"))
            {
                IDictionary<string, object> ntlm = (IDictionary<string, object>)Auth["ntlm"];
                if (ntlm != null && ntlm.Count > 0)
                    pythonModules.Add("requests_ntlm==1.*");
            }

            return pythonModules;
        }


        private IDictionary<string, object> UpdateOption(IDictionary<string, object> optionsNotToUpdate, IDictionary<string, object> actual, IDictionary<string, object> update)
        {
            // If the whole content must not be updated, return the actual content
            if (optionsNotToUpdate == null || optionsNotToUpdate.Count() == 0)
                return actual;

            var merged = update;

            foreach (var optionNotToUpdate in optionsNotToUpdate)
            {
                if (actual.ContainsKey(optionNotToUpdate.Key))
                {
                    // If the update does not contains the options, use the actual content
                    if (!merged.ContainsKey(optionNotToUpdate.Key))
                    {
                        merged[optionNotToUpdate.Key] = actual[optionNotToUpdate.Key];
                    }
                    // Otherwise perform a partial update
                    else
                    {
                        merged[optionNotToUpdate.Key] = UpdateOption((IDictionary<string, object>)optionNotToUpdate.Value, (IDictionary<string, object>)actual[optionNotToUpdate.Key], (IDictionary<string, object>)merged[optionNotToUpdate.Key]);
                    }
                }
            }

            return merged;
        }

        private void ToDict(IDictionary<string, IDictionary<string, object>> result, IEnumerable<string> sections)
        {
            string section = sections.ElementAt(0);
            if (!result.ContainsKey(section))
                result[section] = new Dictionary<string, object>();

            ToDict((IDictionary<string, IDictionary<string, object>>)result[section], sections.Skip(1));
        }

        internal void UpdateFrom(Service updated)
        {
            skipUpdateFor = updated.skipUpdateFor;

            var optionsNotToUpdate = new Dictionary<string, IDictionary<string, object>>();
            foreach (string sections in skipUpdateFor)
                ToDict(optionsNotToUpdate, sections.Split('.'));

            if (!optionsNotToUpdate.ContainsKey(DESCRIPTION_PROPERTY))
                description = updated.description;

            OpenAPI = UpdateOption(optionsNotToUpdate.ContainsKey(OPEN_API_PROPERTY) ? optionsNotToUpdate[OPEN_API_PROPERTY] : null, OpenAPI, updated.OpenAPI);
            Network = UpdateOption(optionsNotToUpdate.ContainsKey(NETWORK_PROPERTY) ? optionsNotToUpdate[NETWORK_PROPERTY] : null, Network, updated.Network);
            Auth = UpdateOption(optionsNotToUpdate.ContainsKey(AUTH_PROPERTY) ? optionsNotToUpdate[AUTH_PROPERTY] : null, Auth, updated.Auth);
            Formulas = UpdateOption(optionsNotToUpdate.ContainsKey(FORMULAS_PROPERTY) ? optionsNotToUpdate[FORMULAS_PROPERTY] : null, Formulas, updated.Formulas);
        }

        internal void FromConfig(YamlMappingNode section)
        {
            var skipUpdateForNode = (YamlSequenceNode)GetProperty(section, SKIP_UPDATE_FOR_PROPERTY);
            skipUpdateFor = skipUpdateForNode == null ? new List<string>() : ToList(skipUpdateForNode);

            var description = (YamlScalarNode)GetProperty(section, DESCRIPTION_PROPERTY);
            this.description = description == null ? string.Empty : description.Value;

            var openAPI = (YamlMappingNode) GetProperty(section, OPEN_API_PROPERTY);
            OpenAPI = openAPI == null ? new Dictionary<string, object>() : ToDict(openAPI);
            AddDefault(OpenAPI, DefaultOpenAPI());

            var network = (YamlMappingNode)GetProperty(section, NETWORK_PROPERTY);
            Network = network == null ? new Dictionary<string, object>() : ToDict(network);
            AddDefault(Network, DefaultNetwork());

            var auth = (YamlMappingNode)GetProperty(section, AUTH_PROPERTY);
            Auth = auth == null ? new Dictionary<string, object>() : ToDict(auth);
            AddDefault(Auth, DefaultAuth());

            var formulas = (YamlMappingNode)GetProperty(section, FORMULAS_PROPERTY);
            Formulas = formulas == null ? DefaultFormulas() : ToDict(formulas);
        }

        internal YamlMappingNode ToConfig()
        {
            var section = new YamlMappingNode();

            if (skipUpdateFor != null && skipUpdateFor.Count > 0)
                section.Add(new YamlScalarNode(SKIP_UPDATE_FOR_PROPERTY), new YamlSequenceNode(FromList(skipUpdateFor)));

            if (!string.IsNullOrEmpty(description))
                section.Add(new YamlScalarNode(DESCRIPTION_PROPERTY), new YamlScalarNode(description));

            RemoveDefault(OpenAPI, DefaultOpenAPI());
            if (OpenAPI != null && OpenAPI.Count > 0)
                section.Add(new YamlScalarNode(OPEN_API_PROPERTY), new YamlMappingNode(FromDict(OpenAPI)));

            RemoveDefault(Network, DefaultNetwork());
            if (Network != null && Network.Count > 0)
                section.Add(new YamlScalarNode(NETWORK_PROPERTY), new YamlMappingNode(FromDict(Network)));

            RemoveDefault(Auth, DefaultAuth());
            if (Auth != null && Auth.Count > 0)
                section.Add(new YamlScalarNode(AUTH_PROPERTY), new YamlMappingNode(FromDict(Auth)));

            RemoveDefaultForEach(Formulas, new Dictionary<string, object> { { "cache", DefaultFormulasCache } });
            if (Formulas != null && Formulas.Count > 0)
                section.Add(new YamlScalarNode(FORMULAS_PROPERTY), new YamlMappingNode(FromDict(Formulas)));

            return section;
        }

        internal void Default()
        {
            skipUpdateFor = new List<string>();
            description = "";
            OpenAPI = DefaultOpenAPI();
            Network = DefaultNetwork();
            Auth = DefaultAuth();
            Formulas = DefaultFormulas();
        }

        private IDictionary<string, object> DefaultOpenAPI()
        {
            return new Dictionary<string, object>() { { "selected_methods", new List<string> { "get", "post", "put", "delete", "patch", "options", "head" } } };
        }

        private IDictionary<string, object> DefaultFormulas()
        {
            return new Dictionary<string, object>() { { "dynamic_array", new Dictionary<string, object>() { { "lock_excel", false }, { "prefix", "{name}_" } } } };
        }

        public static readonly IDictionary<string, object> DefaultFormulasCache = new Dictionary<string, object>() { { "duration", 0 }, { "size", 100 } };

        private IDictionary<string, object> DefaultNetwork()
        {
            return new Dictionary<string, object>() { { "max_retries", 5 }, { "connect_timeout", 1 }, { "read_timeout", 5 }, { "verify", true }, {"proxies", new Dictionary<string, object>() }, { "headers", new Dictionary<string, object>() } };
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

        private void RemoveDefaultForEach(IDictionary<string, object> fromConfs, IDictionary<string, object> defaultConf)
        {
            if (fromConfs != null)
            {
                foreach (var fromConf in fromConfs)
                {
                    RemoveDefault((IDictionary<string, object>)fromConf.Value, defaultConf);
                }
            }
        }

        private void RemoveDefault(IDictionary<string, object> fromConf, IDictionary<string, object> defaultConf)
        {
            foreach (var defaultItem in defaultConf)
            {
                if (fromConf.ContainsKey(defaultItem.Key))
                {
                    if (IsGenericList(defaultItem.Value))
                    {
                        IList<object> confList = (IList<object>)fromConf[defaultItem.Key];
                        IList<object> defaultList = (IList<object>)defaultItem.Value;
                        
                        // Order of elements does not matter in our case for list equality
                        if (confList.All(defaultList.Contains) && confList.Count == defaultList.Count)
                        {
                            fromConf.Remove(defaultItem.Key);
                        }
                    }
                    else if (fromConf[defaultItem.Key].Equals(defaultItem.Value))
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
    }
}
