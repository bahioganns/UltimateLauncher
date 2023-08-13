'''Processing incoming instructions from frontend and executing them'''
from back.servicedb import Servicedb, Session, Dbfile
import json
import eel
import subprocess
import os
import tkinter as tk
from tkinter import filedialog


#TODO move to db place
#TODO: make error handling if db is empty
@eel.expose
def get_files_json():
    """Return all files from database"""
    session = Session()
    files = session.query(Dbfile).all()

    result = []
    for file in files:
        temp = Dbfile(file.path, file.name, file.icon_name, file.section_name)
        result.append(temp)
    
    session.close()
 
    serialized_list = [file.to_json() for file in result]
    json_string = json.dumps(serialized_list)
    return json_string

@eel.expose
def execute_file(path):
    """Execute process by fiven path"""
    subprocess.Popen(path)


@eel.expose
def open_file(path):
    """Open not executable file with default app"""
    os.startfile(path)


def get_filepath_from_explorer():
    """Open a file dialog and retrieve the selected file path."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        return file_path


@eel.expose
def add_new_file():
    """Add new file from the interface"""
    path = Dbfile(get_filepath_from_explorer())
    serv = Servicedb()
    serv.add_to_db(path)
