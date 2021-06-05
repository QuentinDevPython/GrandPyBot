import random

from .models import Response_Bot

def find_response():
    response = Response_Bot.query.all()
    return random.choice(response)