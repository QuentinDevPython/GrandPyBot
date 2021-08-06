"""Import the module os to access files with their path
in the project."""
import os

if os.environ.get('DATABASE_URL') is None:
    # Configuration pour l'environnement de développement
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    GOOGLE_MAP_KEY = "AIzaSyAqgvq_H95ho3m5U4M_mjeErXXJ5cPxhwg"
else:
    # Configuration pour l'environnement de production
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1)

    GOOGLE_MAP_KEY = "AIzaSyDh4aiF7QYczFRpKtMQCdSJdncufoq8W_I"
