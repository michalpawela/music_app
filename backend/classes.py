from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#user-created classes
class User(Base):
    __tablename__ = "user"
    
    uid = Column("UserID", Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    username = Column("Username", String)
    email = Column("Email", String)
    regdate = Column("Registration Date", date)
    #Foreign keys
    
class Playlist(Base):
    __tablename__ = "playlist"
    
    pid = Column("PlaylistID", Integer, primary_key=True)
    name = Column("Name", String)

    #Foreign keys
    uid = Column("UserID", Integer, ForeignKey(user.uid))
    sid = Column("SongID", Integer, ForeignKey(song.sid))
    
    def __init__(self,pid,name):
        
        self.pid = pid
        self.name = name
    

#programmer-created classes
 
class Artist(Base):
    __tablename__ = "artist"  
    
    arid = Column("ArtistID", Integer, primary_key=True)
    fullname = Column("Full name", String)  
    genre = Column("Genre", String)
    country = Column("Country", String)
    albumCnt = Column("Album Count", Integer)
    #Foreign keys
    
    
    def __init__(self,arid,fullname,genre,country,albumCnt):
        
        self.arid = arid
        self.fullname = fullname
        self.genre = genre
        self.country = country
        self.albumCnt = albumCnt
        
    def __repr__(self):
        return f"{self.fullname} from {self.country} plays {self.genre} and has {self.albumCnt} albums available"

class Song(Base):
    __tablename__ = "song"
    
    sid = Column("SongID", Integer, primary_key=True)
    title = Column("Title", String)
    genre = Column("Genre", String)
    uploadDate = Column("Upload Date", date)
    path = Column("Filepath", String)
    #Foreign keys
    arid = Column("ArtistID", String, ForeignKey(Artist.arid))


class Genre(Base):
    __tablename__ = "genre"  
    
    gid = Column("GenreID", Integer, primary_key=True)
    name = Column("Name", String)
    
    #Foreign keys 
    arid = Column("ArtistID", String, ForeignKey(Artist.arid))
    
    def __init__(self,gid,name):
        
        self.gid = gid
        self.name = name


class Album(Base):
    __tablename__ = "album"
    
    alid = Column("AlbumID", Integer, primary_key=True)
    title = Column("Title", String)
    pubdate = Column("Publishing Date", date)
    #Foreign keys
    arid = Column("ArtistID", Integer, ForeignKey(Artist.arid))
    gid = Column("GenreID", Integer, ForeignKey(Genre.gid))    
    
    def __init__(self,alid,title,pubdate):
        
        self.alid = alid
        self.title = title
        self.pubdate = pubdate






