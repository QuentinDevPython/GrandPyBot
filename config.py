"""Import the module os to access files with their path
in the project."""
import os

if os.environ.get('DATABASE_URL') is None:
    # Configuration for the development environment
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    GOOGLE_MAP_KEY = "AIzaSyCAnKF11Od9FXT-GpagAW--hrzqCFTlTRw"

else:
    # Configuration for the production environment
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1)
    GOOGLE_MAP_KEY = "AIzaSyBrlKRlYIgrReCvNlYdQFX1JODyXcMxLR8"
