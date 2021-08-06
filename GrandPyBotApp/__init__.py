from flask import Flask

from .views import app
from . import models

models.db.init_app(app)

models.init_db()
@app.cli.command("init_db")
def init_db():
    models.init_db()