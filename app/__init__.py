from flask import Flask
from flasgger import Swagger

app = Flask(__name__)

# --- Configuração do Swagger ---
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs",
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "TaskMaster API",
        "description": "API para gerenciamento de tarefas com Auth JWT",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Bearer {token}\""
        }
    },
}

Swagger(app, config=swagger_config, template=swagger_template)

# Imports dos controllers DEVEM ficar no final para evitar erro circular
from app.controllers import auth_controller
from app.controllers import task_controller
# Se você criou o view_controller, descomente a linha abaixo:
# from app.controllers import view_controller