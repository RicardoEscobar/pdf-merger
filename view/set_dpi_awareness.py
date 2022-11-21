"""Enabling High-DPI in Windows 10"""


def set_dpi_awareness() -> None:
    """Enabling High-DPI in Windows 10"""
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
