from back.Controllers.controller import Controller, Session, Dbfile
import json
import jsonpickle
import eel

@eel.expose
def get_files_json():
    session = Session()
    files = session.query(Dbfile).all()

    result = []
    for file in files:
        temp = Controller(file.path)
        temp.icon_name = file.icon_name
        temp.name = file.file_name
        temp.section_name = file.section_name
        result.append(temp)
    
    session.close()
    return jsonpickle.encode(result, unpicklable=False)