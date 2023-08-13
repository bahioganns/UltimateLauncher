from sqlalchemy import Column, String, Integer
import os.path
from back.dbbase import Base

class Dbfile(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    path = Column(String, unique=True)
    name = Column(String)
    icon_name = Column(String)
    section_name = Column(String)

    def __init__(self, path, name=None, icon_name=None, section_name=None):
        self.path = path
        self.name = name if name else os.path.basename(path)
        self.icon_name = icon_name if icon_name else "placeholder"
        self.section_name = section_name if section_name else "all"
    
    def to_json(self):
        return {
            "path" : self.path,
            "name" : self.name,
            "icon_name" : self.icon_name,
            "section_name" : self.section_name,
        }