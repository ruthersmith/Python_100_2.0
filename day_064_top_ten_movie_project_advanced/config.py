from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

    ##CREATE DATABASE
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie.db"
    # Optional: But it will silence the deprecation warning in the console.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialize extensions
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()
    

    return app