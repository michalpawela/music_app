from datetime import datetime
from functools import wraps
from flask import jsonify, Blueprint, request, current_app
from Models.UserModel import User
from flask import session
import jwt

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
    from app import bcrypt
    users = User.query.all()
    for user in users:
        if username == user.Username and bcrypt.check_password_hash(user.Password, password):
            return True
    return False


@auth.route("/login", methods=["POST"])
def login():
    from app import bcrypt
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