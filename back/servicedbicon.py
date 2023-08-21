'''Work with database'''
from back.dbbase import Session, engine, Base, IntegrityError
from back.dbicon import DbIcon


class ServiceDbIcon:
    '''Operate with icons table'''

    def __init__(self) -> None:
        Base.metadata.create_all(engine)

    def add_to_db(self, icon):
        """Add given icon to the database"""
        session = Session()

        try:
            session.add(icon)
            session.commit()
            session.refresh(icon)
        except Exception as e:
            session.rollback()
            print("Error occurred during adding new icon:" + str(e))
        finally:
            session.close()

    def get_icons_list(self):
        """Get list of all icons in the database"""
        session = Session()
        files = session.query(DbIcon).all()
        session.close()
        return files

    def get_amount(self):
        """Get amount of files in database"""
        session = Session()
        result = session.query(DbIcon).count()
        session.close()
        return result

    def remove_all(self):
        """Remove all elements from database"""
        session = Session()
        session.query(DbIcon).delete()
        session.commit()
        session.close()

    def icon_for_extension(self, extension):
        """Return icon for extension. Returns None if not present"""
        session = Session()
        existing_icon = session.query(DbIcon).filter_by(extension=extension).first()
        session.close()
        return existing_icon