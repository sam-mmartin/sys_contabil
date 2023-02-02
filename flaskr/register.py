from .scripts.utils import float_converter
from .services.server import ServerSqlite

from flask import (
    redirect, render_template, request, g
)

from flask.views import MethodView


class Register(MethodView):
    def __init__(self, server: ServerSqlite) -> None:
        self.service = server.get_register_service()

    def get(self):
        return render_template('register/create.html')

    def post(self):
        description = request.form['description']
        category = request.form.get('category')
        value = request.form['value']
        operation = request.form.get('operation')
        date = request.form['date']

        value = float_converter(value)
        self.service.create_register(
            description, value, category, operation, date, g.user['id']
        )
        return redirect('/')


def register_api(app, server, url):
    item = Register.as_view(url, server)
    app.add_url_rule(f'/{url}/', view_func=item)
