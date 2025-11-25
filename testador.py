import requests
import time

BASE_URL = "http://127.0.0.1:5000"

def testar_crud():
    print("🤖 INICIANDO TESTE DO SISTEMA...")
    
    # 1. CRIAR (Create)
    print("\n[1] Criando tarefa...")
    nova_tarefa = {"title": "Testar API", "description": "Rodar o script final"}
    resp = requests.post(f"{BASE_URL}/tasks", json=nova_tarefa)
    if resp.status_code == 201:
        id_tarefa = resp.json()['id']
        print(f"✅ Sucesso! ID criado: {id_tarefa}")
    else:
        print("❌ Erro ao criar")
        return

    # 2. LER (Read)
    print("\n[2] Verificando se salvou...")
    resp = requests.get(f"{BASE_URL}/tasks")
    print(f"📋 Lista atual: {resp.json()}")

    # 3. ATUALIZAR (Update)
    print(f"\n[3] Atualizando a tarefa {id_tarefa} para 'Concluída'...")
    dados_atualizados = {
        "title": "Testar API (Atualizado)", 
        "description": "Rodar o script final", 
        "status": True
    }
    resp = requests.put(f"{BASE_URL}/tasks/{id_tarefa}", json=dados_atualizados)
    print(f"🔄 Status da atualização: {resp.status_code}")

    # 4. DELETAR (Delete)
    print(f"\n[4] Deletando a tarefa {id_tarefa}...")
    resp = requests.delete(f"{BASE_URL}/tasks/{id_tarefa}")
    print(f"🗑️ Status da deleção: {resp.status_code}")

    # 5. VERIFICAÇÃO FINAL
    print("\n[5] Verificando se sumiu...")
    resp = requests.get(f"{BASE_URL}/tasks")
    tarefas = resp.json()
    # Verifica se a lista está vazia ou se o ID sumiu
    tem_a_tarefa = any(t['id'] == id_tarefa for t in tarefas)
    if not tem_a_tarefa:
        print("✅ A tarefa foi removida corretamente do banco!")
    else:
        print("❌ A tarefa ainda está lá...")

if __name__ == "__main__":
    try:
        testar_crud()
    except Exception as e:
        print(f"Erro: {e}")