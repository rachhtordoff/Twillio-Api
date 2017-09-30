from flask import request, Blueprint, Response, jsonify, current_app

general = Blueprint('general', __name__)


@general.route("/health")
def check_status():
    return jsonify({
        "app": "email",
        "status": "OK",
        "headers": request.headers.to_list(),
    })
