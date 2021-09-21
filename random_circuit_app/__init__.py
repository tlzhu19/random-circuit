import os
from flask import Flask

app = Flask(__name__)

# For the forms
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SESSION_COOKIE_SECURE'] = False  # to fix issue when deploying?