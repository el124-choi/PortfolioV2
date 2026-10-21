from flask import Blueprint, abort, render_template

from portfolio.db import get_db

bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/<int:index>', methods=['GET'])
def project(index):
    entry = get_db().execute(
        'SELECT * FROM projects WHERE id = ?',
        (index,)
    ).fetchone()

    if entry is None:
        abort(404)

    return render_template('projects/project_page.html', entry=entry)
