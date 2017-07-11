using log4net;
using System;
using System.Net;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class UrlChecker
    {
        private static readonly ILog Log = LogManager.GetLogger("UrlChecker");

        public static bool IsSwaggerReachable(string url, string proxy=null)
        {
            HttpWebResponse response = ConnectTo(url, proxy);
            return response != null && response.StatusCode == HttpStatusCode.OK;
        }

        private static HttpWebResponse ConnectTo(string url, string proxy)
        {
            try
            {
                Uri urlCheck = new Uri(url);
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(urlCheck);
                request.Timeout = 500;
                proxy = GetProxyFor(url, proxy);
                if (!string.IsNullOrEmpty(proxy))
                    request.Proxy = new WebProxy(proxy);
                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                response.Close();
                return response;
            }
            catch (WebException e)
            {
                HttpWebResponse response = (HttpWebResponse)e.Response;
                if (response != null)
                    response.Close();
                return response;
            }
            catch (Exception)
            {
                return null;
            }
        }

        private static string GetProxyFor(string url, string proxy)
        {
            if (string.IsNullOrEmpty(proxy))
                return null;

            string[] proxies = proxy.Split(',');
            if (proxies.Length == 1)
            {
                string[] proxyAndScheme = proxies[0].Split('=');
                if (proxyAndScheme.Length == 1)
                    return proxies[0]; // Single proxy specified (applies to the Swagger URL)
            }

            foreach (string proxyItem in proxies)
            {
                string[] proxyAndScheme = proxyItem.Split('=');
                if(proxyAndScheme.Length == 2)
                {
                    string urlProxy = GetProxyFor(url, proxyAndScheme);
                    if (urlProxy == null)
                        return null; // No Proxy for this URL
                    if (urlProxy.Length > 0)
                        return urlProxy; // Proxy for this URL
                }
            }
            return null;
        }

        private static string GetProxyFor(string url, string[] proxyAndScheme)
        {
            string scheme = proxyAndScheme[0];
            if ("no_proxy" == scheme)
                if (url.StartsWith(proxyAndScheme[1]))
                    return null;
            else if (url.StartsWith(scheme + ':'))
                return proxyAndScheme[1];
            return string.Empty;
        }
    }
}
