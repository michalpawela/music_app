from sqlalchemy.exc import IntegrityError
from Models.ArtistModel import Artist
from extensions import db


def update_artist(artist_id, full_name, country, photo, genre_id):
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

    if existing_artist is None:
        return None
    else:
        return artist_data


def delete_artist(artist_id):
    artist = Artist.query.get(artist_id)
    if artist is None:
        return None
    else:
        db.session.delete(artist)
        db.session.commit()

        return artist


def create_artist(full_name, country, photo, genre_id):
    try:
        new_artist = Artist(Full_Name=full_name, Country=country, Photo=photo, GenreID=genre_id)

        db.session.add(new_artist)
        db.session.commit()

        artist_data = {
            'Full_Name': new_artist.Full_Name,
            'Country': new_artist.Country,
            'Photo': new_artist.Photo,
            'GenreID': new_artist.GenreID
        }
        return artist_data
    except IntegrityError:
        db.session.rollback()
        return IntegrityError


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
        return artist_data
    else:
        return None


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
    return artists_list
