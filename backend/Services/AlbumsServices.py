from sqlalchemy.orm.exc import NoResultFound
from Models.AlbumModel import Album
from extensions import db


async def update_album(album_id, title, publishingDate, cover, artistId, genreId):
    try:
        existing_album = Album.query.get(album_id)

        # Update the album attributes if the corresponding data is provided in the request
        if title:
            existing_album.Title = title
        if publishingDate:
            existing_album.Publishing_Date = publishingDate
        if cover:
            existing_album.Cover = cover
        if artistId:
            existing_album.ArtistID = artistId
        if genreId:
            existing_album.GenreID = genreId
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
    except NoResultFound:
        return NoResultFound


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
