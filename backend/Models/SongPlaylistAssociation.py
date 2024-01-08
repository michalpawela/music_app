from sqlalchemy import ForeignKey, Column, Integer, Table
from extensions import db

songPlaylistAssociation = Table(
    'Song Playlist Association',
    db.Model.metadata,
    Column('SongID', Integer, ForeignKey('songs.SongID')),
    Column('PlaylistID', Integer, ForeignKey('playlists.PlaylistID'))
)