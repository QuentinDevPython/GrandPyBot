import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_response
from .api_wikipedia import ApiWikipedia
from .parser import Parser

#wikipedia = ApiWikipedia('tour eiffel') #A la place de tour eiffel mettre le mot parser

from .api_google_maps import ApiGoogleMaps

 #A la place de tour eiffel mettre le mot parser

@app.route('/')
def index():
    response_bot = find_response().response_bot
    return render_template('home.html', response=response_bot)

@app.route('/question/')
def response():
    data = request.args.get('question')

    parser = Parser()
    parsed_sentence = parser.parser(data)

    print(parsed_sentence)

    wikipedia = ApiWikipedia(parsed_sentence)
    response_wikipedia = wikipedia.get_information_place()

    gmaps = ApiGoogleMaps(parsed_sentence)
    response_map = gmaps.get_coords_place()   

    return jsonify((response_wikipedia, response_map))