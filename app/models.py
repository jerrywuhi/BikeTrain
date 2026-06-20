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
    monthly_goal = db.Column(
        db.Integer,
        default=500
    )

    def __repr__(self):
        return f'<User {self.username}>'
    
    from . import login_manager

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Ride(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    date = db.Column(
        db.Date,
        nullable=False
    )

    distance = db.Column(
        db.Float,
        nullable=False
    )

    duration = db.Column(
        db.Float,
        nullable=False
    )

   