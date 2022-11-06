from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app.function.DateTimeUtlis import date_time_now

from app.models.models import Status, Client, Users, Ticket
from .. import db

ticket = Blueprint('ticket', __name__)

@ticket.route('/ticket')
@login_required
def open_ticket():

   status = Status.query.all()

   clients = Client.query.all()
   company_name = []
   for names in clients:
      company_name.append(names.company_name)

   return render_template('ticket/ticket_create.html', status=status, clients=company_name)
   

@ticket.route('/ticket', methods=['POST'])
@login_required
def ticket_post():

   ticket_number = request.form.get('ticket_number')
   company_name = request.form.get('company_name')
   status_ticket = request.form.get('status_ticket')
   repeat_ticket_day = request.form.get('repeat_ticket_day')
   description = request.form.get('description')

   user = Users.query.get(int(current_user.id))
   status = Status.query.filter_by(id=status_ticket).first()


   client = Client.query.filter_by(company_name=company_name).first()   
   # if check exists client if not register a new client
   if client is None:
      client = Client(company_name=company_name)
      db.session.add(client)
      db.session.commit()
      
   date_time = date_time_now()

   ticket = Ticket(user_id=user.id, clients_id=client.id, status_id=status.id,description=description,ticket_number=ticket_number,
      repeat_day=repeat_ticket_day,create_at=date_time, updated_at=date_time)
   
   db.session.add(ticket)
   db.session.commit()
   
   return render_template('ticket/ticket_table.html')


@ticket.route('/tickets')
@login_required
def ticket_list():

   Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
   return render_template('ticket/ticket_table.html', Pokemons = Pokemons)