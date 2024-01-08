from flask import jsonify, Blueprint, request
from Models.PlaylistModel import Playlist
from Models.SongModel import Song
from extensions import db

playlists = Blueprint("playlists", __name__)


@playlists.route('/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    data = request.json
    name = data.get('Name')

    existing_playlist = Playlist.query.get(playlist_id)

    if existing_playlist:
        if name:
            existing_playlist.Name = name

        db.session.commit()

        playlist_data = {
            'PlaylistID': existing_playlist.PlaylistID,
            'Name': existing_playlist.Name,
        }

        return jsonify({'playlist': playlist_data}), 200
    else:
        return jsonify({'error': 'Playlist not found'}), 404


@playlists.route('/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if playlist is None:
        return jsonify({'error': 'Playlist not found'}), 404

    db.session.delete(playlist)
    db.session.commit()

    return jsonify({'message': 'Playlist deleted successfully'}), 200


@playlists.route('/', methods=['POST'])
def create_playlist():
    data = request.json
    name = data.get('Name')
    userId = data.get('UserID')

    new_playlist = Playlist(Name=name, UserID=userId)

    db.session.add(new_playlist)
    db.session.commit()

    playlist_data = {
        'Name': new_playlist.Name,
        'UserID': new_playlist.UserID
    }

    return jsonify({'playlist': playlist_data}), 201


@playlists.route('/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if playlist:
        songs_data = []
        for song in playlist.songs:
            song_data = {
                'SongID': song.SongID,
                'Title': song.Title,
                'Upload_Date': song.Upload_Date,
                'Description': song.Description,
                'ArtistID': song.ArtistID,
                'AlbumID': song.AlbumID
            }
            songs_data.append(song_data)

        playlist_data = {
            'PlaylistID': playlist.PlaylistID,
            'Name': playlist.Name,
            'UserID': playlist.UserID,
            'Songs': songs_data

        }
        return jsonify({'playlist': playlist_data})
    else:
        return jsonify({'error': 'Playlist not found'}), 404


@playlists.route('/', methods=['GET'])
def get_playlists():
    playlists = Playlist.query.all()
    playlists_list = []
    for playlist in playlists:
        songs_data = []
        for song in playlist.songs:
            song_data = {
                'SongID': song.SongID,
                'Title': song.Title,
                'Upload_Date': song.Upload_Date,
                'Description': song.Description,
                'ArtistID': song.ArtistID,
                'AlbumID': song.AlbumID
            }
            songs_data.append(song_data)

        playlists_list.append({
            'PlaylistID': playlist.PlaylistID,
            'Name': playlist.Name,
            'UserID': playlist.UserID,
            'Songs': songs_data
        })
    return jsonify({'playlists': playlists_list})


@playlists.route('/add_song', methods=["POST"])
def add_song():
    data = request.json
    playlist_id = data.get('PlaylistID')
    song_id = data.get('SongID')
    playlist = Playlist.query.get(playlist_id)
    song = Song.query.get(song_id)

    playlist.songs.append(song)
    song.playlists.append(playlist)

    db.session.commit()
    return jsonify({'playlist':{'playlist_id': playlist_id, 'song_id': song_id}}), 200


@playlists.route('/remove_song', methods=["DELETE"])
def remove_song():
    data = request.json
    playlist_id = data.get('PlaylistID')
    song_id = data.get('SongID')
    playlist = Playlist.query.get(playlist_id)
    song = Song.query.get(song_id)

    playlist.songs.remove(song)

    db.session.commit()
    return jsonify({'playlist': {'playlist_id': playlist_id, 'song_id': song_id}}), 200
