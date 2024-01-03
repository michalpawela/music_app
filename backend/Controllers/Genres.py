from flask import jsonify, Blueprint, request
from Models.GenreModel import Genre # Assuming your model is in a module named 'models'
from extensions import db

genres = Blueprint("genres", __name__)


@genres.route('/<int:genre_id>', methods=['PUT'])
def update_genre(genre_id):
    data = request.json
    name = data.get('Name')

    existing_genre = Genre.query.get(genre_id)

    if existing_genre:
        if name:
            existing_genre.Name = name

        db.session.commit()

        genre_data = {
            'GenreID': existing_genre.GenreID,
            'Name': existing_genre.Name
        }

        return jsonify({'genre': genre_data}), 200
    else:
        return jsonify({'error': 'Genre not found'}), 404


@genres.route('/<int:genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre is None:
        return jsonify({'error': 'Genre not found'}), 404

    db.session.delete(genre)
    db.session.commit()

    return jsonify({'message': 'Genre deleted successfully'}), 200


@genres.route('/', methods=['POST'])
def create_genre():
    data = request.json
    name = data.get('Name')

    new_genre = Genre(Name=name)

    db.session.add(new_genre)
    db.session.commit()

    genre_data = {
        'Name': new_genre.Name
    }

    return jsonify({'genre': genre_data}), 201


@genres.route('/<int:genre_id>', methods=['GET'])
def get_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre:
        genre_data = {
            'GenreID': genre.GenreID,
            'Name': genre.Name
        }
        return jsonify({'genre': genre_data})
    else:
        return jsonify({'error': 'Genre not found'}), 404


@genres.route('/', methods=['GET'])
def get_genres():
    genres = Genre.query.all()
    genres_list = []
    for genre in genres:
        genres_list.append({
            'GenreID': genre.GenreID,
            'Name': genre.Name
        })
    return jsonify({'genres': genres_list})
