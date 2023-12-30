from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from extensions import db


class Artist(db.Model):
    __tablename__ = "artists"

    arid = Column("ArtistID", Integer, primary_key=True)
    fullname = Column("Full name", String)
    genre = Column("Genre", String)
    country = Column("Country", String)
    albumCnt = Column("Album Count", Integer)

    # Define a relationship to the Album class
    albums = relationship('Album', back_populates='artist')

    def __init__(self, arid, fullname, genre, country, albumCnt):
        self.arid = arid
        self.fullname = fullname
        self.genre = genre
        self.country = country
        self.albumCnt = albumCnt

    def __repr__(self):
        return f"{self.fullname} from {self.country} plays {self.genre} and has {self.albumCnt} albums available"
