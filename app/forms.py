from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import DateField, FloatField
from wtforms.validators import DataRequired
from wtforms import FloatField
from wtforms.validators import DataRequired
from wtforms import SelectField

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)
import os

from werkzeug.utils import secure_filename

from flask import current_app

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
    ride_type = SelectField(
        '騎乘類型',
        choices=[
            ('Z2耐力', 'Z2耐力'),
            ('FTP訓練', 'FTP訓練'),
            ('VO2Max', 'VO2Max'),
            ('爬坡訓練', '爬坡訓練'),
            ('長距離', '長距離'),
            ('恢復騎', '恢復騎')
        ]
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

    monthly_goal = FloatField(
        '月目標(km)',
        validators=[DataRequired()]
    )

    submit = SubmitField('儲存')
    profile_image = FileField(
    '頭像',
    validators=[
        FileAllowed(
            ['jpg', 'jpeg', 'png'],
            '只能上傳圖片'
        )
    ]
)