from .scripts.utils import float_converter
from .services.server import Server

from flask import (
    redirect, render_template, request
)

from flask.views import MethodView


class Register(MethodView):
    def __init__(self, server: Server) -> None:
        self.server = server

    def get(self):
        return render_template('register/create.html')

    def post(self):
        description = request.form['description']
        category = request.form.get('category')
        value = request.form['value']
        operation = request.form.get('operation')
        date = request.form['date']

        value = float_converter(value)
        self.server.rs.create_record(
            description, value, category, operation, date)
        return redirect('/')


def register_api(app, server, url):
    item = Register.as_view(url, server)
    app.add_url_rule(f'/{url}/', view_func=item)
