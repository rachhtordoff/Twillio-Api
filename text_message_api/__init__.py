from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")

from text_message_api.blueprints import register_blueprints

# Register blueprints
register_blueprints(app)
