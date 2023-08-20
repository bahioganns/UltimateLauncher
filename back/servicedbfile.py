'''Work with database'''
from back.dbbase import Session, engine, Base, IntegrityError
from back.dbfile import DbFile


class ServiceDbFile:
    '''Operate with files table'''

    def __init__(self) -> None:
        Base.metadata.create_all(engine)

    def add_to_db(self, dbfile):
        """Add to database given file"""
        session = Session()

        try:
            session.add(dbfile)
            session.commit()
            session.refresh(dbfile)
        except IntegrityError:
            session.rollback()
            print("Element with the same path already exists.")
        finally:
            session.close()

    def del_from_db(self, id):
        """Remove element from database by given id"""
        session = Session()

        error = ""
        try:
            to_del = session.query(DbFile).filter_by(id=id).first()
            if to_del:
                session.delete(to_del)
                session.commit()
            else:
                error = "No such element in database."
        except Exception as e:
            session.rollback()
            error = "Error occurred during deletion:" + str(e)
        finally:
            session.close()
            return error

    def get_files_list(self):
        """Get list of all files in the database"""
        session = Session()
        files = session.query(DbFile).all()
        session.close()
        return files

    def get_amount(self):
        """Get amount of files in database"""
        session = Session()
        result = session.query(DbFile).count()
        session.close()
        return result

    def remove_all(self):
        """Remove all elements from database"""
        session = Session()
        session.query(DbFile).delete()
        session.commit()
        session.close()

    def get_path_by_id(self, id):
        """Get path from db by given id"""
        session = Session()

        path = None
        try:
            file = session.query(DbFile).filter_by(id=id).first()
            if file:
                path = file.path
            else:
                print("No such element in database.")
        except Exception as e:
            print("Error occurred while finging file by id:", str(e))
        finally:
            session.close()
            return path
    
    def change_name(self, id, new_name):
        """Change name of file by given id"""
        session = Session()

        error = ""
        if not new_name:
            return "Name can't be empty"

        try:
            record = session.query(DbFile).filter_by(id=id).first()
            if record:
                record.name = new_name
                session.commit()
            else:
                error = "Can't find file with this id"
        except Exception as e:
            session.rollback()
            error = "Error occurred while changing name by id:" + str(e)
        finally:
            session.close()
            return error
        
    
