from flask import Flask, render_template
from accounting_system import server

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template(
        'index.html',
        credit_amount=server.credit_amount(),
        debit_amount=server.debit_amount(),
        month_debits=server.month_debits(),
        invoice_amount=server.invoice_amount()
    )


app.run()
