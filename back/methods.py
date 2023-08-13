from back.Controllers.controller import Controller, Session, Dbfile

def get_files_list():
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
    return result