import sqlite3
from datetime import datetime

import click
from flask import current_app, g
from flaskr.utils.logging import debug

def get_db():
    if 'db' not in g:
        
        
        ("about to connect")
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    debug("about to return g.db")
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    debug("closing db")
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    debug("initializing db")
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Create tables if not already created."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    debug("teardown of app context complete")
    app.cli.add_command(init_db_command)
    debug("init_db_command added")