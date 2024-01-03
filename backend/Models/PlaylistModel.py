from sqlalchemy import Column, Integer, String, Date, ForeignKey, DATE
from sqlalchemy.orm import relationship
from extensions import db


class Playlist(Base):
    __tablename__ = "playlists"

    PlaylistID = Column("PlaylistID", Integer, primary_key=True)
    Name = Column("Name", String)

    # Foreign keys
    UserID = Column("UserID", ForeignKey(User.UserID))

    def __init__(self, PlaylistID, Name, UserID, SongID):
        self.PlaylistID = PlaylistID
        self.Name = Name
        self.UserID = UserID

    songs = relationship('Song', secondary=songPlaylistAssociation, back_populates='playlists')