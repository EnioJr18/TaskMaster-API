from flask import Flask

app = Flask(__name__)


from app.controllers import task_controller
from app.controllers import auth_controller
from app.controllers import view_controller  