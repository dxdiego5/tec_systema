from flask_login import UserMixin

"""" Usar para aplicação rodando """
from .. import db  

""" Usar para criar o banco de dados """
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

"""" Inicialização das Models (Tabelas do BD)  """
class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    color = db.Column(db.String(10))
    isActive = db.Column(db.Boolean, default=True)
    
class PermissionProfile(db.Model):
    __tablename__ = 'permissions_profile'
    id = db.Column(db.Integer, primary_key=True)
    name_profile = db.Column(db.String(20))
    # Method de registro como lista atribuir 1 rash tags # para dar o split depois e retornar uma lista
    #['all','insert', 'update', 'delete', 'select']
    permission = db.Column(db.String(200))
    isActive = db.Column(db.Boolean, default=True)

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    user_name = db.Column(db.String(40))
    password = db.Column(db.String())
    isActive = db.Column(db.Boolean, default=True)
    permissions_profile_id = db.Column(db.Integer, db.ForeignKey('permissions_profile.id', onupdate='CASCADE'))

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80))
    type_client = db.Column(db.String(4), default=None)
    isActive = db.Column(db.Boolean, default=True)

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE'))
    clients_id = db.Column(db.Integer, db.ForeignKey('clients.id', onupdate='CASCADE'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id', onupdate='CASCADE'))
    description = db.Column(db.String)
    ticket_number = db.Column(db.String, default=0)
    repeat_day = db.Column(db.Integer, default=0)
    create_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    