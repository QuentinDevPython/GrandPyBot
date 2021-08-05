import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_first_sentence, find_response_address, find_response_wikipedia, find_another_question, find_search_error
from .api_wikipedia import ApiWikipedia
from .parser import Parser

from .api_google_maps import ApiGoogleMaps

@app.route('/')
def index():
    first_sentence = find_first_sentence().first_sentence
    return render_template('home.html', first_sentence=first_sentence)

@app.route('/question/')
def response():
    data = request.args.get('question')

    parser = Parser()
    parsed_sentence = parser.parser(data)

    wikipedia = ApiWikipedia()
    response_wikipedia = wikipedia.get_information_place(parsed_sentence)

    gmaps = ApiGoogleMaps()
    response_map = gmaps.get_coords_place(parsed_sentence)   

    return jsonify((
        response_wikipedia, 
        response_map, 
        find_response_address().response_address, 
        find_response_wikipedia().response_wikipedia,
        find_another_question().another_question,
    ))

@app.route('/error/')
def error_response():
    return jsonify((
        find_search_error().search_error
    ))