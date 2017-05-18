import logging
import time

import pywintypes
from win32com.client import Dispatch


class IE:
    """A proxy class to the InternetExplorer.Application that handles gracefully.
    
    See http://stackoverflow.com/questions/12965032/excel-vba-controlling-ie-local-intranet for reason.
    Using UWND instead of LocationURL as more stable."""

    def __init__(self):
        object.__setattr__(self, "_hwnd", Dispatch("InternetExplorer.Application").HWND)

    def __getattr__(self, item):
        try:
            return getattr(self.ie, item)
        except pywintypes.com_error as e:
            del self.ie
            return getattr(self, item)

    def __setattr__(self, item, value):
        try:
            setattr(self.ie, item, value)
        except pywintypes.com_error:
            del self.ie
            setattr(self, item, value)

    @property
    def ie(self):
        if not "_ie" in self.__dict__:
            object.__setattr__(self, "_ie", self._get_ie_from_hwnd())

        return self._ie

    @ie.deleter
    def ie(self):
        del self._ie

    def _get_ie_from_hwnd(self):
        """Retrieve the IE instance with the proper HWND property based on self._hwnd"""
        sh = Dispatch("Shell.Application")

        found = False
        while not found:
            for ie in sh.Windows():
                if ie.HWND == self._hwnd:
                    found = True
                    break
            else:
                found = False
            time.sleep(0.1)

        sh = None

        if not found:
            raise ValueError("Could not find IE instance with uuid={}".format(hwnd))

        return ie


#
# def call(url,
#          msg_auth_asked=None,
#          msg_auth_done=None,
#          url_auth_done=None):
#     ie = IE()
#
#     ie.navigate(url)
#
#     while (ie.ReadyState != 4):
#         time.sleep(0.1)
#     logging.info("here")
#     # click on login button
#     # for btn in ie.Document.Body.getElementsByClassName("btn-link"):
#     #     btn.click()
#     print("first check", (msg_auth_asked and msg_auth_asked in ie.document.body.innerText))
#     if (msg_auth_asked and msg_auth_asked in ie.document.body.innerText):
#         popup_for_auth = True
#     else:
#         if url_auth_done:
#             while (ie.LocationURL != url_auth_done):
#                 print("waiting to land on", url_auth_done, ie.LocationURL)
#                 time.sleep(2)
#             popup_for_auth = False
#         else:
#             popup_for_auth = not (msg_auth_done and msg_auth_done in ie.document.body.innerText)
#
#     print("need to popup", popup_for_auth)
#     if popup_for_auth:
#         print("pop up for auth")
#         ie.Visible = 1
#     else:
#         print("already auth")
#         ie.Quit()
#
#     ie = None
#
#     return True

def call_till_redirect(url_origin,
                       url_redirect):
    """Open IE on url_origin and close IE once url_redirect is loaded."""
    logging.debug("Opening IE")
    ie = IE()

    logging.debug("Navigating to {}".format(url_origin))
    ie.navigate(url_origin)

    while (ie.LocationURL != url_redirect):
        logging.debug("Waiting to land on {}".format(url_redirect))
        time.sleep(0.25)

    while (ie.ReadyState != 4):
        logging.debug("Waiting redirect page fully loaded")
        time.sleep(0.1)

    logging.debug("Closing IE")
    ie.Quit()

    ie = None

    return True


if __name__ == '__main__':
    call('https://developer.gemservices.io/',
         # msg_auth_asked="Sign in below with your internal account",
         msg_auth_done="You are now authenticated")
