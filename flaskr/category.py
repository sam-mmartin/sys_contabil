from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.models.category import Category
from flaskr.services.server import ServerSqlite

bp = Blueprint('category', __name__)
server = ServerSqlite()


@bp.route('/category')
def index():
    service = server.get_category_service()
    categorys: Category = service.list_all_category()
    return render_template('category/index.html', categorys=categorys)


@bp.route('/category/create', methods=('GET', 'POST'))
def create_category():
    if request.method == 'POST':
        description = request.form['description']
        error = None

        if not description:
            error = 'Description is required.'

        if error is not None:
            flash(error)
        else:
            service = server.get_category_service()
            service.create_category(description)
            return redirect(url_for('category.index'))

    return render_template('category/create.html')
