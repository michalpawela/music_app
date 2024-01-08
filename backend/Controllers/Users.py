from datetime import date, datetime
from functools import wraps
from flask import jsonify, Blueprint, request, current_app
from Models.UserModel import User
from extensions import db
from flask import session
import jwt

users = Blueprint("users", __name__)


@users.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
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
            existing_user.Password = password
        if email:
            existing_user.Email = email

        db.session.commit()

        user_data = {
            'Name': existing_user.Name,
            'Surname': existing_user.Surname,
            'Username': existing_user.Username,
            'Password': existing_user.Password,
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
    data = request.json
    name = data.get('Name')
    surname = data.get('Surname')
    username = data.get('Username')
    password = data.get('Password')
    email = data.get('Email')

    today = date.today()
    registration_date = today.strftime("%d-%m-%Y")

    new_user = User(Name=name, Surname=surname, Username=username, Password=password, Email=email, Registration_Date=registration_date)

    db.session.add(new_user)
    db.session.commit()

    user_data = {
        'Name': new_user.Name,
        'Surname': new_user.Surname,
        'Username': new_user.Username,
        'Password': new_user.Password,
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
            'Password': user.Password,
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
            'Password': user.Password,
            'Email': user.Email,
            'Registration_date': user.Registration_Date
        })
    return jsonify({'users': users_list})


auth = Blueprint("auth", __name__)


def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({'message': "A valid token is missing!"}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            username = data['Username']
            if username not in session:
                return jsonify({'message': "This user has no session!"}), 401
        except:
            return jsonify({"message": "Invalid token!"}), 401
        return func(*args, **kwargs)
    return decorator


def valid_email_and_password(username, password):
    users = User.query.all()
    for user in users:
        if username == user.Username and password == user.Password:
            return True
    return False


@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get('Username')
    password = data.get('Password')
    if not valid_email_and_password(username, password):
        return jsonify({'error': 'User not found'}), 404

    if username in session:
        session.pop(username)

    timestamp = datetime.now().timestamp()

    token = jwt.encode(
        {"Username": username, "time": timestamp},
        current_app.config["SECRET_KEY"],
        algorithm="HS256")

    session[username] = token

    return jsonify({"JWT": token}), 200


@auth.route("/logout", methods=["DELETE"])
@login_required
def logout():
    token = request.headers.get("Authorization")

    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        username = data['Username']
        if username in session:
            session.pop(username)
        else:
            return jsonify({'message': "This user has no session!"}), 401
    except:
        return jsonify({"message": "Invalid token!"}), 401

    return jsonify({'message': 'Session deleted successfully'}), 200
