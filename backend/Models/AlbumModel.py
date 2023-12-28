# AlbumModel.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from extensions import db
from .ArtistModel import Artist  # Make sure to import the Artist class


class Album(db.Model):
    __tablename__ = "albums"

    albumId = Column("AlbumID", Integer, primary_key=True)
    title = Column("Title", String)
    publishingDate = Column("Publishing Date", Date)

    # Foreign keys
    artistId = Column("ArtistID", Integer, ForeignKey("artists.arid"))
    genreId = Column("GenreID", Integer, ForeignKey("genres.arid"))

    def __init__(self, title, pubdate, arid):
        self.title = title
        self.publishingDate = pubdate
        self.arid = arid
