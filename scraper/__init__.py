from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xf1\\3\x91p\x97i>\x9a\xeal\x1e\xe2\xcc\xd3y"\x96\xfca\xb7\xf6`\xa7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from scraper import routes
