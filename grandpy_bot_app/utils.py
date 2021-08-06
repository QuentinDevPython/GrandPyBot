"""Import the module random"""
import random

from .models import FirstSentences, \
    ResponseAddress, \
    ResponseWikipediaInfo, \
    AskAnotherQuestion, \
    SearchError


def find_first_sentence():
    """
    Method to choose a random sentence in the FirstSentences database table.
    """
    first_sentence = FirstSentences.query.all()
    return random.choice(first_sentence)


def find_response_address():
    """
    Method to choose a random sentence in the ResponseAddress database table.
    """
    response_address = ResponseAddress.query.all()
    return random.choice(response_address)


def find_response_wikipedia():
    """
    Method to choose a random sentence in the ResponseWikipediaInfo database table.
    """
    response_wikipedia = ResponseWikipediaInfo.query.all()
    return random.choice(response_wikipedia)


def find_another_question():
    """
    Method to choose a random sentence in the AskAnotherQuestion database table.
    """
    another_question = AskAnotherQuestion.query.all()
    return random.choice(another_question)


def find_search_error():
    """
    Method to choose a random sentence in the SearchError database table.
    """
    search_error = SearchError.query.all()
    return random.choice(search_error)
