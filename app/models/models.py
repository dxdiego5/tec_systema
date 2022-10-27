from flask_login import UserMixin
from sqlalchemy import Table

"""" Usar para aplicação rodando """
from .. import db  

""" Usar para criar o banco de dados """
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

"""" Inicialização das Models (Tabelas do BD)  """
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
