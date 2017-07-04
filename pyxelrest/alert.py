import ctypes
import sys

# If set to True, calling message_box will have no effect. Can be useful for an application running on non-graphical env
HIDE_MESSAGE_BOX = False

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
    if HIDE_MESSAGE_BOX:
        return
    if sys.version_info.major > 2:
        ctypes.windll.user32.MessageBoxW(0, message, title, BUTTON_OK | ICON_EXCLAIM | BEHAVIOR_SYSTEM_MODAL)
    else:
        ctypes.windll.user32.MessageBoxA(0, message, title, BUTTON_OK | ICON_EXCLAIM | BEHAVIOR_SYSTEM_MODAL)


