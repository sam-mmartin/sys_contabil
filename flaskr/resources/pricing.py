from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.resources.auth import login_required
from flaskr.services.server import ServerSqlite

bp = Blueprint('pricing', __name__)
server = ServerSqlite()


@bp.route('/pricing/<int:month>')
@login_required
def index(month):

   return render_template('register/pricing.html')
