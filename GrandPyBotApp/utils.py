import random

from .models import First_sentences, Response_Address, Response_Wikipedia_Info, Ask_Another_Question, Search_Error

def find_first_sentence():
    first_sentence = First_sentences.query.all()
    return random.choice(first_sentence)

def find_response_address():
    response_address = Response_Address.query.all()
    return random.choice(response_address)

def find_response_wikipedia():
    response_wikipedia = Response_Wikipedia_Info.query.all()
    return random.choice(response_wikipedia)

def find_another_question():
    another_question = Ask_Another_Question.query.all()
    return random.choice(another_question)

def find_search_error():
    search_error = Search_Error.query.all()
    return random.choice(search_error)