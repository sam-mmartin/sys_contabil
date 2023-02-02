from flask import Flask, render_template

import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import sqlite
    sqlite.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    # from .services.server import Server
    # server = Server("flaskr/data/web_registro_contabil.csv")

    from .services.server import ServerSqlite
    server = ServerSqlite()

    from . import dashboard
    app.register_blueprint(dashboard.bp)
    app.add_url_rule('/', endpoint='index')

    from . import category
    app.register_blueprint(category.bp)
    app.add_url_rule('/', endpoint='index')

    from . import operation
    app.register_blueprint(operation.bp)
    app.add_url_rule('/', endpoint='index')

    from . import register
    register.register_api(app, server, "registers")

    # @app.route('/')
    # def home():
    #     credit_amount = server.finance.get_credit_amount()
    #     debit_amount = server.finance.get_debit_amount()
    #     balance_amount = round(credit_amount - debit_amount, 2)

    #     data = {
    #         'credit_amount': credit_amount,
    #         'debit_amount': debit_amount,
    #         'month_debits': server.finance.list_all_month_debits_value(),
    #         'invoice_amount': server.finance.invoice_debits(),
    #         'balance_amount': balance_amount,
    #         'list_debits': server.finance.list_all_month_debits(),
    #         'list_credits': server.finance.list_all_month_credits()
    #     }
    #     return render_template(
    #         'index.html', finance_data=data
    #     )

    return app
