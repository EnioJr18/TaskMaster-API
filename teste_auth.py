import requests

BASE = "http://127.0.0.1:5000"

def debug_request(response):
    """Função auxiliar para ver o erro real"""
    print(f"Status Code: {response.status_code}")
    try:
        print("JSON:", response.json())
    except Exception:
        print("NÃO É JSON! O servidor respondeu texto/HTML:")
        print(response.text) # <--- AQUI VAMOS VER O ERRO REAL

# 1. Tentar criar usuário
print("--- TENTANDO REGISTRAR ---")
resp = requests.post(f"{BASE}/register", json={"username": "enio", "password": "123"})
debug_request(resp)

# 2. Tentar logar (pegar token)
print("\n--- TENTANDO LOGAR ---")
resp = requests.post(f"{BASE}/login", json={"username": "enio", "password": "123"})

if resp.status_code == 200:
    try:
        token = resp.json()['token']
        print(f"SUCESSO! Token recebido: {token[:20]}...")
    except:
        print("Logou mas não veio token?")
        print(resp.text)
else:
    print("Erro no login:")
    debug_request(resp)
