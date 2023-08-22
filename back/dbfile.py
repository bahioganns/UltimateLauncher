from sqlalchemy import Column, String, Integer, ForeignKey
import os.path
from back.dbbase import Base
from sqlalchemy.orm import relationship
#from back.dbicon import DbIcon

class DbFile(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    path = Column(String, unique=True)
    name = Column(String)
    icon_id = Column(Integer, ForeignKey('icons.id'))
    icon = relationship("DbIcon", lazy="joined")
    section_name = Column(String)

    def __init__(self, path, name=None, section_name=None):
        self.path = path
        self.name = name if name else os.path.basename(path)
        self.section_name = section_name if section_name else "all"

    def __str__(self):
                return (
                    f"DbFile(id={self.id}, "
                    f"path={self.path}, "
                    f"name={self.name}, "
                    f"name={self.icon_id}, "
                    f"section_name={self.section_name})"
        )
    
    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "icon_path" : self.icon.to_json(),
            "section_name" : self.section_name,
        }
