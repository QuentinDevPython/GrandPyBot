"""Import the module flask to use its functionalites to connect the templates with the ajax.
Import also the classes Parser (to parse a sentence), Api_google_Maps (to access Google Maps)
and Api_Wikipedia (to access the Wikipedia information).
Import alse the sentences randomly chosen in the project database to make the bot talk."""
from flask import Flask, \
    render_template, \
    request, \
    jsonify
from .api_google_maps import ApiGoogleMaps
from .parser import Parser
from .api_wikipedia import ApiWikipedia

app = Flask(__name__)
app.config.from_object('config')

from .utils import find_first_sentence, \
    find_response_address, \
    find_response_wikipedia, \
    find_another_question, \
    find_search_error
    
GOOGLE_MAP_KEY = "AIzaSyAqgvq_H95ho3m5U4M_mjeErXXJ5cPxhwg"

@app.route('/')
def index():
    """
    Function that allows to display the HTML page to the user, with a bot introduction sentence.
    """
    first_sentence = find_first_sentence().first_sentence
    return render_template('home.html', first_sentence=first_sentence)


@app.route('/question/')
def response():
    """
    Function that allows to respond to the user with the different informations concerning
    the place he wants to talk about. These information are processed in the home.js file.
    """
    data = request.args.get('question')

    parser = Parser()
    parsed_sentence = parser.parser(data)

    wikipedia = ApiWikipedia()
    response_wikipedia = wikipedia.get_information_place(parsed_sentence)

    gmaps = ApiGoogleMaps(GOOGLE_MAP_KEY)
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
    """
    Function that allows to display a bot sentence when there is an error
    concerning the place the user is searching for.
    """
    return jsonify((
        find_search_error().search_error
    ))
