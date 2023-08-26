from sqlalchemy import Column, String, Integer
from back.dbbase import Base


class DbIcon(Base):
    __tablename__ = 'icons'

    id = Column(Integer, primary_key=True, autoincrement=True) # Don't know, what autoincr. is doing.
    icon_path = Column(String)
    extension = Column(String)

    def __init__(self, icon_path, extension):
        self.icon_path = icon_path
        self.extension = extension

    def __str__(self):
            """Make icon printable for debugging"""
            return (
                f"Icon(id={self.id}, "
                f"Icon(path={self.icon_path}, "
                f"extension={self.extension})"
    )

    def to_json(self):
        """Make icon serialisable for json"""
        return self.icon_path.split("\\")[-1] if self.icon_path else ""
