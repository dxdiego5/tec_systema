from flask_login import UserMixin
from .. import db

class Users(UserMixin, db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# class Called(db.Model):
#     # __tablename__ = 'calleds'
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     ticket_number = db.Column(db.Integer)
#     name_customer = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
#     name = db.Column(db.String(1000))