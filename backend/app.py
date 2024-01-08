from flask import Flask
from Controllers.Albums import albums
from Controllers.Genres import genres
from Controllers.Artists import artists
from Controllers.Songs import songs
from Controllers.Playlists import playlists
from Controllers.Users import users, auth
from flask_swagger_ui import get_swaggerui_blueprint
from extensions import db
from flask_session import Session
from flask_bcrypt import Bcrypt


sess = Session()

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = 300
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
sess.init_app(app)
bcrypt = Bcrypt(app)


# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dupeczka1234@localhost/ppliowap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(albums, url_prefix="/albums")
app.register_blueprint(genres, url_prefix="/genres")
app.register_blueprint(artists, url_prefix="/artists")
app.register_blueprint(songs, url_prefix="/songs")
app.register_blueprint(playlists, url_prefix="/playlists")
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(auth, url_prefix="")
# Initialize the database with the Flask app

db.init_app(app)

app.run(debug=True)
