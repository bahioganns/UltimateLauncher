from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

engine = create_engine("sqlite:///memory", echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()