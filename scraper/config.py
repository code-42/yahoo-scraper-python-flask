import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MONGOALCHEMY_DATABASE = os.environ.get('MONGOALCHEMY_DATABASE')
    MONGOALCHEMY_CONNECTION_STRING = os.environ.get('MONGOALCHEMY_CONNECTION_STRING')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # EMAIL_USER = os.environ.get('EMAIL_USER')
    # EMAIL_PASS = os.environ.get('EMAIL_PASS')
