from flask import jsonify, Blueprint
from Models.AlbumModel import Album

albums = Blueprint("albums", __name__)


@albums.route('/get_all')
def get_all():
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