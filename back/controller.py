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


# can't use python functino to check if file is executable
@eel.expose
def open_file(id):
    """Execute if executable, open if not"""
    serv = Servicedb()
    path = serv.get_path_by_id(id)
    file_extension = os.path.splitext(path)[1]
    if file_extension in get_ex_extentions_list():
        subprocess.Popen(path)
    else:
        os.startfile(path)


def get_filepath_from_explorer():
    """Open a file dialog and retrieve the selected file path."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


# TODO: open explorer on top
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
    serv.del_from_db(id)
