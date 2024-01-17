from flask import jsonify, Blueprint, request
from sqlalchemy.exc import IntegrityError
from Services import SongService

songs = Blueprint("songs", __name__)


@songs.route('/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song_data = SongService.get_song(song_id)
    if song_data is None:
        return jsonify({'error': 'Song not found'}), 404
    else:
        return jsonify({'songs': song_data}), 200


@songs.route('/artist/<int:artist_id>', methods=['GET'])
def get_songs_for_artist(artist_id):
    songs_list = SongService.get_songs_for_artist(artist_id)
    if songs_list is None:
        return jsonify({'error': 'Songs not found'}), 404
    else:
        return jsonify({'songs': songs_list}), 200


@songs.route('/genre/<int:genre_id>', methods=['GET'])
def get_songs_for_genre(genre_id):
    songs_list = SongService.get_songs_for_genre(genre_id)
    if songs_list is None:
        return jsonify({'error': 'Songs not found'}), 404
    else:
        return jsonify({'songs': songs_list}), 200


@songs.route('/', methods=['GET'])
def get_songs():
    songs_list = SongService.get_songs()
    if songs_list is None:
        return jsonify({'error': 'Songs not found'}), 404
    else:
        return jsonify({'songs': songs_list}), 200


@songs.route('/', methods=['POST'])
def create_song():
    data = request.json

    title = data.get('Title')
    description = data.get('Description')
    artist_id = data.get('ArtistID')
    album_id = data.get('AlbumID')
    song_base64 = data.get('Song')

    song_data = SongService.create_song(title, description, artist_id, album_id, song_base64)

    if song_data is IntegrityError:
        return jsonify({'error': 'IntegrityError: Artist or Album not found'}), 404
    else:
        return jsonify({'song': song_data}), 201


@songs.route('/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    data = request.json
    title = data.get('Title')
    upload_date = data.get('Upload_Date')
    description = data.get('Description')
    artist_id = data.get('ArtistID')
    album_id = data.get('AlbumID')
    song_base64 = data.get('Song')

    song_data = SongService.update_song(song_id, title, upload_date, description, artist_id, album_id, song_base64)

    if song_data is IntegrityError:
        return jsonify({'error': 'IntegrityError: Artist or Album not found'}), 404
    elif song_data is None:
        return jsonify({'error': 'Song not found'}), 404
    else:
        return jsonify({'song': song_data}), 200


@songs.route('/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    song = SongService.delete_song(song_id)

    if song is None:
        return jsonify({'error': 'Song not found'}), 404
    else:
        return jsonify({'message': 'Song deleted successfully'}), 200
