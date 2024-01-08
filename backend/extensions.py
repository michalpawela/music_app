
import os.path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

data_directory = 'C:\\dataMusicApp'
songs_directory = os.path.join(data_directory, 'songs')
allowed_extensions = {'mp3'}

