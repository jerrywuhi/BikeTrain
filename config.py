class Config:
    SECRET_KEY = 'bike-train-secret-key'

    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://root:950822@localhost/biketrain'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False