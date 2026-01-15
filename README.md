# 📋 TaskMaster API

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)
![Swagger](https://img.shields.io/badge/Swagger-UI-85EA2D?style=for-the-badge&logo=swagger)
![Pytest](https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge&logo=pytest)

O **TaskMaster** é uma API RESTful robusta desenvolvida para gerenciamento de tarefas. O projeto foi construído com foco em boas práticas de engenharia de software, incluindo autenticação JWT, documentação interativa, testes automatizados e containerização com Docker.

---

## 🚀 Funcionalidades

- **🔐 Autenticação Segura:** Sistema de Registro e Login com Tokens JWT (JSON Web Tokens).
- **📝 CRUD Completo:** Criação, Leitura, Atualização e Exclusão de tarefas.
- **🔍 Filtros Dinâmicos:** Filtragem de tarefas por status (Concluída/Pendente).
- **📄 Paginação:** Otimização de listagem com suporte a `limit` e `offset`.
- **📚 Documentação Interativa:** Swagger UI integrado para testar endpoints visualmente.
- **🐳 Containerização:** Pronto para rodar em qualquer ambiente via Docker.
- **🧪 Testes Automatizados:** Cobertura de testes de integração com Pytest.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.13
- **Framework Web:** Flask
- **Banco de Dados:** SQLite (SQL Puro/Raw SQL para performance e controle)
- **Documentação:** Flasgger (Swagger UI)
- **Testes:** Pytest & Unittest
- **Container:** Docker

---

## 📂 Estrutura do Projeto

```bash
projeto_taskmaster/
├── app/
│   ├── controllers/    # Lógica das rotas (Endpoints)
│   ├── models/         # Camada de acesso ao banco (SQL)
│   ├── utils/          # Decorators e utilitários (Auth)
│   └── __init__.py     # Configuração do App Flask
├── tests/              # Testes automatizados (Pytest)
├── .dockerignore       # Arquivos ignorados pelo Docker
├── Dockerfile          # Receita da imagem Docker
├── README.md           # Documentação do projeto
├── requirements.txt    # Dependências do Python
└── run.py              # Ponto de entrada da aplicação
```

## ⚡ Como Rodar o Projeto
Você pode rodar a aplicação localmente (com Python instalado) ou via Docker.

Opção 1: Rodando com Docker (Recomendado)
Construa a imagem:
```bash
docker build -t taskmaster-app .
```
Inicie o container:
```bash
docker run -p 5000:5000 taskmaster-app
```
Acesse: O sistema estará rodando em: http://localhost:5000/apidocs

Opção 2: Rodando Localmente (Python)
Clone o repositório:
```bash
git clone https://github.com/SEU-USUARIO/taskmaster.git
cd taskmaster
```
Crie e ative um ambiente virtual:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
Execute a aplicação:
```bash
python run.py
```

## 🧪 Rodando os Testes
O projeto conta com testes de integração que validam o fluxo de autenticação e manipulação de tarefas.

Para executar os testes, rode no terminal:
```bash
python -m pytest
```
## 📖 Documentação da API (Endpoints)
A documentação completa pode ser visualizada via Swagger UI (/apidocs), mas aqui está um resumo:

Autenticação
```bash
│Método  │Rota        │Descrição
│POST/   │register    │Cria um novo usuário.         
│POST/   │login       │Retorna o Token JWT de acesso.
```

Tarefas (Requer Header ```Authorization: Bearer <TOKEN>```)
```bash
Método	    Rota	        Descrição	                Params
GET 	    /tasks	        Lista tarefas do usuário.	?page=1&per_page=10&status=true
POST	    /tasks	        Cria uma nova tarefa.	    Body JSON
PUT 	    /tasks/{id}	    Atualiza uma tarefa.	    Body JSON
DELETE	    /tasks/{id}	    Remove uma tarefa.	        -
```

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor
Desenvolvido por Enio Jr como parte de um portfólio de Engenharia de Software Backend.

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
