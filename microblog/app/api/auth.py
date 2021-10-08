from flask_httpauth import HTTPBasicAuth
from app.models import Mbluser
from app.api.errors import error_response
from flask_httpauth import HTTPTokenAuth

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    user = Mbluser.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)

@token_auth.verify_token
def verify_token(token):
    return Mbluser.check_token(token) if token else None

@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)