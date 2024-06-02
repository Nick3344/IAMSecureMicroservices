from flask import jsonify
from werkzeug.exceptions import BadRequest, Unauthorized, InternalServerError

def handle_bad_request(e):
    response = jsonify(error=str(e))
    response.status_code = BadRequest.code
    return response

def handle_unauthorized(e):
    response = jsonify(error=str(e))
    response.status_code = Unauthorized.code
    return response

def handle_internal_server_error(e):
    response = jsonify(error="Internal Server Error")
    response.status_code = InternalServerError.code
    return response

def register_error_handlers(app):
    app.register_error_handler(BadRequest, handle_bad_request)
    app.register_error_handler(Unauthorized, handle_unauthorized)
    app.register_error_handler(InternalServerError, handle_internal_server_error)
