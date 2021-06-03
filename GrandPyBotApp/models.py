from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app

db = SQLAlchemy(app)

class Response_Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response_bot = db.Column(db.String(1000), nullable=False)

    def __init__(self, response_bot):
        self.response_bot = response_bot

db.create_all()

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Response_Bot("Réponse 1"))
    db.session.add(Response_Bot("Réponse 2"))
    db.session.commit()
    lg.warning('Database initialised')
