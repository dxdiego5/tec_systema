from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select

from flask_sqlalchemy import SQLAlchemy

import configparser
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
import os.path
filepath = os.path.abspath('app/data.db')

conn = sqlite3.connect(filepath)
engine = create_engine('sqlite:///'+filepath)
db = SQLAlchemy()

class Users(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Users_table = Table('users', Users.metadata)


def create_users_table():
    Users.metadata.create_all(engine)

create_users_table()

