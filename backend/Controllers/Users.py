from datetime import date
from flask import jsonify, Blueprint, request
from Models.UserModel import User
from extensions import db


users = Blueprint("users", __name__)


@users.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    from app import bcrypt
    data = request.json
    name = data.get('Name')
    surname = data.get('Surname')
    username = data.get('Username')
    password = data.get('Password')
    email = data.get('Email')

    existing_user = User.query.get(user_id)

    if existing_user:
        if name:
            existing_user.Name = name
        if surname:
            existing_user.Surname = surname
        if username:
            existing_user.Username = username
        if password:
            existing_user.Password = bcrypt.generate_password_hash(password).decode('utf-8')
        if email:
            existing_user.Email = email

        db.session.commit()

        user_data = {
            'Name': existing_user.Name,
            'Surname': existing_user.Surname,
            'Username': existing_user.Username,
            'Email': existing_user.Email
        }

        return jsonify({'user': user_data}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@users.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200


@users.route('/', methods=['POST'])
def create_user():
    from app import bcrypt
    data = request.json
    name = data.get('Name')
    surname = data.get('Surname')
    username = data.get('Username')
    password = data.get('Password')
    email = data.get('Email')

    today = date.today()
    registration_date = today.strftime("%d-%m-%Y")

    new_user = User(Name=name, Surname=surname, Username=username, Password=bcrypt.generate_password_hash(password).decode('utf-8'), Email=email, Registration_Date=registration_date)

    db.session.add(new_user)
    db.session.commit()

    user_data = {
        'Name': new_user.Name,
        'Surname': new_user.Surname,
        'Username': new_user.Username,
        'Email': new_user.Email,
        'Registration_date': new_user.Registration_Date
    }

    return jsonify({'user': user_data}), 201


@users.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            'UserID': user.UserID,
            'Name': user.Name,
            'Surname': user.Surname,
            'Username': user.Username,
            'Email': user.Email,
            'Registration_date': user.Registration_Date
        }
        return jsonify({'user': user_data})
    else:
        return jsonify({'error': 'User not found'}), 404


@users.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            'UserID': user.UserID,
            'Name': user.Name,
            'Surname': user.Surname,
            'Username': user.Username,
            'Email': user.Email,
            'Registration_date': user.Registration_Date
        })
    return jsonify({'users': users_list})



