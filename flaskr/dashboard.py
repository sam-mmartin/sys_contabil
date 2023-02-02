from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.services.server import ServerSqlite
from flaskr.dto.register_dto import RegisterDTO

bp = Blueprint('dashboard', __name__)
server = ServerSqlite()


@bp.route('/')
def index():
    from .services.server import Server
    csv = Server("flaskr/data/web_registro_contabil.csv")

    service = server.get_register_service()

    credit_amount = service.get_sum_amount(2, False)
    debit_amount = service.get_sum_amount(1, False)
    balance_amount = round(credit_amount - debit_amount, 2)
    balance_percentual = round((balance_amount * 100) / credit_amount, 2)

    data = {
        'ins': service.count_registers_by_operation(2),
        'outs': service.count_registers_by_operation(1),
        'bal_percent': balance_percentual,
        'credit_amount': credit_amount,
        'debit_amount': debit_amount,
        'month_debits': service.month_debits_sum_amount(),
        'invoice_amount': service.invoice_debits(),
        'balance_amount': balance_amount,
        'list_debits': service.list_all_registers_by_operation(1),
        'list_credits': service.list_all_registers_by_operation(2),
    }

    return render_template('index.html', finance_data=data)


@bp.route('/sum-credit-month', methods=('GET', 'POST'))
def sum_credit_month():
    if request.method == 'POST':
        service = server.get_register_service()

        return redirect(url_for('dashboard.index'))
