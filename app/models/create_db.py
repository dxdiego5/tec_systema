from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os.path
from models import db, PermissionProfile, Users

filepath = os.path.abspath('app/data.db')

conn = sqlite3.connect(filepath)
engine = create_engine('sqlite:///'+filepath)
Session = sessionmaker(bind = engine)
 

Session = sessionmaker(bind = engine)
session = Session()

def create_database_table():
    db.metadata.create_all(engine)
    
    add_permissions_profile()
    add_users()
    
    session.commit()


def add_permissions_profile():
    permis_profile1 = PermissionProfile(name_profile='master',permission='insert#update#delete#select')
    return session.add(permis_profile1)

def add_users():
    user1 = Users(name='Diego Felipe',user_name='diego',password='12345',isActive=True, permissions_profile_id=1)
    return session.add(user1)

create_database_table()

