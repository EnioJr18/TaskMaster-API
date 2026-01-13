import requests

BASE = "http://127.0.0.1:5000"
USUARIO = "admin_supremo"
SENHA = "123"

def testar_sistema_seguro():
    print("--- 🤖 INICIANDO TESTE DE SEGURANÇA ---\n")

    # 1. Tenta acessar rota protegida (Deve ser bloqueado)
    print("🔐 1. Tentando acessar tarefas sem token...")
    resp = requests.get(f"{BASE}/tasks")
    if resp.status_code == 401:
        print("✅ SUCESSO: O guarda barrou o acesso (401 Unauthorized).")
    else:
        print(f"❌ FALHA: A rota está aberta! Status: {resp.status_code}")
        return

    # 2. Registra o usuário (Garante que ele existe)
    print(f"\n👤 2. Registrando usuário '{USUARIO}'...")
    resp = requests.post(f"{BASE}/register", json={"username": USUARIO, "password": SENHA})
    if resp.status_code == 201:
        print("✅ Usuário criado.")
    elif resp.status_code == 409: # 409 = Conflict (Já existe)
        print("ℹ️ Usuário já existia, prosseguindo...")
    else:
        print(f"❌ Erro ao criar usuário: {resp.text}")
        return

    # 3. Faz Login para pegar o Token
    print(f"\n🔑 3. Fazendo Login...")
    resp = requests.post(f"{BASE}/login", json={"username": USUARIO, "password": SENHA})
    
    if resp.status_code != 200:
        print(f"❌ Erro fatal no login: {resp.text}")
        return

    token = resp.json()['token']
    print(f"✅ Token recebido: {token}...")

    # 4. Usa o token para acessar a rota protegida
    print("\n📝 4. Acessando tarefas COM token...")
    headers = {'Authorization': token} # <--- O segredo está aqui
    
    # Criando uma tarefa de teste
    nova_tarefa = {"title": "Testar JWT", "description": "Funciona mesmo?"}
    resp = requests.post(f"{BASE}/tasks", json=nova_tarefa, headers=headers)
    
    if resp.status_code == 201:
        print("✅ SUCESSO TOTAL: Tarefa criada na área restrita!")
        print("Resposta:", resp.json())
    else:
        print(f"❌ Falha ao criar tarefa: {resp.status_code}")

if __name__ == "__main__":
    try:
        testar_sistema_seguro()
    except Exception as e:
        print(f"Erro de conexão: {e}")
        print("Verifique se o 'run.py' está rodando em outro terminal!")