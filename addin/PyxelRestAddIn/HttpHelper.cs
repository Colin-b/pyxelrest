using log4net;
using System;
using System.Net;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;

namespace PyxelRestAddIn
{
    public sealed class HttpHelper
    {
        private static readonly ILog Log = LogManager.GetLogger("HttpHelper");

        internal static HttpWebResponse ConnectTo(string url, string proxy="", bool close=false)
        {
            try
            {
                ServicePointManager.ServerCertificateValidationCallback += new RemoteCertificateValidationCallback(AlwaysValidate);
                ServicePointManager.Expect100Continue = true;
                ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                Uri urlCheck = new Uri(url);
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(urlCheck);
                request.ServerCertificateValidationCallback += new RemoteCertificateValidationCallback(AlwaysValidate);
                request.Timeout = 500;
                if (proxy.Equals(string.Empty))
                    proxy = GetProxyFor(url);
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

        private static bool AlwaysValidate(object sender, X509Certificate certificate, X509Chain chain, SslPolicyErrors sslPolicyErrors)
        {
            return true;
        }

        internal static string GetProxyFor(string url)
        {
            string no_proxy = Environment.GetEnvironmentVariable("NO_PROXY");
            if (string.IsNullOrEmpty(no_proxy))
                return string.Empty; // System proxy should be used

            foreach(string no_proxy_url in no_proxy.Split(','))
            {
                if (url.Contains(no_proxy_url))
                    return null;  // No proxy should be used
            }
            return string.Empty;  // System proxy should be used
        }
    }
}
