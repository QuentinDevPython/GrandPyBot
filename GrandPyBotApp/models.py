from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app

db = SQLAlchemy(app)

class First_sentences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_sentence = db.Column(db.String(1000), nullable=False)

    def __init__(self, first_sentence):
        self.first_sentence = first_sentence

class Response_Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response_address = db.Column(db.String(1000), nullable=False)

    def __init__(self, response_address):
        self.response_address = response_address

class Response_Wikipedia_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response_wikipedia = db.Column(db.String(1000), nullable=False)

    def __init__(self, response_wikipedia):
        self.response_wikipedia = response_wikipedia

class Ask_Another_Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    another_question  = db.Column(db.String(1000), nullable=False)

    def __init__(self, another_question):
        self.another_question = another_question

class Search_Error(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_error = db.Column(db.String(1000), nullable=False)

    def __init__(self, search_error):
        self.search_error = search_error

db.create_all()

def init_db():
    db.drop_all()
    db.create_all()

    add_first_sentences(First_sentences)
    add_response_address(Response_Address)
    add_response_wikipedia(Response_Wikipedia_Info)
    add_another_question(Ask_Another_Question)
    add_search_error(Search_Error)

    db.session.commit()
    lg.warning('Database initialised')

def add_first_sentences(First_sentences):
    db.session.add(
        First_sentences(
        "Salut ! Je suis GrandPy Bot ! J'ai beau être un robot, "
        "j'adore raconter des histoires à mes super visiteurs ! "
        "Demande-moi une anecdote sur n'importe quel lieu "
        "et tu verras que je suis incollable !"
        )
    )
    db.session.add(
        First_sentences(
        "Bonjour, je me présente je m'appelle GrandPy Bot ! "
        "Je suis là pour vous donner des indications sur les "
        "lieux de votre choix. Mais .. gare à vous ! Il se pourrait "
        "que je sois quelque peu bavard !"
        )
    )
    db.session.add(
        First_sentences(
        "Bonjour cher visiteurs ! Je suis GrandPy Bot, votre nouveau "
        "meilleur ami. Non non, pas Google Maps ni Wikipedia, MOI, "
        "la fusion des deux .. une version améliorée .. "
        "sans prétention bien évidemment !!"
        )
    )

def add_response_address(Response_Address):
    db.session.add(
        Response_Address(
        "J'ai l'adresse qu'il te faut mon poussin ! Je t'ajoute même une "
        "petite carte en dessous pour ne pas que tu te perdes ! La voici : "
        )
    )
    db.session.add(
        Response_Address(
        "Très bon choix mon petit coco ! J'y suis déjà allé de mon temps ! "
        "Je me souviens même de l'adresse, comme si c'était hier : "
        )
    )
    db.session.add(
        Response_Address(
        "D'accord ! Calcul des coordonnées GPS en cours .. récupération de l'adresse "
        ".. positionnement d'un marqueur sur la carte .. c'est comme ça que vous parlez "
        "vous les jeun's aujourd'hui n'est-ce pas ? Aller la voilà ton adresse : "
        )
    )

def add_response_wikipedia(Response_Wikipedia_Info):
    db.session.add(
        Response_Wikipedia_Info(
        "D'ailleurs, en parlant de ce lieu, t'ai-je déjà raconté la fois où je m'y suis "
        "perdu ? Avant de m'y atarder je vais te faire un petit topot de ce que tu as "
        "à en savoir pour mieux comprendre la suite de mon histoire ! <br />"
        )
    )
    db.session.add(
        Response_Wikipedia_Info(
        "Ah ! Quel merveilleux endroit ! C'est là bas que j'ai batti de nombreux souvenirs "
        "d'enfance ! Voyons ce que je peux te dire là dessus ... <br />"
        )
    )
    db.session.add(
        Response_Wikipedia_Info(
        "Oh mais je m'en souviens maintenant ! J'ai vécu là bas durant mon adolescence ! "
        "Si tu savais le nombre de bêtises que j'y ai fait ... Mais parlons plutôt de son "
        "histoire ! <br />"
        )
    )

def add_another_question(Ask_Another_Question):
    db.session.add(
        Ask_Another_Question(
        "Je sais .. je parle beaucoup .. mais tu sais je suis un vieux papy et "
        "je regorge d'histoires à raconter ! As-tu une autre question à me poser ?"
        )
    )
    db.session.add(
        Ask_Another_Question(
        "J'espère que mes indications t'auront aidé malgré mon grand bavardage ! "
        "N'hésites pas à me poser d'autres questions, je m'ennuie un peu maintenant "
        "que je suis à la retraite !"
        )
    )
    db.session.add(
        Ask_Another_Question(
        "Ah mon enfant ! J'ai adoré pouvoir te venir en aide ! Surtout si tu as d'autres "
        "questions n'hésite pas, je serais ravi de pouvoir continuer à te parler !"
        )
    )

def add_search_error(Search_Error):
    db.session.add(
        Search_Error(
            "Désolé mon petit poussin ! Je ne connais pas le lieu dont tu me parles, est-ce "
            "que tu es sûr de son orthographe ? Ou alors peut-être que je ne comprends pas "
            "bien ta question, est-ce que tu pourrais la reformuler ?"
        )
    )
    db.session.add(
        Search_Error(
            "Désolé mon kiki mais je ne vois pas du tout de quoi tu me parles .. ma mémoire "
            "doit encore me jouer des tours ! Aaah la vieillesse ! Est-ce que tu pourrais répéter "
            "ta question en la reformulant ?"
        )
    )