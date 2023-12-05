from flask_sqlalchemy import SQLAlchemy

# create database
db = SQLAlchemy()

# connect app with databse.


def db_connect(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = "pets"

    def __repr__(self) -> str:
        """ Model attributes """
        return f"< id={Pet.id} | name={Pet.name} | species={Pet.species} | available={Pet.available} >"

    # set up attributes to turn into table columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
    notes = db.Column(db.Text, nullable=True)


class User(db.Model):
    __tablename__ = 'users'

    # set up attributes to turn into table columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    first_name = db.Column(db.Text, nullable=False, unique=False)
    last_name = db.Column(db.Text, nullable=True, unique=False)

    def __repr__(self) -> str:
        """ Model attributes """
        return f"< id={User.id} | username={User.username} | first_name={User.first_name} | last_name={User.last_name} >"
