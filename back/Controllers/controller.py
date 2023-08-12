import os.path

from back.Controllers.dbbase import Session, engine, Base
from back.Controllers.dbfile import Dbfile


class Controller:
    '''Parenting class for all controllers'''

    path = ""
    name = ""
    icon_name = ""
    section_name = "all"

    def __init__(self, path) -> None:
        pass
        # self.path = path
        # self.name = os.path.basename(path)
        # self.section_name = "all"
    
    def add_to_db(self, path):
        Base.metadata.create_all(engine)
        session = Session()
        to_add = Dbfile(path, os.path.basename(path), "icon_name placeholder", self.section_name)
        session.add(to_add)
        session.commit()

    def get_data(self):
        pass

    def change_db_data(self):
        pass
    
