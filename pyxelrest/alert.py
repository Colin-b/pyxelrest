import ctypes
import sys
import logging
import re

BUTTON_OK = 0x0
BUTTON_OK_CANCEL = 0x01
BUTTON_YES_NO_CANCEL = 0x03
BUTTON_YES_NO = 0x04
BUTTON_HELP = 0x4000

ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10

BEHAVIOR_SYSTEM_MODAL = 0x1000
POSITION_FOREGROUND = 0x10000
POSITION_TOP_MOST = 0x40000


def message_box(title, message):
    if sys.version_info.major > 2:
        ctypes.windll.user32.MessageBoxW(0, message, title, BUTTON_OK | ICON_EXCLAIM | BEHAVIOR_SYSTEM_MODAL)
    else:
        ctypes.windll.user32.MessageBoxA(0, message, title, BUTTON_OK | ICON_EXCLAIM | BEHAVIOR_SYSTEM_MODAL)


class AlertHandler(logging.Handler):
    """
    AlertHandler is a logging handler to show a message box when an error is logged (if the log level is error)
        h = AlertHandler()
        h.setLevel(logging.ERROR)
        logging.getLogger().addHandler(h)
    """
    tags = re.compile(r'\[\w*=([^]]*)\]')

    def emit(self, record):
        msg = self.tags.sub(r'\1', record.msg)
        message_box('Python ' + record.levelname.capitalize(), msg)

if __name__ == '__main__':
    l = logging.getLogger()
    h = AlertHandler()
    l.addHandler(h)
    try:
        raise Exception('msg')
    except:
        l.exception('toto [a=2]')
