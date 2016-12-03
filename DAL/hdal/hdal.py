from flask import Flask
import sqlalchemy

app = Flask(__name__)

# TODO Configuration
app.config.update(dict(
    DATABASE=r'duma.db'
))

import hdal.views
