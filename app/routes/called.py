from flask import Blueprint, render_template, request
from .. import db
from flask_login import login_required, current_user

called = Blueprint('called', __name__)

@called.route('/called')
@login_required
def open_called():
   return render_template('called/called_create.html')


@called.route('/called', methods=['POST'])
@login_required
def called_post():
   return render_template('called/called_table.html')


@called.route('/call_list')
@login_required
def called_list():

   Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
         #   ,len = len(Pokemons), Pokemons = Pokemons
   return render_template('called/called_table.html', Pokemons = Pokemons)