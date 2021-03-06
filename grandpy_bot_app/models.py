"""Import the module flask_sqlalchemy to create the project database.
Import the module which is intended to provide a standard error logging
mechanism in Python as per PEP 282.
Import also the project app."""
import logging as lg
from flask_sqlalchemy import SQLAlchemy


from .views import app

db = SQLAlchemy(app)


class FirstSentences(db.Model):
    """
    Class that creates a database table for the first sentence the
    GrandPyBot is going to say.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_sentence = db.Column(db.String(1000), nullable=False)

    def __init__(self, first_sentence):
        self.first_sentence = first_sentence


class ResponseAddress(db.Model):
    """
    Class that creates a database table for the sentence the GrandPyBot is
    going to say to give the address of the searched place.
    """
    id = db.Column(db.Integer, primary_key=True)
    response_address = db.Column(db.String(1000), nullable=False)

    def __init__(self, response_address):
        self.response_address = response_address


class ResponseWikipediaInfo(db.Model):
    """
    Class that creates a database table for the sentence the GrandPyBot is
    going to say to give the wikipedia information of the searched place.
    """
    id = db.Column(db.Integer, primary_key=True)
    response_wikipedia = db.Column(db.String(1000), nullable=False)

    def __init__(self, response_wikipedia):
        self.response_wikipedia = response_wikipedia


class AskAnotherQuestion(db.Model):
    """
    Class that creates a database table for the sentence the GrandPyBot is
    going to say to answer for an other question.
    """
    id = db.Column(db.Integer, primary_key=True)
    another_question = db.Column(db.String(1000), nullable=False)

    def __init__(self, another_question):
        self.another_question = another_question


class SearchError(db.Model):
    """
    Class that creates a database table for the sentence the GrandPyBot is
    going if he doesn't understand the question.
    """
    id = db.Column(db.Integer, primary_key=True)
    search_error = db.Column(db.String(1000), nullable=False)

    def __init__(self, search_error):
        self.search_error = search_error


db.create_all()


def init_db():
    """
    Method to initialize the database of the project.
    """
    db.drop_all()
    db.create_all()

    add_first_sentences(FirstSentences)
    add_response_address(ResponseAddress)
    add_response_wikipedia(ResponseWikipediaInfo)
    add_another_question(AskAnotherQuestion)
    add_search_error(SearchError)

    db.session.commit()
    lg.warning('Database initialised')


def add_first_sentences(FirstSentences):
    """
    Method to add sentences in the FirstSentences database table.
    """
    db.session.add(
        FirstSentences(
            "Salut ! Je suis GrandPy Bot ! J'ai beau ??tre un robot, "
            "j'adore raconter des histoires ?? mes super visiteurs ! "
            "Demande-moi une anecdote sur n'importe quel lieu "
            "et tu verras que je suis incollable !"
        )
    )
    db.session.add(
        FirstSentences(
            "Bonjour, je me pr??sente je m'appelle GrandPy Bot ! "
            "Je suis l?? pour vous donner des indications sur les "
            "lieux de votre choix. Mais .. gare ?? vous ! Il se pourrait "
            "que je sois quelque peu bavard !"
        )
    )
    db.session.add(
        FirstSentences(
            "Bonjour cher visiteurs ! Je suis GrandPy Bot, votre nouveau "
            "meilleur ami. Non non, pas Google Maps ni Wikipedia, MOI, "
            "la fusion des deux .. une version am??lior??e .. "
            "sans pr??tention bien ??videmment !!"
        )
    )


def add_response_address(ResponseAddress):
    """
    Method to add sentences in the ResponseAddress database table.
    """
    db.session.add(
        ResponseAddress(
            "J'ai l'adresse qu'il te faut mon poussin ! Je t'ajoute m??me une "
            "petite carte en dessous pour ne pas que tu te perdes ! La voici : "
        )
    )
    db.session.add(
        ResponseAddress(
            "Tr??s bon choix mon petit coco ! J'y suis d??j?? all?? de mon temps ! "
            "Je me souviens m??me de l'adresse, comme si c'??tait hier : "
        )
    )
    db.session.add(
        ResponseAddress(
            "D'accord ! Calcul des coordonn??es GPS en cours .. r??cup??ration de l'adresse "
            ".. positionnement d'un marqueur sur la carte .. c'est comme ??a que vous parlez "
            "vous les jeun's aujourd'hui n'est-ce pas ? Aller la voil?? ton adresse : "
        )
    )


def add_response_wikipedia(ResponseWikipediaInfo):
    """
    Method to add sentences in the ResponseWikipediaInfo database table.
    """
    db.session.add(
        ResponseWikipediaInfo(
            "D'ailleurs, en parlant de ce lieu, t'ai-je d??j?? racont?? la fois o?? je m'y suis "
            "perdu ? Avant de m'y atarder je vais te faire un petit topot de ce que tu as "
            "?? en savoir pour mieux comprendre la suite de mon histoire ! <br />"
        )
    )
    db.session.add(
        ResponseWikipediaInfo(
            "Ah ! Quel merveilleux endroit ! C'est l?? bas que j'ai batti de nombreux souvenirs "
            "d'enfance ! Voyons ce que je peux te dire l?? dessus ... <br />"
        )
    )
    db.session.add(
        ResponseWikipediaInfo(
            "Oh mais je m'en souviens maintenant ! J'ai v??cu l?? bas durant mon adolescence ! "
            "Si tu savais le nombre de b??tises que j'y ai fait ... Mais parlons plut??t de son "
            "histoire ! <br />"
        )
    )


def add_another_question(AskAnotherQuestion):
    """
    Method to add sentences in the AskAnotherQuestion database table.
    """
    db.session.add(
        AskAnotherQuestion(
            "Je sais .. je parle beaucoup .. mais tu sais je suis un vieux papy et "
            "je regorge d'histoires ?? raconter ! As-tu une autre question ?? me poser ?"
        )
    )
    db.session.add(
        AskAnotherQuestion(
            "J'esp??re que mes indications t'auront aid?? malgr?? mon grand bavardage ! "
            "N'h??sites pas ?? me poser d'autres questions, je m'ennuie un peu maintenant "
            "que je suis ?? la retraite !"
        )
    )
    db.session.add(
        AskAnotherQuestion(
            "Ah mon enfant ! J'ai ador?? pouvoir te venir en aide ! Surtout si tu as d'autres "
            "questions n'h??site pas, je serais ravi de pouvoir continuer ?? te parler !"
        )
    )


def add_search_error(SearchError):
    """
    Method to add sentences in the SearchError database table.
    """
    db.session.add(
        SearchError(
            "D??sol?? mon petit poussin ! Je ne connais pas le lieu dont tu me parles, est-ce "
            "que tu es s??r de son orthographe ? Ou alors peut-??tre que je ne comprends pas "
            "bien ta question, est-ce que tu pourrais la reformuler ?"
        )
    )
    db.session.add(
        SearchError(
            "D??sol?? mon kiki mais je ne vois pas du tout de quoi tu me parles .. ma m??moire "
            "doit encore me jouer des tours ! Aaah la vieillesse ! Est-ce que tu pourrais r??p??ter "
            "ta question en la reformulant ?"
        )
    )
