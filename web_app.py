from flask import Flask, render_template, request, redirect, url_for
from accounting_system import server
from models.record import Record

import scripts.utils as utils

app = Flask(__name__)


@app.route('/')
def home():
    credit_amount = server.credit_amount()
    debit_amount = server.debit_amount()
    balance_amount = round(credit_amount - debit_amount, 2)

    data = {
        'credit_amount': credit_amount,
        'debit_amount': debit_amount,
        'month_debits': server.month_debits(),
        'invoice_amount': server.invoice_amount(),
        'balance_amount': balance_amount,
        'list_debits': server.list_all_debits()
    }
    return render_template(
        'index.html', finance_data=data
    )


@app.route('/add')
def add():
    return render_template('registro/create.html')


@app.route('/add-registro', methods=['POST',])
def add_registro():
    description = request.form['description']
    category = request.form.get('category')
    value = request.form['value']
    operation = request.form.get('operation')
    date = request.form['date']

    value = utils.float_converter(value)
    server.create_record(description, value, category, operation, date)
    return redirect('/')


app.run()
