from sqlalchemy.orm.exc import NoResultFound
from Models.AlbumModel import Album
from extensions import db


def update_album(album_id, title, publishing_date, cover, artist_id, genre_id):
    existing_album = Album.query.get(album_id)
    if existing_album is None:
        return None
    else:
        # Update the album attributes if the corresponding data is provided in the request
        if title:
            existing_album.Title = title
        if publishing_date:
            existing_album.Publishing_Date = publishing_date
        if cover:
            existing_album.Cover = cover
        if artist_id:
            existing_album.ArtistID = artist_id
        if genre_id:
            existing_album.GenreID = genre_id
        # Commit the changes to the database
        db.session.commit()
        # Return the updated album data
        album_data = {
            'Title': existing_album.Title,
            'Publishing_Date': existing_album.Publishing_Date,
            'Cover': existing_album.Cover,
            'ArtistID': existing_album.ArtistID,
            'GenreID': existing_album.GenreID
        }
        return album_data


def get_album(album_id):
    album = Album.query.get(album_id)
    if album is None:
        return None
    else:
        album_data = {
            'AlbumID': album.AlbumID,
            'Title': album.Title,
            'Publishing_Date': str(album.Publishing_Date),
            'Cover': album.Cover,
            'ArtistID': album.ArtistID,
            'GenreID': album.GenreID
        }
        return album_data


def get_albums():
    albums = Album.query.all()
    # Serialize data into JSON
    albums_list = []
    for album in albums:
        albums_list.append({
            'AlbumID': album.AlbumID,
            'Title': album.Title,
            'Publishing_Date': str(album.Publishing_Date),
            'Cover': album.Cover,
            'ArtistID': album.ArtistID,
            'GenreID': album.GenreID
        })
    return albums_list


def delete_album(album_id):
    # Check if the album exists
    album = Album.query.get(album_id)
    if album is None:
        return None
    else:
        # Delete the album from the database
        db.session.delete(album)
        db.session.commit()

        return album


def create_album(title, publishing_date, cover, artist_id, genre_id):
    # Create a new album object
    new_album = Album(Title=title, Publishing_Date=publishing_date, Cover=cover, ArtistID=artist_id, GenreID=genre_id)

    # Add the new album to the database
    db.session.add(new_album)
    db.session.commit()

    # Return the created album data
    album_data = {
        'Title': new_album.Title,
        'Publishing_Date': new_album.Publishing_Date,
        'Cover': new_album.Cover,
        'ArtistID': new_album.ArtistID,
        'GenreID': new_album.GenreID
    }

    return album_data
