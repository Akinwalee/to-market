from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

#Create function to create app and return the app object

def create_app():
    app = Flask(__name__)
#config database
#register blueprints
#create database