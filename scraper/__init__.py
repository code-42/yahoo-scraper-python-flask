import os
from flask import Flask
from scraper.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
# pass in the function name for our /login route
login_manager.login_view = 'login'
# nicely colored blue login alert
login_manager.login_message_category = 'info'

from scraper import routes
