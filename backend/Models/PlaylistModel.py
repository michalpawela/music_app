from sqlalchemy import Column, Integer, String, Date, ForeignKey, DATE
from sqlalchemy.orm import relationship
from extensions import db
from .UserModel import User

class Playlist(db.Model):
    __tablename__ = "playlists"

    PlaylistID = Column("PlaylistID", Integer, primary_key=True)
    Name = Column("Name", String)

    # Foreign keys
    UserID = Column("UserID", ForeignKey(User.UserID))

    def __init__(self, Name, UserID):
        self.Name = Name
        self.UserID = UserID
