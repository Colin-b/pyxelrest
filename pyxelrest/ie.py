import logging
import time

import pywintypes
from win32com.client import Dispatch


class IE:
    """A proxy class to the InternetExplorer.Application that handles gracefully.
    
    See http://stackoverflow.com/questions/12965032/excel-vba-controlling-ie-local-intranet for reason.
    Using UWND instead of LocationURL as more stable."""

    def __init__(self):
        ie = Dispatch("InternetExplorer.Application")
        object.__setattr__(self, "_hwnd", ie.HWND)

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

    def wait(self):
        """Wait for end of page loading"""
        while (self.ReadyState != 4):
            time.sleep(0.25)

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

def call_till_redirect(url_origin,
                       url_redirect):
    """Open IE on url_origin and close IE once url_redirect is loaded."""
    logging.info("Opening IE")
    try:
        ie = IE()
    except pywintypes.com_error:
        return False


    logging.info("Navigating to {}".format(url_origin))
    ie.navigate(url_origin)

    ie.wait()

    count = 0.
    sleep_time = 1
    max_time = 20.
    # exit loop after max_time seconds
    while (ie.LocationURL != url_redirect) and (count <= max_time):
        logging.info("Waiting to land on {}, still on {} : {} / {}".format(
            url_redirect, ie.LocationURL,
            url_redirect != ie.LocationURL,
            count
        ))
        time.sleep(sleep_time)
        count += sleep_time

    if count > max_time:
        ie.Quit()
        return False

    ie.wait()

    logging.info("Closing IE")
    ie.Quit()

    ie = None

    return True


if __name__ == '__main__':
    call('https://developer.gemservices.io/',
         # msg_auth_asked="Sign in below with your internal account",
         msg_auth_done="You are now authenticated")
