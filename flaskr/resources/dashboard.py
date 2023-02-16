import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.resources.auth import login_required
from flaskr.services.server import ServerSqlite
from flaskr.dto.register_dto import RegisterDTO

bp = Blueprint('dashboard', __name__)
server = ServerSqlite()


@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
   service = server.get_register_service()
   ac_service = server.get_annual_sums_service()
   today = datetime.date.today()

   if request.method == 'POST':
      month = int(request.form['month'])
      today = datetime.date(today.year, month, 1)

   credit_amount = service.get_sum_amount(
       2, today.month, g.user['id'])
   debit_amount = service.get_sum_amount(
       1, today.month, g.user['id'])
   try:
      balance_amount = round(credit_amount - debit_amount, 2)
      balance_percentual = round((balance_amount * 100) / credit_amount, 2)
   except:
      balance_amount = 0
      balance_percentual = 0

   data = {
       'ins': service.count_registers_by_operation(2, today.month, g.user['id']),
       'outs': service.count_registers_by_operation(1, today.month, g.user['id']),
       'bal_percent': balance_percentual,
       'credit_amount': credit_amount,
       'debit_amount': debit_amount,
       'month_debits': service.month_debits_sum_amount(today.month, g.user['id']),
       'invoice_amount': service.invoice_debits(today.month, g.user['id']),
       'balance_amount': balance_amount,
       'list_debits': service.list_all_registers_by_operation(1, today.month, g.user['id']),
       'list_credits': service.list_all_registers_by_operation(2, today.month, g.user['id']),
       'annual_sums': ac_service.get_all_annual_sums_by_months(g.user['id']),
   }

   return render_template('index.html', finance_data=data)


@bp.route('/sum-month/<int:operation_id>', methods=('GET', 'POST'))
@login_required
def sum_credit_month(operation_id):
   if request.method == 'POST':
      month = request.form['month']
      year = request.form['year']
      error = None

      if not month:
         error = 'Reference month is required.'
      elif not year:
         error = 'Reference year is required.'

      if error is not None:
         flash(error)
      else:
         month = int(month)
         year = int(year)
         service = server.get_annual_sums_service()
         service.set_sum_month(
             operation_id, month, year, g.user['id']
         )
         return redirect(url_for('dashboard.index'))
