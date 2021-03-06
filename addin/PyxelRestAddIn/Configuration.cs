﻿using log4net;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using YamlDotNet.RepresentationModel;

namespace PyxelRestAddIn
{
    internal class Configuration
    {
        private static readonly ILog Log = LogManager.GetLogger("Configuration");

        internal static readonly string DEFAULT_SECTION = "DEFAULT";

        private readonly List<Service> services = new List<Service>();
        private readonly YamlStream config;

        internal ISet<string> pythonModules = new HashSet<string>();
        internal bool modified = false;

        public Configuration(string path, bool warnIfPathNotProvided=true)
        {
            if (string.IsNullOrEmpty(path))
            {
                if (warnIfPathNotProvided)
                    Log.Warn("Configuration cannot be loaded as configuration path was not provided.");
                config = null;
            }
            else
            {
                config = LoadPath(path);
            }
        }

        private YamlStream LoadPath(string path)
        {
            try
            {
                return File.GetAttributes(path).HasFlag(FileAttributes.Directory) ? LoadFolder(path) : LoadFile(path);
            }
            catch (DirectoryNotFoundException)
            {
                Log.Warn("Path corresponds to a file that does not exists, consider as empty YAML.");
                return new YamlStream();
            }
            catch (ArgumentException)
            {
                return LoadUrl(path);
            }
        }

        private YamlStream LoadUrl(string fileUrl)
        {
            HttpWebResponse response = HttpHelper.ConnectTo(fileUrl);
            if (response == null || response.StatusCode != HttpStatusCode.OK)
            {
                string details = response == null ? "" : response.StatusDescription;
                Log.ErrorFormat("Configuration cannot be loaded from {0}: {1}.", fileUrl, details);
                if (response != null)
                    response.Close();
                return null;
            }

            Log.InfoFormat("Configuration loaded from {0}: {1}.", fileUrl, response.StatusDescription);
            var parser = new YamlStream();
            var reader = new StreamReader(response.GetResponseStream());
            parser.Load(reader);
            reader.Close();
            response.Close();
            return parser;
        }

        private YamlStream LoadFile(string filePath)
        {
            var parser = new YamlStream();
            var reader = new StreamReader(filePath);
            parser.Load(reader);
            reader.Close();
            return parser;
        }

        private YamlStream LoadFolder(string folderPath)
        {
            Log.Warn("Configuration cannot be loaded as configuration folder path loading is not yet implemented.");
            return null;  // TODO Add ability to load a folder content into a single YAML data
        }

        public List<Service> Load()
        {
            services.Clear();
            if (config == null || config.Documents.Count == 0)
                return services;

            var mapping = (YamlMappingNode)config.Documents[0].RootNode;
            foreach (var section in mapping.Children)
            {
                string serviceName = ((YamlScalarNode)section.Key).Value;
                try
                {
                    Service service = AddService(serviceName);
                    service.FromConfig((YamlMappingNode) section.Value);
                }
                catch (Exception e)
                {
                    Log.Error(string.Format("Unable to load '{0}' service configuration", serviceName), e);
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
            if (!File.Exists(configurationFilePath))
            {
                Log.WarnFormat("{0} configuration file does not exists. Creating it.", configurationFilePath);
                Directory.CreateDirectory(Path.GetDirectoryName(configurationFilePath));
                File.Create(configurationFilePath).Close();
            }

            var parser = new YamlStream();
            var mapping = new YamlMappingNode();

            pythonModules.Clear();
            foreach (Service service in services)
            {
                mapping.Add(new YamlScalarNode(service.Name), service.ToConfig());
                pythonModules.UnionWith(service.GetPythonModules());
            }

            parser.Add(new YamlDocument(mapping));
            var writer = new StreamWriter(configurationFilePath);
            parser.Save(writer);
            writer.Close();
            modified = true;
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
