"""Windows utils that are used in controller"""

import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import win32ui
import win32gui
import win32con
import win32api
from PIL import Image
import shlex
import winreg


# probably it con be stored somewhere but not be called every time
def get_ex_extentions_list():
    """Get all extensions, that windows counts as executable"""
    pathext = os.environ.get('PATHEXT', '').split(os.pathsep)
    return [extension.lower() for extension in pathext]


def open_ex_file(path):
    """Execute process by given id, can return error"""
    error = ""
    try:
        subprocess.Popen(path)
    except Exception as e:
        error = str(e)
    finally:
        return error


def open_nonex_file(path):
    """Open not executable file with default app, can return error"""
    error = ""
    try:
        os.startfile(path)
    except Exception as e:
        error = str(e)
    finally:
        return error
    
def get_filepath_from_explorer():
    """Open a file dialog and retrieve the selected file path."""
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename()
    root.attributes("-topmost", False)
    root.destroy()
    return file_path


# Have to check if it's possible to get better quality from this function
def extract_icon_from_exe(icon_in_path):
    """Given an icon path (exe file) extract it and output at the desired width/height as a png image. """
    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    large, small = win32gui.ExtractIconEx(icon_in_path,0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap( hdc, ico_x, ico_x )
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject( hbmp )
    hdc.DrawIcon( (0,0), large[0] )

    bmpstr = hbmp.GetBitmapBits(True)
    icon = Image.frombuffer('RGBA', (32, 32), bmpstr, 'raw', 'BGRA', 0, 1)

    icon_bytes = icon.tobytes()
    return icon_bytes


def get_default_windows_app(extension):
    """Get path to standart windows application for this extesion. Returns none if unsuccessfull"""
    """Can't find application for .png, .jpg, .dll and many others"""
    try:  # UserChoice\ProgId lookup initial
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts\{}\UserChoice'.format(extension)) as key:
            progid = winreg.QueryValueEx(key, 'ProgId')[0]
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Classes\{}\shell\open\command'.format(progid)) as key:
            path = winreg.QueryValueEx(key, '')[0]
    except:  # UserChoice\ProgId not found
        try:
            class_root = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, extension)
            if not class_root:  # No reference from extension
                class_root = extension  # Try direct lookup from extension
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'{}\shell\open\command'.format(class_root)) as key:
                path = winreg.QueryValueEx(key, '')[0]
        except:  # Ext not found
            path = None

    if path:
        path = os.path.expandvars(path)  # Expand env vars, e.g. %SystemRoot% for extension .txt
        path = shlex.split(path, posix=False)[0]  # posix False for Windows operation
        path = path.strip('"')  # Strip quotes

    return path


def get_bin_icon_nonex(extension):
    """Get binary icon for non executable file"""
    path_to_def_app = get_default_windows_app(extension=extension)

    if path_to_def_app:
        return extract_icon_from_exe(path_to_def_app)
    else:
        return None
