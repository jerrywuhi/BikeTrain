from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)


class RegistrationForm(FlaskForm):

    username = StringField(
        '使用者名稱',
        validators=[
            DataRequired(),
            Length(min=3, max=20)
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        '密碼',
        validators=[
            DataRequired()
        ]
    )

    confirm_password = PasswordField(
        '確認密碼',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('註冊')