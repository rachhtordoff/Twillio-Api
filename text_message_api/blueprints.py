from text_message_api import app
from text_message_api.views import text

def register_blueprints(app):
    """
    Adds all blueprint objects into the app.
    """
    app.register_blueprint(text.text)

    # All done!
    app.logger.info("Blueprints registered")
