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
        ie.Visible = 1
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
        while self.Busy or (self.ReadyState != 4):
            time.sleep(0.25)

    @property
    def location_url(self):
        url = self.LocationURL
        if url == "about:blank":
            del self.ie
        return url

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
        count = 0
        while not found:
            for ie in sh.Windows():
                if ie.HWND == self._hwnd:
                    found = True
                    break
            time.sleep(0.1)

            count += 1
            if count > 100:
                break

        sh = None

        if not found:
            raise ValueError("Could not find IE instance with uuid={}".format(self._hwnd))

        return ie


def open_url(url):
    """
    Open IE on url.

    :param url: Initial URL the browser will be opened onto.
    :return: IE instance if opened.
    """
    logging.debug("Opening Microsoft Internet Explorer...")
    try:
        ie = IE()
    except pywintypes.com_error:
        return

    logging.debug("Navigating to {}.".format(url))
    ie.navigate(url)
    return ie


def close(ie):
    logging.debug("Closing Microsoft Internet Explorer...")
    ie.Quit()
    # Force release of underlying Microsoft Internet Explorer instance
    ie = None


def wait_until_url_is(ie, url, timeout, time_between_checks=1):
    ie.wait()

    current_awaited_time = 0
    # exit loop after max_time seconds
    while (ie.location_url != url) and (current_awaited_time <= timeout):
        logging.debug("Waiting for URL to be {0}... Current one is still {1} ({2}), Awaited {3} seconds on {4}.".format(
            url,
            ie.Document.Title,
            ie.location_url,
            current_awaited_time,
            timeout
        ))
        time.sleep(time_between_checks)
        current_awaited_time += time_between_checks

    if current_awaited_time > timeout:
        logging.debug("URL was still not {0} after {1} seconds.".format(url, current_awaited_time))
        return False

    logging.debug("URL is now {0}.".format(url))
    ie.wait()
    return True


def call_till_redirect(url_origin, url_redirect, max_time):
    """
    Open IE on url_origin and close IE once url_redirect is loaded.

    :param url_origin: Initial URL the browser will be opened onto.
    :param url_redirect: The redirection URL
    :param max_time: Maximum time to wait (in seconds) for redirection to be performed.
    :return: If redirection succeeded within imparted time.
    """
    ie = open_url(url_origin)

    if ie:
        was_redirected = wait_until_url_is(ie, url_redirect, max_time)
        if was_redirected:
            ie.wait()  # Wait for page to be fully loaded
        close(ie)
        return was_redirected


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    call_till_redirect('https://gemgo.gemservices.io/',
                       'https://gemgo.gemservices.io/',
                       30)
