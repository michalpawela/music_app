from sqlalchemy import Column, Integer, String, Date, ForeignKey, DATE
from sqlalchemy.orm import relationship
from extensions import db
from .ArtistModel import Artist
from .GenreModel import Genre


class Album(db.Model):
    __tablename__ = "albums"

    albumId = Column("AlbumID", Integer, primary_key=True)
    title = Column("Title", String)
    publishingDate = Column("Publishing Date", DATE)

    # Foreign keys
    artistId = Column("ArtistID", Integer, ForeignKey("artists.ArtistID"))
    genreId = Column("GenreID", Integer, ForeignKey("genres.GenreID"))

    # Define a relationship to the Artist class
    artist = relationship('Artist', back_populates='albums')

    def __init__(self, title, publishingDate, artistId, genreId):
        self.title = title
        self.publishingDate = publishingDate
        self.artistId = artistId
        self.genreId = genreId
