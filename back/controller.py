from back.servicedb import Session, Dbfile
import json
import eel

@eel.expose
def get_files_json():
    session = Session()
    files = session.query(Dbfile).all()

    result = []
    for file in files:
        temp = Dbfile(file.path, file.name, file.icon_name, file.section_name)
        result.append(temp)
    
    session.close()
    jlist = []
    for el in result:
        jlist.append(json.dumps(el.to_json()))
    return jlist