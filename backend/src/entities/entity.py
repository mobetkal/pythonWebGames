# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'pythonGames'
db_user = 'app_user'
db_password = 'app_user'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Abstract entity
class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)

    def __init__(self):
        self.created_at = datetime.now()
