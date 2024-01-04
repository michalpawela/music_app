import os.path

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

data_directory = 'C:\\dataMusicProject'
covers_imgs_directory = os.path.join(data_directory, 'cover_imgs')
artists_imgs_directory = os.path.join(data_directory, 'artists_imgs')
songs_directory = os.path.join(data_directory, 'songs')
