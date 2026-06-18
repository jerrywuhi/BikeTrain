from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from datetime import date
from datetime import timedelta

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
    today = date.today()

    week_ago = today - timedelta(days=7)

    month_start = today.replace(day=1)

    

    

    rides = Ride.query.filter_by(
    user_id=current_user.id
    ).all()
    week_rides = Ride.query.filter(
        Ride.user_id == current_user.id,
        Ride.date >= week_ago
    ).all()

    week_ride_count = len(week_rides)

    week_distance = sum(
        ride.distance
        for ride in week_rides
    )

    week_duration = sum(
        ride.duration
        for ride in week_rides
    )


    longest_ride = 0

    if rides:
        longest_ride = max(
            ride.distance
            for ride in rides
        )

    weekly_distance = 0
    weekly_rides = 0

    monthly_distance = 0
    monthly_rides = 0

    avg_speeds = []

    for ride in rides:

        if ride.date >= week_ago:

            weekly_distance += ride.distance
            weekly_rides += 1

        if ride.date >= month_start:

            monthly_distance += ride.distance
            monthly_rides += 1

        if ride.duration > 0:

            avg_speeds.append(
                round(
                    ride.distance /
                    ride.duration,
                    1
                )
            )
    monthly_goal = 500

    goal_progress = min(
        round(
            (monthly_distance / monthly_goal) * 100,
            1
        ),
        100
    )
    

    if current_user.weight > 0:
        wkg = round(
            current_user.ftp /
            current_user.weight,
            2
    
    )
        
    else:
        wkg = 0
    if wkg < 2:
        rider_level = "新手騎士"

    elif wkg < 3:
        rider_level = "休閒騎士"

    elif wkg < 4:
        rider_level = "進階騎士"

    elif wkg < 5:
        rider_level = "競賽級騎士"

    else:
        rider_level = "菁英級騎士"

    if wkg < 2:
        rider_level = "新手騎士"

    elif wkg < 3:
        rider_level = "休閒騎士"

    elif wkg < 4:
        rider_level = "進階騎士"

    elif wkg < 5:
        rider_level = "競賽級騎士"

    else:
        rider_level = "菁英級騎士"

    ftp = current_user.ftp

    z1 = int(ftp * 0.55)

    z2_low = int(ftp * 0.56)
    z2_high = int(ftp * 0.75)

    z3_low = int(ftp * 0.76)
    z3_high = int(ftp * 0.90)

    z4_low = int(ftp * 0.91)
    z4_high = int(ftp * 1.05)

    z5_low = int(ftp * 1.06)
    z5_high = int(ftp * 1.20)

    if wkg < 2:
        advice = """
        建議每週騎乘 2~3 次，
        培養基礎有氧能力。
            """

    elif wkg < 3:
        advice = """
        增加長距離 Z2 訓練，
        提升耐力。
        """

    elif wkg < 4:
        advice = """
        每週安排：
        2 次 Z2
        1 次 FTP 訓練
        """

    elif wkg < 5:
        advice = """
        增加 VO2Max 訓練，
        強化高強度輸出。
        """

    else:
        advice = """
        已達菁英等級，
        建議週期化訓練。
        """

    total_distance = sum(
        ride.distance for ride in rides
    )

    total_duration = sum(
        ride.duration for ride in rides
    )
    if total_duration > 0:
        avg_speed = round(
            total_distance / total_duration,
            1
        )
    else:
        avg_speed = 0

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
    monthly_goal=monthly_goal,
    goal_progress=goal_progress,
    week_ride_count=week_ride_count,
    week_distance=week_distance,
    week_duration=week_duration,
    longest_ride=longest_ride,
    avg_speed=avg_speed,
    weekly_distance=weekly_distance,
    weekly_rides=weekly_rides,
    monthly_distance=monthly_distance,
    monthly_rides=monthly_rides,
    user=current_user,
    total_distance=total_distance,
    total_duration=total_duration,
    total_rides=total_rides,
    ride_dates=ride_dates,
    ride_distances=ride_distances,
    wkg=wkg,
    rider_level=rider_level,
    advice=advice,
    avg_speeds=avg_speeds,
    z1=z1,

    z2_low=z2_low,
    z2_high=z2_high,

    z3_low=z3_low,
    z3_high=z3_high,

    z4_low=z4_low,
    z4_high=z4_high,

    z5_low=z5_low,
    z5_high=z5_high,
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