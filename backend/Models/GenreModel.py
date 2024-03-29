from sqlalchemy import Column, Integer, String
from extensions import db


class Genre(db.Model):
    __tablename__ = "genres"

    GenreID = Column("GenreID", Integer, primary_key=True)
    Name = Column("Name", String)

    # Foreign keys

    def __init__(self, Name):
        self.Name = Name
