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
    db.session.add(Response_Bot("Hi ! I'm GrandPyBot ! My purpose is to answer your questions by" 
        "giving you wikipedia information about the place you search for, and by pointing this" 
        "place on a Google Map. So, what do you want to know ?"))
    db.session.add(Response_Bot("Hello ! Welcome to my website ! My name is GrandPyBot and I'm here" 
    "to help you in fiding a place on Google Map and give you some information about it ! "))
    db.session.commit()
    lg.warning('Database initialised')
