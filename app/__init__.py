from flask import Flask, url_for
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.principal import Principal

import os

tronms = Flask(__name__)
tronms.config.from_object('config')

db = SQLAlchemy(tronms)

lm = LoginManager()
lm.init_app(tronms)

bcrypt = Bcrypt(tronms)

principals = Principal(tronms)


from .views.load import load
from .views.dashboard import dashboard
from .views.carrier import carrier
from .views.static import static
tronms.register_blueprint(load)
tronms.register_blueprint(carrier)
tronms.register_blueprint(dashboard)
tronms.register_blueprint(static)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
tronms.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

from tronms import views, models

