from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DATE
from extensions import Base

class Artist(Base):
    __tablename__ = "artists"

    arid = Column("ArtistID", Integer, primary_key=True)
    fullname = Column("Full name", String)
    genre = Column("Genre", String)
    country = Column("Country", String)
    albumCnt = Column("Album Count", Integer)

    # Foreign keys

    def __init__(self, arid, fullname, genre, country, albumCnt):
        self.arid = arid
        self.fullname = fullname
        self.genre = genre
        self.country = country
        self.albumCnt = albumCnt

    def __repr__(self):
        return f"{self.fullname} from {self.country} plays {self.genre} and has {self.albumCnt} albums available"