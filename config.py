import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

GOOGLE_MAP_KEY = "AIzaSyAqgvq_H95ho3m5U4M_mjeErXXJ5cPxhwg"