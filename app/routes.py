from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from . import db
from .models import User

from .forms import RegistrationForm
from werkzeug.security import generate_password_hash

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