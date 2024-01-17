from flask import jsonify, Blueprint, request
from sqlalchemy.exc import IntegrityError
from Services import ArtistService

artists = Blueprint("artists", __name__)


@artists.route('/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    data = request.json
    full_name = data.get('Full_Name')
    country = data.get('Country')
    photo = data.get('Photo')
    genre_id = data.get('GenreID')

    artist_data = ArtistService.update_artist(artist_id, full_name, country, photo, genre_id)

    if artist_data is None:
        return jsonify({'error': 'Artist not found'}), 404
    else:
        return jsonify({'artist': artist_data}), 200


@artists.route('/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = ArtistService.delete_artist(artist_id)
    if artist is None:
        return jsonify({'error': 'Artist not found'}), 404
    else:
        return jsonify({'message': 'Artist deleted successfully'}), 200


@artists.route('/', methods=['POST'])
def create_artist():
    data = request.json
    full_name = data.get('Full_Name')
    country = data.get('Country')
    photo = data.get('Photo')
    genre_id = data.get('GenreID')

    artist_data = ArtistService.create_artist(full_name, country, photo, genre_id)
    if artist_data is IntegrityError:
        return jsonify({'error': 'IntegrityError: Genre not found'}), 404
    else:
        return jsonify({'artist': artist_data}), 201


@artists.route('/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist_data = ArtistService.get_artist(artist_id)

    if artist_data:
        return jsonify({'artist': artist_data})
    else:
        return jsonify({'error': 'Artist not found'}), 404


@artists.route('/', methods=['GET'])
def get_artists():
    artists_list = ArtistService.get_artists()
    return jsonify({'artists': artists_list})
