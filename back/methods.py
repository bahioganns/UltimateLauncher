import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import os
import win32ui
import win32gui
import win32con
import win32api
from PIL import Image

# probably it con be stored somewhere but not be called every time
def get_ex_extentions_list():
    pathext = os.environ.get('PATHEXT', '').split(os.pathsep)
    return [ext.lower() for ext in pathext]


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

    # Сохранение иконки в виде двоичного файла
    icon_bytes = icon.tobytes()
    return icon_bytes

def save_icon_from_bytes(bin_icon, file_path, file_format='PNG'):
    """Save binary icon into png file"""
    img = Image.frombytes('RGBA', (32, 32), bin_icon)
    with open(file_path, 'wb') as file:
        img.save(file, file_format)


def get_standart_app(extension):
    """Get path to the app, that windows uses to open files with such extensions"""
    # Запускаем команду assoc для получения ассоциации расширения файла с типом файла
    command = f'assoc {extension}'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    # Получаем вывод команды и извлекаем тип файла
    output = result.stdout.strip()
    file_type = output.split('=')[1].strip()

    # Запускаем команду ftype для получения исполняемого файла, связанного с типом файла
    command = f'ftype {file_type}'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    # Получаем вывод команды и извлекаем исполняемый файл
    output = result.stdout.strip()
    executable = output.split('=')[1].strip().split(" ")[0]

    return executable


def get_bin_icon_nonex(extension):
    """Get binary icon for non executable file"""
    path_to_app = get_standart_app(extension=extension)
    return extract_icon_from_exe(path_to_app)
