using System;
using System.IO;
using System.Net;

namespace PyxelRestAddIn
{
    public sealed class UrlChecker
    {
        public static bool CanReachOpenAPIDefinition(string url, string proxy)
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
            HttpWebResponse response = HttpHelper.ConnectTo(url, proxy, close:true);
            return response != null && response.StatusCode == HttpStatusCode.OK;
        }
    }
}
