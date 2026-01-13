from flask import request, jsonify
import datetime
import jwt
from app import app
from app.models.user_manager import UserManager

user_manager = UserManager()

Secrety_KEY = 'minha_chave_secreta_aqui_do_taskmanager'


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Usuário and senha são necessário.'}), 400

    if user_manager.create_user(username, password):
        return jsonify({'message': 'Usuário criado com sucesso.'}), 201
    else:
        return jsonify({'message': 'Usuário já existe.'}), 409


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user_id = user_manager.verify_user(username, password)

    if user_id:
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, Secrety_KEY, algorithm='HS256')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Credenciais inválidas.'}), 401

