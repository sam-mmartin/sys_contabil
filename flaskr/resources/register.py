from flaskr.resources.auth import login_required
from flaskr.utils import float_converter
from flaskr.services.server import ServerSqlite

from flask import (
    redirect, render_template, request, g
)

from flask.views import MethodView


class Register(MethodView):
   decorators = [login_required]

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


class RegisterUpdate(MethodView):
   decorators = [login_required]

   def __init__(self, server: ServerSqlite) -> None:
      self.service = server.get_register_service()

   def get(self, id):
      register = self.service.get_register_by_id(id, g.user['id'])
      return render_template('register/details.html', register=register)

   def post(self, id):
      description = request.form['description']
      category = request.form.get('category')
      value = request.form['amount']
      operation = request.form.get('operation')
      date = request.form['date_register']

      values = float_converter(value)
      self.service.update_register(
          id, description, value, category, operation, date, g.user['id']
      )
      return redirect('/')


class RegisterDelete(MethodView):
   decorators = [login_required]

   def __init__(self, server: ServerSqlite) -> None:
      self.service = server.get_register_service()

   def get(self, id):
      register = self.service.get_register_by_id(id, g.user['id'])
      return render_template('register/details.html', register=register)

   def post(self, id):
      self.service.delete(id, g.user['id'])
      return redirect('/')


def register_api(app, server, url):
   item = Register.as_view(f'{url}-register', server)
   update = RegisterUpdate.as_view(f'{url}-update', server)
   delete = RegisterDelete.as_view(f'{url}-delete', server)
   app.add_url_rule(f'/{url}/', view_func=item)
   app.add_url_rule(f'/{url}/<int:id>/update', view_func=update)
   app.add_url_rule(f'/{url}/<int:id>/delete', view_func=delete)
