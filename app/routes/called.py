from flask import Blueprint, render_template, request
from .. import db
from flask_login import login_required, current_user

called = Blueprint('called', __name__)

@called.route('/service')
@login_required
def called_table():
   return render_template('service/called_table.html')


@called.route('/service', methods=['POST'])
@login_required
def called_save():
   # ticket_number = request.form.get('ticket_number')
   # name_customer = request.form.get('name_customer')
   # status_ticket = request.form.get('status_ticket')
   # description = request.form.get('description')

   # print(ticket_number)
   # print(name_customer)
   # print(status_ticket)
   # print(description)

   return render_template('service/called_table.html')