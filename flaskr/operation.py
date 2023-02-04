from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.models.category import Category
from flaskr.models.operation import Operation
from flaskr.services.server import ServerSqlite

bp = Blueprint('operation', __name__)
server = ServerSqlite()


@bp.route('/operation')
@login_required
def index():
    service = server.get_operation_service()
    operations: Operation = service.list_all_operations()
    return render_template('operation/index.html', operations=operations)


@bp.route('/operation/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        description = request.form['description']
        error = None

        if not description:
            error = 'Description is required.'

        if error is not None:
            flash(error)
        else:
            service = server.get_operation_service()
            service.create_operation(description)
            return redirect(url_for('operation.index'))

    return render_template('operation/create.html')
