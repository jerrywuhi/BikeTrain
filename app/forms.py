from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import DateField, FloatField
from wtforms.validators import DataRequired
from wtforms import FloatField
from wtforms.validators import DataRequired

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

class LoginForm(FlaskForm):

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

    submit = SubmitField('登入')

class RideForm(FlaskForm):

    date = DateField(
        '日期',
        validators=[DataRequired()]
    )

    distance = FloatField(
        '距離(km)',
        validators=[DataRequired()]
    )

    duration = FloatField(
        '時間(hr)',
        validators=[DataRequired()]
    )

    submit = SubmitField('新增紀錄')

class ProfileForm(FlaskForm):

    ftp = FloatField(
        'FTP',
        validators=[DataRequired()]
    )

    weight = FloatField(
        '體重',
        validators=[DataRequired()]
    )

    submit = SubmitField('儲存')