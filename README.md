# 🚀 TaskMaster API

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Microframework-lightgrey?style=flat&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=flat&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green)

O **TaskMaster** é uma API RESTful robusta desenvolvida para gerenciamento de tarefas. O projeto foi construído focando em **Arquitetura MVC**, **Clean Code** e **Segurança**, servindo como backend para aplicações de produtividade.

---

## 🏗️ Arquitetura do Projeto

O sistema segue o padrão **MVC (Model-View-Controller)** adaptado para APIs, garantindo separação de responsabilidades e facilidade de manutenção.

```text
CLIENTE (Postman/Frontend)
      ⬇️  (Requisição HTTP)
[ CONTROLLER ] --> Gerencia as rotas e valida a entrada de dados.
      ⬇️  (Chama métodos)
[   MODEL    ] --> Regras de negócio e manipulação de objetos.
      ⬇️  (SQL)
[ DATABASE ] --> Persistência dos dados (SQLite).


## ⚙️ Funcionalidades
CRUD Completo: Criação, Leitura, Atualização e Exclusão de tarefas.

Update Dinâmico (Smart Patch): Permite atualizar apenas um campo (ex: status) sem precisar re-enviar todo o objeto.

Persistência de Dados: Uso de banco SQL para armazenamento seguro.

Tratamento de Erros: Retornos HTTP adequados (200, 201, 400, 404).

## 🛠️ Instalação e Configuração
Siga os passos abaixo para rodar a API localmente:

1. Clone o repositório
Bash

git clone [https://github.com/SEU-USUARIO/projeto_taskmaster.git](https://github.com/SEU-USUARIO/projeto_taskmaster.git)
cd projeto_taskmaster

2. Configure o Ambiente Virtual
É recomendado usar um ambiente virtual para isolar as dependências.

#### Windows
python -m venv venv
.\venv\Scripts\activate

#### Linux/macOS
python3 -m venv venv
source venv/bin/activate

3. Instale as Dependências

pip install flask requests

4. Inicialize o Banco de Dados

python db_setup.py
Isso criará o arquivo taskmaster.db na raiz do projeto.

5. Execute o Servidor

python run.py
O servidor iniciará em http://127.0.0.1:5000.

## 📡 Documentação da API

1. Listar Tarefas
Retorna todas as tarefas cadastradas.

URL: /tasks

Método: GET

Resposta Sucesso (200):

JSON

[
  {
    "id": 1,
    "title": "Estudar Python",
    "description": "Focar em Flask e POO",
    "status": false
  }
]

2. Criar Tarefa
URL: /tasks

Método: POST

Corpo (JSON):

JSON

{
  "title": "Comprar Café",
  "description": "Café em grãos arábica"
}

3. Atualizar Tarefa (Dinâmico)
Você pode enviar apenas os campos que deseja alterar.

URL: /tasks/<id>

Método: PUT

Corpo (Exemplo - Mudar só status):

JSON

{
  "status": true
}

4. Deletar Tarefa
URL: /tasks/<id>

Método: DELETE

## 🧪 Testes Automatizados
O projeto inclui um script de testes de integração (testador.py) que simula um cliente real realizando todas as operações do CRUD.

Para rodar os testes (com o servidor ligado):

python testador.py

## 👨‍💻 Autor
Desenvolvido por Enio Jr como parte de um portfólio de Engenharia de Software Backend.

📧 Entre em contato: eniojr100@gmail.com 🔗 LinkedIn: [Link do seu LinkedIn]