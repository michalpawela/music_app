from flask import jsonify, Blueprint, request
from Models.AlbumModel import Album
from extensions import db
from Services import AlbumService

albums = Blueprint("albums", __name__)


@albums.route('/<int:album_id>', methods=['PUT'])
def update_album(album_id):
    # Get data from the request
    data = request.json  # Assuming the data is sent in JSON format
    title = data.get('Title')
    publishingDate = data.get('Publishing_Date')
    cover = data.get('Cover')
    artistId = data.get('ArtistID')
    genreId = data.get('GenreID')

    # Find the existing album in the database
    album_data = AlbumService.update_album(album_id, title, publishingDate, cover, artistId, genreId)
    if album_data is None:
        return jsonify({'error': 'Album not found'}), 404  # 404 Not Found status code
    else:
        return jsonify({'album': album_data}), 200  # 200 OK status code


@albums.route('/<int:album_id>', methods=['DELETE'])
def delete_album(album_id):
    # Check if the album exists
    album = AlbumService.delete_album(album_id)
    if album is None:
        return jsonify({'error': 'Album not found'}), 404  # 404 Not Found status code
    else:
        return jsonify({'message': 'Album deleted successfully.'}), 200  # 200 OK status code


@albums.route('/', methods=['POST'])
def create_album():
    # Get data from the request
    data = request.json  # Assuming the data is sent in JSON format
    title = data.get('Title')
    publishingDate = data.get('Publishing_Date')
    cover = data.get('Cover')
    artistId = data.get('ArtistID')
    genreId = data.get('GenreID')

    album_data = AlbumService.create_album(title, publishingDate, cover, artistId, genreId)

    return jsonify({'album': album_data}), 201  # 201 Created status code


@albums.route('/<int:album_id>', methods=['GET'])
def get_album(album_id):
    album = AlbumService.get_album(album_id)

    if(album == None):
        return jsonify({'error': 'Album not found'}), 404

    return jsonify({'album': album}), 200


@albums.route('/', methods=['GET'])
def get_albums():
    albums_list = AlbumService.get_albums()
    return jsonify({'albums': albums_list})