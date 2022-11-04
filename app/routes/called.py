from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from app.models.models import Status, Client


called = Blueprint('called', __name__)

@called.route('/called')
@login_required
def open_called():

   status = Status.query.all()

   clients = Client.query.all()
   company_name = []
   for names in clients:
      company_name.append(names.company_name)

   return render_template('called/called_create.html', status=status, clients=company_name)


@called.route('/called', methods=['POST'])
@login_required
def called_post():
   return render_template('called/called_table.html')


@called.route('/call_list')
@login_required
def called_list():

   Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
   return render_template('called/called_table.html', Pokemons = Pokemons)