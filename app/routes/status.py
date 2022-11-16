from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.models.models import Status, Tickets
from .. import db

status = Blueprint('status', __name__)


@status.route('/status', methods=['GET','POST'])
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
               return redirect(url_for('status.status_list'))


            status = Status(name=status_name.strip(), color=status_color)
            db.session.add(status)
            db.session.commit()
            flash(f'Status criado com sucesso.')

         elif type_register == 'update':
            status_name = request.form.get('status_name_update')
            
            status_color = request.form.get('status_color_update') 
            status_id = request.form.get('status_id_update')

            # updatetd status
            status = Status.query.get(status_id)
            status.name = status_name.strip()
            status.color = status_color
            db.session.commit()
            flash(f'Status atualizado com sucesso.')

         elif type_register == 'delete':
            
            status_id = request.form.get('status_id_delete')

            # if exist ticke open actie status not delete
            if Tickets.query.filter_by(status_id=status_id).first():
               flash(f'Há chamados que utilizam o nome deste status, não podemos remover.')
               return redirect(url_for('status.status_list'))

            else:

               Status.query.filter_by(id=status_id).delete()
               db.session.commit()
               flash(f'Status removido com sucesso.')
               return redirect(url_for('status.status_list'))


   return redirect(url_for('status.status_list'))