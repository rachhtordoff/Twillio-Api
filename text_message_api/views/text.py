from flask import(
    request,
    Blueprint,
    Response,
    jsonify,
    current_app
)
import json
from text_message_api import config
from text_message_api import app
from twilio.rest import Client

# This is the blueprint object that gets registered into the app in blueprints.py.
text = Blueprint('text', __name__,
                    template_folder='templates')
 #test comment
@text.route("/send-text", methods=['POST'])
def send_text():
    """
    This route will send a text message to the number defined in the env
    variables.
    """
    current_app.logger.info('Sending a text message')
    json_data = request.json
    message = f"{json_data['messagehead']} {json_data['message']} {json_data['link']}"
    client = Client(config.TEXT_ACCOUNT, config.TEXT_TOKEN)
    message = client.messages.create(to="+44" +  config.NUMBER_TO,
                                 from_=config.NUMBER_FROM,
                                 body=message)
