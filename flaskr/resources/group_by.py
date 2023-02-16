from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.resources.auth import login_required
from flaskr.services import group_by_service as service

bp = Blueprint('groupby', __name__)


@bp.route('/groupby')
@login_required
def index():
   groups = service.list_all_groups()
   return render_template('group_by/index.html', groups=groups)


@bp.route('/groupby/create', methods=('GET', 'POST'))
@login_required
def create():
   if request.method == 'POST':
      description = request.form['description']
      name = request.form['name']
      error = None

      if not description:
         error = 'Description is required.'

      if not name:
         error = 'Name is required.'

      if error is not None:
         flash(error)
      else:
         service.create_group_by(description, name)
         return redirect(url_for('groupby.index'))

   return render_template('group_by/create.html')
