from functools import wraps
from flask import request, jsonify
import jwt
from app.controllers.auth_controller import Secrety_KEY


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'Token de autenticação ausente!'}), 401

        try:
            data = jwt.decode(token, Secrety_KEY, algorithms=['HS256'])

            current_user_id = data['user_id']

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirou, faça login novamente!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido!'}), 401

        return f(*args, **kwargs)
    return decorated
