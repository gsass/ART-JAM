from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flaskext.markdown import Markdown


app = Flask(__name__)
#TODO Config for db goes here.
db = SQLAlchemy(app)

#Set up a LoginManager
lm = LoginManager()
lm.init_app(app)
#TODO: Make a User class which integrates with our user db model.
#See: http://flask-login.readthedocs.org/en/latest/#your-user-class

#Add the markdown templating filter from Flask-Markdown.
Markdown(app)

#TODO: Make a Flask-Oauth oauth manager for the user class to authenticate
#with.
#There's related work in the gsass/sassandsass repo, but it can surely be
#cleaned up.
