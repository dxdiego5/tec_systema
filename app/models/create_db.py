from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os.path
from models import db, PermissionProfile, Users, Status, Clients

filepath = os.path.abspath('app/data.db')

conn = sqlite3.connect(filepath)
engine = create_engine('sqlite:///'+filepath)

Session = sessionmaker(bind = engine)
session = Session()

def create_database_table():
    db.metadata.create_all(engine)
    
    add_permissions_profile()
    add_users()
    add_status()
    add_client()

    session.commit()


def add_permissions_profile():
    permis_profile1 = PermissionProfile(name_profile='master',permission='insert#update#delete#select')
    return session.add(permis_profile1)

def add_users():
    user1 = Users(name='Diego Felipe',user_name='diego',password=generate_password_hash('12345', method='sha256'),isActive=True, permissions_profile_id=1)
    return session.add(user1)

def add_status():
    status1 = Status(name='novo chamado', color='#00afe9')
    session.add(status1)

    status2 = Status(name='notificação', color='#2b49c5')
    session.add(status2)

    status3 = Status(name='concluido', color='#008000')
    session.add(status3)

    status4 = Status(name='cancelado', color='#020005')
    session.add(status4)

def add_client():
    client1 = Clients(company_name='Diego Felipe',type_client='PF')
    session.add(client1)

    client2 = Clients(company_name='Esc. Valter Leite',type_client='PJ')
    session.add(client2)

    client3 = Clients(company_name='Esc. Jardim Bela Vista',type_client='PJ')
    session.add(client3)

    client4 = Clients(company_name='Cemeis. São Domingos',type_client='PJ')
    session.add(client4)

create_database_table()

