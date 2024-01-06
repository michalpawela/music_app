from flask import jsonify, Blueprint, request
from Models.PlaylistModel import Playlist
from extensions import db

playlists = Blueprint("playlists", __name__)


@playlists.route('/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    data = request.json
    name = data.get('Name')
    userId = data.get('UserID')

    existing_playlist = Playlist.query.get(playlist_id)

    if existing_playlist:
        if name:
            existing_playlist.Name = name
        if userId:
            existing_playlist.UserID = userId

        db.session.commit()

        playlist_data = {
            'PlaylistID': existing_playlist.PlaylistID,
            'Name': existing_playlist.Name,
            'UserID': existing_playlist.UserID
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
        playlist_data = {
            'PlaylistID': playlist.PlaylistID,
            'Name': playlist.Name,
            'UserID': playlist.UserID
        }
        return jsonify({'playlist': playlist_data})
    else:
        return jsonify({'error': 'Playlist not found'}), 404


@playlists.route('/', methods=['GET'])
def get_playlists():
    playlists = Playlist.query.all()
    playlists_list = []
    for playlist in playlists:
        playlists_list.append({
            'PlaylistID': playlist.PlaylistID,
            'Name': playlist.Name,
            'UserID': playlist.UserID
        })
    return jsonify({'playlists': playlists_list})
