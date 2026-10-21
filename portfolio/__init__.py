import os 

from flask import Flask
from flask import render_template
from portfolio.db import get_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path, 'portfolio.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/blog')
    def blog():
        db = get_db()
        entries = db.execute(
            'SELECT posted, content'
            ' FROM entries'
            ' WHERE archived = FALSE'
        ).fetchall()
        return render_template('blog.html', entries=entries)

    @app.route('/projects')
    def projects():
        db = get_db()
        complete = db.execute(
            'SELECT id, title'
            ' FROM projects'
            ' WHERE completed = TRUE'
        ).fetchall()
        incomplete = db.execute(
            'SELECT id, title'
            ' FROM projects'
            ' WHERE completed = FALSE'
        ).fetchall() 
        return render_template('projects/index.html', c_projects=complete, i_projects=incomplete)

    from . import db
    db.init_app(app)

    from . import projects
    app.register_blueprint(projects.bp)

    return app
