from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Controllers.Albums import albums
from extensions import db

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dupeczka1234@localhost/ppliowap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(albums, url_prefix="/albums")
# Initialize the database with the Flask app

db.init_app(app)


app.run(debug=True)
