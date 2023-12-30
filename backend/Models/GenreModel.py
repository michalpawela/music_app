from sqlalchemy import Column, Integer, String, Date, ForeignKey, DATE
from sqlalchemy.orm import relationship
from extensions import db


class Genre(db.Model):
    __tablename__ = "genres"

    genreId = Column("GenreID", Integer, primary_key=True)
    name = Column("Name", String)


    def __init__(self, genreId, name):
        self.gid = genreId
        self.name = name
