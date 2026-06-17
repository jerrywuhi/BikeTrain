from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

from . import db

from .models import User
from .models import Ride

from .forms import RegistrationForm
from .forms import LoginForm
from .forms import RideForm
from .forms import ProfileForm

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(
                form.password.data
            )
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.index'))


    return render_template(
        'register.html',
        form=form
    )

@main.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            return redirect(
                url_for('main.dashboard')
            )

    return render_template(
        'login.html',
        form=form
    )

@main.route('/dashboard')
@login_required
def dashboard():
    rides = Ride.query.filter_by(
    user_id=current_user.id
    ).all()

    total_distance = sum(
        ride.distance for ride in rides
    )

    total_duration = sum(
        ride.duration for ride in rides
    )

    total_rides = len(rides)

    ride_dates = [
        ride.date.strftime("%m-%d")
        for ride in rides
    ]

    ride_distances = [
        ride.distance
        for ride in rides
    ]
    return render_template(
        'dashboard.html',
        user=current_user,
        total_distance=total_distance,
        total_duration=total_duration,
        total_rides=total_rides,
        ride_dates=ride_dates,
        ride_distances=ride_distances
    )
        
@main.route('/ride/add', methods=['GET', 'POST'])
@login_required
def add_ride():

    form = RideForm()

    if form.validate_on_submit():

        ride = Ride(
            user_id=current_user.id,
            date=form.date.data,
            distance=form.distance.data,
            duration=form.duration.data
        )

        db.session.add(ride)
        db.session.commit()

        return redirect(url_for('main.dashboard'))

    return render_template(
        'add_ride.html',
        form=form
    )

@main.route('/rides')
@login_required
def rides():

    rides = Ride.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Ride.date.desc()
    ).all()

    return render_template(
        'rides.html',
        rides=rides
    )
@main.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for('main.login'))

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    form = ProfileForm()

    if form.validate_on_submit():

        current_user.ftp = form.ftp.data
        current_user.weight = form.weight.data

        db.session.commit()

        return redirect(
            url_for('main.dashboard')
        )

    if not form.is_submitted():
        form.ftp.data = current_user.ftp
        form.weight.data = current_user.weight

    return render_template(
        'profile.html',
        form=form
    )