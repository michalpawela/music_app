from flask import jsonify, Blueprint, request
from Models.AlbumModel import Album
from extensions import db

albums = Blueprint("albums", __name__)


@albums.route('/<int:album_id>', methods=['PUT'])
def update_album(album_id):
    # Get data from the request
    data = request.json  # Assuming the data is sent in JSON format
    title = data.get('Title')
    publishingDate = data.get('PublishingDate')
    artistId = data.get('ArtistID')
    genreId = data.get('GenreID')

    # Find the existing album in the database
    existing_album = Album.query.get(album_id)

    # Check if the album exists
    if existing_album:
        # Update the album attributes if the corresponding data is provided in the request
        if title:
            existing_album.title = title
        if publishingDate:
            existing_album.publishingDate = publishingDate
        if artistId:
            existing_album.artistId = artistId
        if genreId:
            existing_album.genreId = genreId

        # Commit the changes to the database
        db.session.commit()

        # Return the updated album data
        album_data = {
            'Title': existing_album.title,
            'PublishingDate': existing_album.publishingDate,
            'ArtistID': existing_album.artistId,
            'GenreID': existing_album.genreId
        }

        return jsonify({'album': album_data}), 200  # 200 OK status code
    else:
        return jsonify({'error': 'Album not found'}), 404  # 404 Not Found status code


@albums.route('/<int:album_id>', methods=['DELETE'])
def delete_album(album_id):
    # Check if the album exists
    album = Album.query.get(album_id)
    if album is None:
        return jsonify({'error': 'Album not found'}), 404  # 404 Not Found status code

    # Delete the album from the database
    db.session.delete(album)
    db.session.commit()

    return jsonify({'message': 'Album deleted successfully'}), 200  # 200 OK status code


@albums.route('/', methods=['POST'])
def create_album():
    # Get data from the request
    data = request.json  # Assuming the data is sent in JSON format
    title = data.get('Title')
    publishingDate = data.get('PublishingDate')
    artistId = data.get('ArtistID')
    genreId = data.get('GenreID')

    # Validate data (you might want to add more validation based on your requirements)

    # Create a new album object
    new_album = Album(title=title, publishingDate=publishingDate, artistId=artistId, genreId=genreId)

    # Add the new album to the database
    db.session.add(new_album)
    db.session.commit()

    # Return the created album data
    album_data = {
        'Title': new_album.title,
        'PublishingDate': new_album.publishingDate,
        'ArtistID': new_album.artistId,
        'GenreID': new_album.genreId
    }

    return jsonify({'album': album_data}), 201  # 201 Created status code


@albums.route('/<int:album_id>', methods=['GET'])
def get_album(album_id):
    album = Album.query.get(album_id)
    if album:
        album_data = {
            'AlbumID': album.albumId,
            'Title': album.title,
            'PublishingDate': str(album.publishingDate),
            'ArtistID': album.artistId,
            'GenreID': album.genreId
        }
        return jsonify({'album': album_data})
    else:
        return jsonify({'error': 'Album not found'}), 404


@albums.route('/', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    # Serialize data into JSON
    albums_list = []
    for album in albums:
        albums_list.append({
            'AlbumID': album.albumId,
            'Title': album.title,
            'PublishingDate': str(album.publishingDate),
            'ArtistID': album.artistId,
            'GenreID': album.genreId
        })
    return jsonify({'albums': albums_list})