from sqlalchemy import Column, String, Integer
from back.dbbase import Base


class DbIcon(Base):
    __tablename__ = 'icons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bin_icon = Column(String)
    extension = Column(String)

    def __init__(self, bin_icon, extension):
        self.bin_icon = bin_icon
        self.extension = extension

    def __str__(self):
            return (
                f"Icon(id={self.id}, "
                f"Icon(bin={self.bin_icon}, "
                f"extension={self.extension})"
    )