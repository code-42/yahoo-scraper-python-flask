import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from scraper.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from scraper import routes
