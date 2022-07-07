"""Import the module os to access files with their path
in the project."""
import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

GOOGLE_MAP_KEY = "AIzaSyCAnKF11Od9FXT-GpagAW--hrzqCFTlTRw"
