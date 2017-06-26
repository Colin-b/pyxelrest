import ctypes
import sys

MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10
MB_SYSTEMMODAL = 0x1000
MB_SETFOREGROUND = 0x10000
MB_TOPMOST = 0x40000


def message_box(title, message):
    if sys.version_info.major > 2:
        ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | ICON_EXCLAIM | MB_SYSTEMMODAL)
    else:
        ctypes.windll.user32.MessageBoxA(0, message, title, MB_OK | ICON_EXCLAIM | MB_SYSTEMMODAL)


