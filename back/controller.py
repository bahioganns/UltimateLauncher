'''Processing incoming instructions from frontend and executing them'''
from back.servicedbfile import ServiceDbFile, DbFile
from back.servicedbicon import ServiceDbIcon, DbIcon
from back.servicedbfile import Session
import eel
import json
import os
import subprocess

from back.methods import get_ex_extentions_list, get_filepath_from_explorer, open_ex_file, open_nonex_file, extract_icon_from_exe, get_bin_icon_nonex


@eel.expose
def get_files_json():
    """Return all files from database in json string format"""
    serv = ServiceDbFile()
    list = serv.get_files_list()
    serialized_list = [file.to_json() for file in list]
    json_string = json.dumps(serialized_list)
    return json_string


# can't use python functino to check if file is executable
@eel.expose
def open_file(id):
    """Execute if executable, open if not"""
    serv = ServiceDbFile()
    path = serv.get_path_by_id(id)
    file_extension = os.path.splitext(path)[1]
    if file_extension in get_ex_extentions_list():
        return open_ex_file(path)
    else:
        return open_nonex_file(path)


@eel.expose
def add_new_file():
    """Add new file from the interface"""
    path = get_filepath_from_explorer()
    if path:
        icon_serv = ServiceDbIcon()
        file = DbFile(path=path)
        file_extension = os.path.splitext(path)[1]
        if file_extension in get_ex_extentions_list():
            bin_icon = extract_icon_from_exe(path)
            icon = DbIcon(bin_icon=bin_icon, extension=file_extension)
        else:
            icon = icon_serv.icon_for_extension(file_extension)
            if not icon:
                bin_icon = get_bin_icon_nonex(file_extension)
                icon = DbIcon(bin_icon=bin_icon, extension=file_extension)
        
        icon_serv.add_to_db(icon)

        file.icon = icon
        file_serv = ServiceDbFile()
        file_serv.add_to_db(file)


@eel.expose
def del_file(id):
    """Delete file from the database by given id"""
    serv = ServiceDbFile()
    return serv.del_from_db(id)


@eel.expose
def change_name(id, new_name):
    """Change name of file by given id and new name"""
    serv = ServiceDbFile()
    error = serv.change_name(id, new_name)
    return error


@eel.expose
def open_containing_directory(id):
    """Open directory containing the file by id"""
    #TODO fix
    serv = ServiceDbFile()
    error = ""
    path_to_file = serv.get_path_by_id(id).replace("/", "\\")
    if path_to_file:
        subprocess.Popen(f'explorer /select,"{path_to_file}"')
    else:
        error = "No path by given id found"

    return error
