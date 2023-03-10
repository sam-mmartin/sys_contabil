from flask import Flask, render_template

import os

from .resources import auth, category, dashboard, operation, pricing, register, group_by


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

   from . import (
       sqlite
   )

   sqlite.init_app(app)

   app.register_blueprint(auth.bp)

   from .services.server import ServerSqlite
   server = ServerSqlite()

   app.register_blueprint(dashboard.bp)
   app.add_url_rule('/', endpoint='index')

   app.register_blueprint(category.bp)
   app.add_url_rule('/', endpoint='index')

   app.register_blueprint(operation.bp)
   app.add_url_rule('/', endpoint='index')

   app.register_blueprint(group_by.bp)
   app.add_url_rule('/', endpoint='index')

   app.register_blueprint(pricing.bp)
   app.add_url_rule('/', endpoint='index')

   register.register_api(app, server, "registers")
   register.register_api(app, server, "register")

   return app
