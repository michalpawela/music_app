from sqlalchemy import Column, Integer, String, Date, ForeignKey, DATE
from sqlalchemy.orm import relationship
from extensions import db


class Song(Base):
    __tablename__ = "songs"

    SongID = Column("SongID", Integer, primary_key=True)
    Title = Column("Title", String)
    Upload_Date = Column("Upload Date", String)
    Song_Filepath = Column("Song Filepath", String)
    Description = Column("Description", String)
    # Foreign keys
    ArtistID = Column("ArtistID", ForeignKey(Artist.ArtistID))
    AlbumID = Column("AlbumID", ForeignKey(Album.AlbumID))

    def __init__(self, SongID, Title, Upload_Date, Song_Filepath, ArtistID, AlbumID):
        self.SongID = SongID
        self.Title = Title
        self.Upload_Date = Upload_Date
        self.Song_Filepath = Song_Filepath
        self.ArtistID = ArtistID
        self.AlbumID = AlbumID

    playlists = relationship('Playlist', secondary=songPlaylistAssociation, back_populates='songs')
