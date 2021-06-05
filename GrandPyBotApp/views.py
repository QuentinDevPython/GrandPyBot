from flask import Flask, render_template
from flask.wrappers import Response

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_response

@app.route('/')
def index():
    response_bot = find_response().response_bot
    return render_template('home.html', response=response_bot)

