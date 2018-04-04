using log4net;
using System;
using System.IO;
using System.Net;

namespace AutoLoadPyxelRestAddIn
{
    public sealed class UrlChecker
    {
        private static readonly ILog Log = LogManager.GetLogger("UrlChecker");

        public static bool IsSwaggerReachable(string url, string proxy)
        {
            if (url.StartsWith("file://"))
            {
                try
                {
                    return File.Exists(url.Substring(7));
                }
                catch(Exception)
                {
                    return false;
                }
            }
            HttpWebResponse response = ConnectTo(url, proxy);
            return response != null && response.StatusCode == HttpStatusCode.OK;
        }

        internal static HttpWebResponse ConnectTo(string url, string proxy, bool close=true)
        {
            try
            {
                Uri urlCheck = new Uri(url);
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(urlCheck);
                request.Timeout = 500;
                if (proxy == null)
                    request.Proxy = new WebProxy();
                else if (proxy.Length > 0)
                    request.Proxy = new WebProxy(proxy);
                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                if (close)
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

        internal static string GetProxyFor(string url)
        {
            string no_proxy = Environment.GetEnvironmentVariable("NO_PROXY");
            if (string.IsNullOrEmpty(no_proxy))
                return string.Empty; // System proxy should be used

            foreach(string no_proxy_url in no_proxy.Split(','))
            {
                if (url.Contains(no_proxy))
                    return null;  // No proxy should be used
            }
            return string.Empty;  // System proxy should be used
        }
    }
}
