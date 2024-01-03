from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DATE, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2

conn = psycopg2.connect(host = "localhost",
                        dbname = "ppliowap",
                        user = "postgres",
                        password = "ppliowap",
                        port = 5432)

conn.close()

Base = declarative_base()

#user-created classes
class User(Base):
    __tablename__ = "users"
    
    UserID = Column("UserID", Integer, primary_key=True)
    Name = Column("Name", String)
    Surname = Column("Surname", String)
    Username = Column("Username", String)
    Password = Column("Password", String)
    Email = Column("Email", String)
    Registration_Date = Column("Registration Date", String)
    #Foreign keys


    def __init__(self,UserID,Name,Surname,Username,Password,Email,Registration_Date):
        
        self.UserID = UserID
        self.Name = Name
        self.Surname = Surname
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.Registration_Date = Registration_Date
        
        
#programmer-created classes
class Genre(Base):
    __tablename__ = "genres"  
    
    GenreID = Column("GenreID", Integer, primary_key=True)
    Name = Column("Name", String)
    
    #Foreign keys 

    
    def __init__(self,GenreID,Name):
        
        self.GenreID = GenreID
        self.Name = Name


class Artist(Base):
    __tablename__ = "artists"  
    
    ArtistID = Column("ArtistID", Integer, primary_key=True)
    Full_Name = Column("Full name", String)  
    Country = Column("Country", String)
    PhotoPath = Column("PhotoPath", String)
    #Foreign keys
    GenreID = Column("GenreID", ForeignKey(Genre.GenreID))
    
    def __init__(self,ArtistID,Full_Name,Country,Album_Count,Photo,GenreID):
        
        self.ArtistID = ArtistID
        self.Full_Name = Full_Name
        self.Country = Country
        self.Photo = Photo
        self.GenreID = GenreID
        
    def __repr__(self):
        return f"{self.Full_Name} from {self.Country} has {self.Album_Count} albums available"


class Album(Base):
    __tablename__ = "albums"
    
    AlbumID = Column("AlbumID", Integer, primary_key=True)
    Title = Column("Title", String)
    Publishing_Date = Column("Publishing Date", String)
    CoverPath = Column("Cover Path", String)
    #Foreign keys
    ArtistID = Column("ArtistID", ForeignKey(Artist.ArtistID))
    GenreID = Column("GenreID", ForeignKey(Genre.GenreID))    
    
    def __init__(self,AlbumID,Title,Publishing_Date,Cover,ArtistID,GenreID):
        
        self.AlbumID = AlbumID
        self.Title = Title
        self.Publishing_Date = Publishing_Date
        self.Cover = Cover
        self.ArtistID = ArtistID
        self.GenreID = GenreID


songPlaylistAssociation = Table(
    'Song Playlist Association',
    Base.metadata,
    Column('SongID', Integer, ForeignKey('songs.SongID')),
    Column('PlaylistID', Integer, ForeignKey('playlists.PlaylistID'))
)


class Song(Base):
    __tablename__ = "songs"
    
    SongID = Column("SongID", Integer, primary_key=True)
    Title = Column("Title", String)
    Upload_Date = Column("Upload Date", String)
    Song_Filepath = Column("Song Filepath", String)
    Description = Column("Description", String)
    #Foreign keys
    ArtistID = Column("ArtistID", ForeignKey(Artist.ArtistID))
    AlbumID = Column("AlbumID", ForeignKey(Album.AlbumID))
    
    def __init__(self,SongID,Title,Upload_Date,Song_Filepath,ArtistID,AlbumID):
    
        self.SongID = SongID
        self.Title = Title
        self.Upload_Date = Upload_Date
        self.Song_Filepath = Song_Filepath
        self.ArtistID = ArtistID
        self.AlbumID = AlbumID

    playlists = relationship('Playlist', secondary=songPlaylistAssociation, back_populates='songs')


class Playlist(Base):
    __tablename__ = "playlists"
    
    PlaylistID = Column("PlaylistID", Integer, primary_key=True)
    Name = Column("Name", String)

    #Foreign keys
    UserID = Column("UserID", ForeignKey(User.UserID))
    
    def __init__(self,PlaylistID,Name,UserID,SongID):
        
        self.PlaylistID = PlaylistID
        self.Name = Name
        self.UserID = UserID

    songs = relationship('Song', secondary=songPlaylistAssociation, back_populates='playlists')


engine = create_engine('postgresql://postgres:Dupeczka1234@localhost/ppliowap', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


gen1 = Genre(101, "Hip-Hop")
gen2 = Genre(102, "Pop")
gen3 = Genre(103, "Rock")

ar1 = Artist(101, "Grubson", "Poland", 6, "./artists/grubson.jpg", 101)
ar2 = Artist(102, "Adi Nowak", "Poland", 5, "./artists/adinowak.jpg", 101)
ar3 = Artist(103, "Doja Cat", "USA", 3, "./artists/dojacat", 101)

session.add_all([gen1, gen2, gen3, ar1, ar2, ar3])
# song1 = Song(101, "Emotikony", "2020", "./songs/emotikony.mp3")
# song2 = Song(102, "Na szczycie" "2009", "./songs/naszczycie.mp3")
# song3 = Song(103, "Nie, nie, nie", "2009", "./songs/nienienie.mp3")

# song4 = Song(104, "Strach na wróble", "2017", "./songs/strachnawroble.mp3")
# song5 = Song(105, "Zohan", "2017", "./songs/zohan.mp3")
# song6 = Song(106, "Placebo", "2018", "./songs/placebo.mp3")

# song7 = Song(107, "I paint the town red", "2023", "./songs/ipaintthetownred.mp3")
# song8 = Song(108, "Demons", "2023", "./songs/demons.mp3")
# song9 = Song(109, "Say so", "2020", "./songs/sayso.mp3")

# song10 = Song(110, "Nie kłami", "2018", )

session.commit()

