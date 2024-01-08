import base64
import os
from datetime import date
from flask import jsonify, Blueprint, request
from Models.SongModel import Song
from Models.ArtistModel import Artist
from Models.AlbumModel import Album
from extensions import db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from extensions import songs_directory

songs = Blueprint("songs", __name__)


@songs.route('/<int:song_id>', methods=['GET'])
def get_song(song_id):
    try:
        song = Song.query.filter_by(SongID=song_id).one()
        song_file_path_base64 = song.Song_Filepath
        bytes_song = bytes.fromhex(song_file_path_base64.replace('\\x', ''))
        song_file_path = base64.b64decode(bytes_song)

        with open(song_file_path, "rb") as mp3_file:
            binary_song = mp3_file.read()
            song_base64 = base64.b64encode(binary_song)
            song_base64_str = song_base64.decode('utf-8')

        album = Album.query.filter_by(AlbumID=song.AlbumID).one()
        album_data = {
            'AlbumID': album.AlbumID,
            'Title': album.Title,
            'Publishing_Date': str(album.Publishing_Date),
            'Cover': album.Cover,
            'ArtistID': album.ArtistID,
            'GenreID': album.GenreID
        }

        artist = Artist.query.filter_by(ArtistID=song.ArtistID).one()
        artist_data = {
            'ArtistID': artist.ArtistID,
            'Full_Name': artist.Full_Name,
            'Country': artist.Country,
            'Photo': artist.Photo,
            'GenreID': artist.GenreID
        }

        songs_data = {
            'SongID': song.SongID,
            'Title': song.Title,
            'Upload_Date': song.Upload_Date,
            'Song': song_base64_str,
            'Description': song.Description,
            'Artist': artist_data,
            'Album': album_data
        }
        return jsonify({'songs': songs_data})
    except NoResultFound:
        return jsonify({'error': 'Song not found'}), 404


@songs.route('/', methods=['GET'])
def get_songs():
    songs_list = []

    for song in Song.query.all():

        song_file_path_base64 = song.Song_Filepath
        bytes_song = bytes.fromhex(song_file_path_base64.replace('\\x', ''))
        song_file_path = base64.b64decode(bytes_song)

        with open(song_file_path, "rb") as mp3_file:
            binary_song = mp3_file.read()
            song_base64 = base64.b64encode(binary_song)
            song_base64_str = song_base64.decode('utf-8')

        album = Album.query.filter_by(AlbumID=song.AlbumID).one()
        album_data = {
            'AlbumID': album.AlbumID,
            'Title': album.Title,
            'Publishing_Date': str(album.Publishing_Date),
            'Cover': album.Cover,
            'ArtistID': album.ArtistID,
            'GenreID': album.GenreID
        }
        artist = Artist.query.filter_by(ArtistID=song.ArtistID).one()
        artist_data = {
            'ArtistID': artist.ArtistID,
            'Full_Name': artist.Full_Name,
            'Country': artist.Country,
            'Photo': artist.Photo,
            'GenreID': artist.GenreID
        }


        songs_list.append({
            'SongID': song.SongID,
            'Title': song.Title,
            'Upload_Date': song.Upload_Date,
            'Song': song_base64_str,
            'Description': song.Description,
            'Artist': artist_data,
            'Album': album_data
        })
    return jsonify({'songs': songs_list})


@songs.route('/', methods=['POST'])
def create_song():
    data = request.json

    title = data.get('Title')
    description = data.get('Description')
    artist_id = data.get('ArtistID')
    album_id = data.get('AlbumID')
    song_base64 = data.get('Song')

    song_file_path = os.path.join(songs_directory, title + '.mp3')

    song_data = base64.b64decode(song_base64)
    with open(song_file_path, "wb") as mp3_file:
        mp3_file.write(song_data)

    song_file_path_base64 = base64.b64encode(song_file_path.encode("utf-8"))

    today = date.today()
    upload_date = today.strftime("%d-%m-%Y")

    new_song = Song(
        Title=title,
        Upload_Date=upload_date,
        Song_Filepath=song_file_path_base64,
        Description=description,
        ArtistID=artist_id,
        AlbumID=album_id
    )

    try:
        db.session.add(new_song)
        db.session.commit()

        song_data = {
            'Title': new_song.Title,
            'Upload_Date': new_song.Upload_Date,
            'Song_base64': song_base64,
            'Description': new_song.Description,
            'ArtistID': new_song.ArtistID,
            'AlbumID': new_song.AlbumID
        }
        return jsonify({'song': song_data}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'IntegrityError: Artist or Album not found'}), 404


@songs.route('/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    data = request.json
    title = data.get('Title')
    upload_date = data.get('Upload_Date')
    description = data.get('Description')
    artist_id = data.get('ArtistID')
    album_id = data.get('AlbumID')
    song_base64 = data.get('Song')

    try:
        existing_song = Song.query.filter_by(SongID=song_id).one()
        if title:
            existing_song.Title = title
        if upload_date:
            existing_song.Upload_Date = upload_date
        if song_base64:
            song_file_path = os.path.join(songs_directory, title + '.mp3')

            song_data = base64.b64decode(song_base64)
            with open(song_file_path, "wb") as mp3_file:
                mp3_file.write(song_data)

            song_file_path_base64 = base64.b64encode(song_file_path.encode("utf-8"))
            existing_song.Song_Filepath = song_file_path_base64
        if description:
            existing_song.Description = description
        if artist_id:
            existing_song.ArtistID = artist_id
        if album_id:
            existing_song.AlbumID = album_id

        db.session.commit()

        song_data = {
            'SongID': existing_song.SongID,
            'Title': existing_song.Title,
            'Upload_Date': existing_song.Upload_Date,
            'Song_Filepath': existing_song.Song_Filepath,
            'Description': existing_song.Description,
            'ArtistID': existing_song.ArtistID,
            'AlbumID': existing_song.AlbumID
        }

        return jsonify({'song': song_data}), 200
    except NoResultFound:
        return jsonify({'error': 'Song not found'}), 404


@songs.route('/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    try:
        song = Song.query.filter_by(SongID=song_id).one()
        db.session.delete(song)
        db.session.commit()
        return jsonify({'message': 'Song deleted successfully'}), 200
    except NoResultFound:
        return jsonify({'error': 'Song not found'}), 404
