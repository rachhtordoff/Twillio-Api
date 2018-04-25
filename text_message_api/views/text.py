from flask import request, Blueprint, Response, jsonify, current_app
from flask import current_app
import json
from text_message_api.exceptions import ApplicationError
from text_message_api import config
from text_message_api import app
from twilio.rest import Client

# This is the blueprint object that gets registered into the app in blueprints.py.
text = Blueprint('text', __name__,
                    template_folder='templates')
 #test comment
@text.route("/send-priority-1", methods=['POST'])
def send_text():
    json_data = request.json
    number= json_data['number']
    current_app.logger.info('sending a text message')
    message = json_data['messagehead'] + '  '+ json_data['message'] + '  ' + json_data['link'] + '  ' + json_data['signature']
    client = Client(config.TEXT_ACCOUNT, config.TEXT_TOKEN)
    message = client.messages.create(to="+44" + number[1:], from_="+441173253472",
                                 body=message)
    return "yay"

@text.route("/send-priority-2/<id>", methods=['POST'])
def send_text_if_condition():

    return "temp"

def check_if_text_true(company_id):
    resp = requests.get(config.DOCUMENT_API_URL+ '/email_notifications/' + str(client_id))
    data = json.loads(resp.text)
    return data
