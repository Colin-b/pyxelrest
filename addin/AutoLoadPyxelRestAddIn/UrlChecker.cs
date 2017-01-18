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
    }
}
