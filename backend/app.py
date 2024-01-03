from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Controllers.Albums import albums
from Controllers.Genres import genres
from Controllers.Artists import artists
from extensions import db
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app = Flask(__name__)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dupeczka1234@localhost/ppliowap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(albums, url_prefix="/albums")
app.register_blueprint(genres, url_prefix="/genres")
app.register_blueprint(artists, url_prefix="/artists")
# Initialize the database with the Flask app

db.init_app(app)


app.run(debug=True)
