from sqlalchemy import Column, String, Integer

from back.Controllers.dbbase import Base


class Dbfile(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    path = Column(String, unique=True)
    file_name = Column(String)
    icon_name = Column(String)
    section_name = Column(String)

    def __init__(self, path, file_name, icon_name, section_name):
        self.path = path
        self.file_name = file_name
        self.icon_name = icon_name
        self.section_name = section_name