# Arquivo: tests/test_api.py

def test_register_and_login(client):
    """Teste 1: Garante que dá para criar usuário e logar"""
    
    # 1. Registrar
    payload = {"username": "usuario_teste_1", "password": "123"}
    client.post('/register', json=payload)

    # 2. Logar
    login_response = client.post('/login', json=payload)
    
    # 3. Conferir
    assert login_response.status_code == 200
    assert 'token' in login_response.get_json()


def test_create_and_list_tasks(client):
    """Teste 2: Garante que usuário logado consegue criar e ver tarefas"""
    
    # 1. Login (com um usuário novo para não misturar)
    auth_payload = {"username": "usuario_teste_2", "password": "123"}
    client.post('/register', json=auth_payload)
    login_resp = client.post('/login', json=auth_payload)
    token = login_resp.get_json()['token']
    
    headers = {'Authorization': f'Bearer {token}'}

    # 2. Criar Tarefa
    task_payload = {
        "title": "Aprender Pytest",
        "description": "Ficar fera em testes automatizados"
    }
    client.post('/tasks', json=task_payload, headers=headers)

    # 3. Listar Tarefas
    response_list = client.get('/tasks', headers=headers)
    
    # 4. Conferir
    assert response_list.status_code == 200
    dados = response_list.get_json()
    assert len(dados['data']) >= 1
    assert dados['data'][0]['title'] == "Aprender Pytest"