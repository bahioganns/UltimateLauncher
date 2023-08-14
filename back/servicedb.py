'''Work with database'''
from back.dbbase import Session, engine, Base, IntegrityError
from back.dbfile import Dbfile


class Servicedb:
    '''Parenting class for all controllers.'''

    def __init__(self) -> None:
        Base.metadata.create_all(engine)

    def add_to_db(self, dbfile):
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

    def del_from_db(self, id):
        """Remove element from database by given id"""
        session = Session()

        try:
            to_del = session.query(Dbfile).filter_by(id=id).first()
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

    def get_files_list(self):
        """Get list of all files in the database"""
        session = Session()
        files = session.query(Dbfile).all()
        session.close()
        return files

    def get_amount(self):
        """Get amount of files in database"""
        session = Session()
        result = session.query(Dbfile).count()
        session.close()
        return result

    def remove_all(self):
        """Remove all elements from database"""
        session = Session()
        session.query(Dbfile).delete()
        session.commit()
        session.close()

    def get_path_by_id(self, id):
        session = Session()

        path = None
        try:
            file = session.query(Dbfile).filter_by(id=id).first()
            if file:
                path = file.path
            else:
                print("No such element in database.")
        except Exception as e:
            print("Error occurred while finging file by id:", str(e))
        finally:
            session.close()
            return path

    def change_existing(self, path):
        session = Session()
        session.close()

    def add_to_section(self):
        pass

    def get_data(self):
        pass

    def change_db_data(self):
        pass
    
