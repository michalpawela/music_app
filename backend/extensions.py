from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = SQLAlchemy()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()