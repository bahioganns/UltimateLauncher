'''Work with database'''
from back.dbbase import Session, engine, Base, IntegrityError
from back.dbfile import Dbfile


class Servicedb:
    '''Parenting class for all controllers.'''

    def __init__(self) -> None:
        pass

    def add_to_db(self, dbfile):
        Base.metadata.create_all(engine)
        session = Session()

        try:
            to_add = Dbfile(dbfile.path, dbfile.name, dbfile.icon_name, dbfile.section_name)
            session.add(to_add)
            session.commit()
        except IntegrityError:
            session.rollback()
            print("Element with the same path already exists.")
        finally:
            session.close()

    def del_from_db(self, path):
        Base.metadata.create_all(engine)
        session = Session()

        try:
            to_del = session.query(Dbfile).filter_by(path=path).first()
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

    def change_existing(self, path):
        Base.metadata.create_all(engine)
        session = Session()
        session.close()

    def add_to_section(self):
        pass

    def get_data(self):
        pass

    def change_db_data(self):
        pass
    
