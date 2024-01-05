from sqlalchemy import Column, Integer, String, ForeignKey
from extensions import db
from .GenreModel import Genre

class Artist(db.Model):
    __tablename__ = "artists"

    ArtistID = Column("ArtistID", Integer, primary_key=True)
    Full_Name = Column("Full name", String)
    Country = Column("Country", String)
    Photo = Column("Photo", String)
    # Foreign keys
    GenreID = Column("GenreID", ForeignKey(Genre.GenreID))

    def __init__(self, Full_Name, Country, Photo, GenreID):
        self.Full_Name = Full_Name
        self.Country = Country
        self.Photo = Photo
        self.GenreID = GenreID

