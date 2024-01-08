from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from extensions import db
from .UserModel import User
from .SongPlaylistAssociation import songPlaylistAssociation

class Playlist(db.Model):
    __tablename__ = "playlists"

    PlaylistID = Column("PlaylistID", Integer, primary_key=True)
    Name = Column("Name", String)

    # Foreign keys
    UserID = Column("UserID", ForeignKey(User.UserID))

    def __init__(self, Name, UserID):
        self.Name = Name
        self.UserID = UserID

    songs = relationship('Song', secondary=songPlaylistAssociation, back_populates='playlists')