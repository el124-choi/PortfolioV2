from flask import Blueprint, abort, render_template

from portfolio.db import get_db

bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/<int:index>', methods=['GET'])
def project(index):
    entry = get_db().execute(
        'SELECT title, created, img_path, technologies, github, award, content FROM projects WHERE id = ?',
        (index,)
    ).fetchone()

    if entry is None:
        abort(404)

    contents = entry['content'].split(". ")
    return render_template('projects/project_page.html', entry=entry, contents=contents)
