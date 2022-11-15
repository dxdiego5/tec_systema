from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from app.function.DateTimeUtlis import date_time_now

from app.models.models import Status, Clients, Users, Tickets
from .. import db

ticket = Blueprint('ticket', __name__)

@ticket.route('/ticket', methods=['GET','POST'])
@login_required
def open_ticket():
      if request.method == 'GET':
         status = Status.query.all()

         clients = Clients.query.all()
         company_name = []
         for names in clients:
            company_name.append(names.company_name)

         return render_template('ticket/ticket_create.html', status=status, clients=company_name)

      elif request.method == 'POST':

         ticket_number = request.form.get('ticket_number')
         company_name = request.form.get('company_name')
         status_ticket = request.form.get('status_ticket')
         repeat_ticket_day = request.form.get('repeat_ticket_day')
         description = request.form.get('description')

         user = Users.query.get(int(current_user.id))
         status = Status.query.filter_by(id=status_ticket).first()


         client = Clients.query.filter_by(company_name=company_name.strip()).first()   
         # if check exists client if not register a new client
         if client is None:
            client = Clients(company_name=company_name.strip())
            db.session.add(client)
            db.session.commit()
            
         date_time = date_time_now()

         ticket = Tickets(user_id='---', clients_id=client.id, status_id=status.id,description=description.strip(),ticket_number=ticket_number,
            repeat_day=repeat_ticket_day,created_at=date_time, updated_at=date_time)
         
         db.session.add(ticket)
         db.session.commit()
         
         return redirect(url_for('ticket.ticket_list'))

@ticket.route('/tickets')
@login_required
def ticket_list():
   tickets = Tickets.query.all()
   return render_template('ticket/ticket_table.html', tickets = tickets)

@ticket.route('/status', methods=['GET','POST'])
@login_required
def status_list():
   status = Status.query.all()

   if request.method == 'GET':
      return render_template('status/status_table.html', status = status)

   elif request.method == 'POST':

         # response possibles [create or update]
         type_register = request.form.get('status_type')

         # register a new status
         if type_register == 'create':
            
            status_name = request.form.get('status_name')
            status_color = request.form.get('status_color') 

            if Status.query.filter_by(name=status_name.strip()).first():
               flash(f'O nome de status {status_name.strip()} já existe.')
               redirect(url_for('ticket.status_list'))


            status = Status(name=status_name.strip(), color=status_color)
            db.session.add(status)
            db.session.commit()

         elif type_register == 'update':
            status_name = request.form.get('status_name_update')
            
            status_color = request.form.get('status_color_update') 
            status_id = request.form.get('status_id_update')

            # updatetd status
            status = Status.query.get(status_id)
            status.name = status_name.strip()
            status.color = status_color
            db.session.commit()
         
         elif type_register == 'delete':
            
            status_id = request.form.get('status_id_delete')

            # if exist ticke open actie status not delete
            if Tickets.query.filter_by(status_id=status_id).first():
               flash(f'Há chamados que utilizam o nome deste status, não podemos remover.')
               return redirect(url_for('ticket.status_list'))

            else:

               Status.query.filter_by(id=status_id).delete()
               db.session.commit()
               flash(f'Status removido com sucesso.')
               return redirect(url_for('ticket.status_list'))


   return redirect(url_for('ticket.status_list'))