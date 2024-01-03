from sqlalchemy import Column, Integer, String, Date, ForeignKey, DATE
from sqlalchemy.orm import relationship
from extensions import db
from .ArtistModel import Artist
from .GenreModel import Genre


class Album(db.Model):
    __tablename__ = "albums"

    AlbumID = Column("AlbumID", Integer, primary_key=True)
    Title = Column("Title", String)
    Publishing_Date = Column("Publishing Date", String)
    CoverPath = Column("Cover Path", String)
    # Foreign keys
    ArtistID = Column("ArtistID", ForeignKey(Artist.ArtistID))
    GenreID = Column("GenreID", ForeignKey(Genre.GenreID))

    def __init__(self, AlbumID, Title, Publishing_Date, Cover, ArtistID, GenreID):
        self.AlbumID = AlbumID
        self.Title = Title
        self.Publishing_Date = Publishing_Date
        self.Cover = Cover
        self.ArtistID = ArtistID
        self.GenreID = GenreID
