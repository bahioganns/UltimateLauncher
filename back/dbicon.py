from sqlalchemy import Column, String, Integer
from back.dbbase import Base


class DbIcon(Base):
    __tablename__ = 'icons'

    id = Column(Integer, primary_key=True, autoincrement=True) # Don't know, what autoincr. is doing.
    bin_icon = Column(String)
    extension = Column(String)

    def __init__(self, bin_icon, extension):
        self.bin_icon = bin_icon
        self.extension = extension

    def __str__(self):
            """Make icon printable for debugging"""
            return (
                f"Icon(id={self.id}, "
                f"Icon(bin={self.bin_icon}, "
                f"extension={self.extension})"
    )

    def bin_json(self):
        """Make icon serialisable for json"""
        return str(self.bin_icon)
