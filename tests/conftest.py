import pytest
import os
import sqlite3
from app import app
from app.models.task_manager import TaskManager
from app.models.user_manager import UserManager
from app.controllers import task_controller, auth_controller

TEST_DB = 'test_taskmaster.db'


@pytest.fixture
def client():
    # 1. Configurações Iniciais
    app.config['TESTING'] = True
    app.config['DATABASE'] = TEST_DB
    app.config['SECRET_KEY'] = 'chave_super_secreta_de_teste'

    # 2. Setup do Banco de Dados (Criar tabelas do zero)
    # Criamos instâncias que apontam para o banco de teste
    test_task_manager = TaskManager(TEST_DB)
    test_user_manager = UserManager(TEST_DB)

    task_controller.manager = test_task_manager
    auth_controller.user_manager = test_user_manager
    # ----------------------------------------

    # Criar as tabelas (Tasks E Users)
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    # Tabela de Tarefas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status INTEGER NOT NULL DEFAULT 0
        )
    ''')

    # Tabela de Usuários (Crucial para o Login!)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL  
        )
    ''')
    conn.commit()
    conn.close()

    # 3. Yield (Entrega o cliente para o teste rodar)
    with app.test_client() as client:
        with app.app_context():
            yield client

    # 4. Teardown (Limpeza depois que o teste acaba)
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
        print(f"\n🗑️ Banco de teste {TEST_DB} removido.")
