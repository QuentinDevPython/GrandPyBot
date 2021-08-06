"""Import the files which contain the project app and the project database."""
from .views import app
from . import models

models.db.init_app(app)

models.init_db()


@app.cli.command("init_db")
def init_db():
    """
    Method that initializes the project database.
    """
    models.init_db()
