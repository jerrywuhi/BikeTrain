from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    ftp = db.Column(
        db.Integer,
        default=0
    )

    weight = db.Column(
        db.Float,
        default=0
    )

    def __repr__(self):
        return f'<User {self.username}>'