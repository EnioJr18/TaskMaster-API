from functools import wraps
from flask import request, jsonify
import jwt
from app.controllers.auth_controller import Secrety_KEY


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # 1. Tenta pegar do Header
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            # A lógica do "Bearer": separar a palavra do código
            try:
                # Divide "Bearer SEU_TOKEN" em duas partes e pega a segunda
                token = auth_header.split(" ")[1]
            except IndexError:
                # Se vier sem "Bearer" (só o código), tenta pegar direto
                token = auth_header

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
