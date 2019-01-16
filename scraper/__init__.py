import os
from flask import Flask
from scraper.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
# pass in the function name for our /login route
login_manager.login_view = 'login'
# nicely colored blue login alert
login_manager.login_message_category = 'info'

# client = pymongo.MongoClient('mongodb://yahoo:yah00!@ds157223.mlab.com:57223/',
#         username='yahoo',
#         password='yah00!',
#         authSource='yahoo-scraper',
#         authMechanism='SCRAM-SHA-1')

client = pymongo.MongoClient('mongodb://yahoo:yah00!@ds157223.mlab.com:57223/yahoo-scraper')
# client = pymongo.MongoClient('MONGOALCHEMY_CONNECTION_STRING')

mdb = client['yahoo-scraper']
print("mdb.name == " + mdb.name)
# data = mdb.name
collection = mdb.totals
print("collection == " + collection.name)
# print("data: ")
# for x in collection.find():
#     print(x)




from scraper import routes
