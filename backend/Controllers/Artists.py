from flask import jsonify, Blueprint, request
from Models.ArtistModel import Artist
from extensions import db


artists = Blueprint("artists", __name__)


@artists.route('/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    data = request.json
    full_name = data.get('Full_Name')
    country = data.get('Country')
    photo = data.get('Photo')
    genre_id = data.get('GenreID')

    existing_artist = Artist.query.get(artist_id)

    if existing_artist:
        if full_name:
            existing_artist.Full_Name = full_name
        if country:
            existing_artist.Country = country
        if photo:
            existing_artist.Photo = photo
        if genre_id:
            existing_artist.GenreID = genre_id

        db.session.commit()

        artist_data = {
            'Full_Name': existing_artist.Full_Name,
            'Country': existing_artist.Country,
            'Photo': existing_artist.Photo,
            'GenreID': existing_artist.GenreID
        }

        return jsonify({'artist': artist_data}), 200
    else:
        return jsonify({'error': 'Artist not found'}), 404


@artists.route('/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = Artist.query.get(artist_id)
    if artist is None:
        return jsonify({'error': 'Artist not found'}), 404

    db.session.delete(artist)
    db.session.commit()

    return jsonify({'message': 'Artist deleted successfully'}), 200


@artists.route('/', methods=['POST'])
def create_artist():
    data = request.json
    full_name = data.get('Full_Name')
    country = data.get('Country')
    photo = data.get('Photo')
    genre_id = data.get('GenreID')

    new_artist = Artist(Full_Name=full_name, Country=country, Photo=photo, GenreID=genre_id)

    db.session.add(new_artist)
    db.session.commit()

    artist_data = {
        'Full_Name': new_artist.Full_Name,
        'Country': new_artist.Country,
        'Photo': new_artist.Photo,
        'GenreID': new_artist.GenreID
    }

    return jsonify({'artist': artist_data}), 201


@artists.route('/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist = Artist.query.get(artist_id)

    if artist:
        artist_data = {
            'ArtistID': artist.ArtistID,
            'Full_Name': artist.Full_Name,
            'Country': artist.Country,
            'Photo': artist.Photo,
            'GenreID': artist.GenreID
        }
        return jsonify({'artist': artist_data})
    else:
        return jsonify({'error': 'Artist not found'}), 404


@artists.route('/', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    artists_list = []
    for artist in artists:
        artists_list.append({
            'ArtistID': artist.ArtistID,
            'Full_Name': artist.Full_Name,
            'Country': artist.Country,
            'Photo': artist.Photo,
            'GenreID': artist.GenreID
        })
    return jsonify({'artists': artists_list})
