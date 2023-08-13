import os.path

from back.Controllers.dbbase import Session, engine, Base, IntegrityError
from back.Controllers.dbfile import Dbfile


class Controller:
    '''Parenting class for all controllers.'''

    path = ""
    name = ""
    icon_name = ""
    section_name = ""

    def __init__(self, path) -> None:
        self.path = path
        self.name = os.path.basename(path)
        self.icon_name = "icon placeholder"
        self.section_name = "all"

    def __str__(self) -> str:
        return f"Controller: path={self.path}, icon_name={self.icon_name}, name={self.name}, section_name={self.section_name}"

    def add_to_db(self):
        Base.metadata.create_all(engine)
        session = Session()

        try:
            to_add = Dbfile(self.path, self.name, self.icon_name, self.section_name)
            session.add(to_add)
            session.commit()
        except IntegrityError:
            session.rollback()
            print("Element with the same path already exists.")
        finally:
            session.close()

    def del_from_db(self):
        Base.metadata.create_all(engine)
        session = Session()

        try:
            to_del = session.query(Dbfile).filter_by(path=self.path).first()
            if to_del:
                session.delete(to_del)
                session.commit()
            else:
                print("No such element in database.")
        except Exception as e:
            session.rollback()
            print("Error occurred during deletion:", str(e))
        finally:
            session.close()

    def add_to_section(self):
        pass

    def get_data(self):
        pass

    def change_db_data(self):
        pass
    
