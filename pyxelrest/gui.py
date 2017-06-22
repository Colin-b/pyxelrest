import ctypes
import sys


def message_box(title, message):
    if sys.version_info.major > 2:
        ctypes.windll.user32.MessageBoxW(0, message, title, 1)
    else:
        ctypes.windll.user32.MessageBoxA(0, message, title, 1)
