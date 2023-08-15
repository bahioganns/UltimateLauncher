'''Processing incoming instructions from frontend and executing them'''
from back.servicedb import Servicedb, Dbfile
import eel
import subprocess
import os
import tkinter as tk
import json
from tkinter import filedialog


@eel.expose
def get_files_json():
    """Return all files from database in json string format"""
    serv = Servicedb()
    list = serv.get_files_list()
    serialized_list = [file.to_json() for file in list]
    json_string = json.dumps(serialized_list)
    return json_string


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


# can't use python functino to check if file is executable
@eel.expose
def open_file(id):
    """Execute if executable, open if not"""
    serv = Servicedb()
    path = serv.get_path_by_id(id)
    file_extension = os.path.splitext(path)[1]
    if file_extension in get_ex_extentions_list():
        return open_ex_file(path)
    else:
        return open_nonex_file(path)


def get_filepath_from_explorer():
    """Open a file dialog and retrieve the selected file path."""
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename()
    root.attributes("-topmost", False)
    root.destroy()
    return file_path


@eel.expose
def add_new_file():
    """Add new file from the interface"""
    path = get_filepath_from_explorer()
    if path:
        file = Dbfile(path)
        serv = Servicedb()
        serv.add_to_db(file)


@eel.expose
def del_file(id):
    """Delete file from the database by given id"""
    serv = Servicedb()
    return serv.del_from_db(id)


@eel.expose
def change_name(id, new_name):
    """Change name of file by given id and new name"""
    serv = Servicedb()
    error = serv.change_name(id, new_name)
    return error


@eel.expose
def open_containing_directory(id):
    """Open directory containing the file by id"""
    serv = Servicedb()
    error = ""
    path_to_file = serv.get_path_by_id(id)
    if path_to_file:
        subprocess.Popen(f'explorer /select,"{path_to_file}"')
    else:
        error = "No path by given id found"

    return error
