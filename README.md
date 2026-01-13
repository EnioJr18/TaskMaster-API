# 🛡️ TaskMaster API

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/flask-2.3.x-lightgrey?style=flat&logo=flask)
![Swagger](https://img.shields.io/badge/docs-Swagger_UI-green?style=flat&logo=swagger)
![Security](https://img.shields.io/badge/security-JWT-orange?style=flat&logo=json-web-tokens)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

> Uma API RESTful robusta com documentação interativa, arquitetura MVC e autenticação segura.

O **TaskMaster** é um sistema de backend desenvolvido para demonstrar boas práticas de Engenharia de Software. O projeto vai além do CRUD básico, implementando **Swagger UI** para testes em tempo real, **Autenticação JWT** manual e **Segurança de Dados**.

---

## 📄 Documentação Interativa (Swagger UI)

Esqueça o Postman! Este projeto possui documentação viva gerada automaticamente.
Após rodar o servidor, acesse:

👉 **http://127.0.0.1:5000/apidocs**

Lá você pode:
1.  Visualizar todas as rotas e os dados esperados (JSON).
2.  Testar as requisições direto pelo navegador.
3.  Entender os códigos de erro (400, 401, 404).

---

## 🚀 Destaques Tecnológicos

* **Documentação Automática:** Integração com `Flasgger` para gerar especificações OpenAPI 2.0.
* **Autenticação JWT:** Middleware customizado para proteção de rotas.
* **Password Hashing:** As senhas são criptografadas com `pbkdf2:sha256`.
* **Arquitetura MVC:** Separação clara entre Models, Controllers e Views.
* **Smart Updates (PATCH):** Atualização parcial de recursos sem sobrescrever dados não enviados.
* **Segurança SQL:** Prevenção total contra SQL Injection usando Parameterized Queries.

---

## 🛠️ Instalação e Execução

### 1. Clone e Prepare o Ambiente
```bash
git clone [https://github.com/EnioJr18/TaskMaster-API.git](https://github.com/EnioJr18/TaskMaster-API.git)
cd TaskMaster-API
```

# Crie o ambiente virtual
```bash
python -m venv venv
```
# Ative o ambiente
```bash
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```
2. Instale as Dependências
```bash
pip install -r requirements.txt
```
3. Prepare o Banco de Dados
```bash
python db_setup.py
```
4. Inicie o Servidor
```bash
python run.py
```
O servidor rodará em http://127.0.0.1:5000

🔐 Como Testar Rotas Protegidas (No Swagger)
Como a API é segura, você precisa de um "crachá" (Token) para acessar as rotas de tarefas. Siga os passos na interface do Swagger:

1. Vá na rota POST /register e crie um usuário.
2. Vá na rota POST /login e faça o login.
3. Copie o token gerado na resposta (ex: eyJhbG...).
4.No topo da página, clique no botão verde Authorize.
5.Digite: Bearer SEU_TOKEN_AQUI (Com a palavra Bearer e um espaço antes).
6.Clique em Authorize e feche a janela.

Pronto! Agora os cadeados das rotas de Tarefas abrirão e você poderá testar GET, POST, PUT e DELETE.

🧪 Testes Automatizados
O projeto inclui um script robô que simula um usuário real para validar o fluxo completo (Login -> Token -> CRUD).

```bash
python testador_seguro.py
```
📂 Estrutura do Projeto
```bash
app/
├── controllers/       # Rotas da API (Lógica de entrada)
│   ├── auth_controller.py
│   └── task_controller.py
├── models/            # Regras de Negócio e SQL (DAO)
│   ├── user_manager.py
│   └── task_manager.py
├── templates/         # Interface Web Simples (Front-end)
├── utils/             # Decorators de Segurança (Auth)
└── __init__.py        # Configuração do Flask e Swagger
```

## 🚧 Roadmap & Melhorias Futuras
Este projeto está em constante evolução. Os próximos passos incluem:

[ ] Docker: Containerização da aplicação para fácil deploy. <br>
[x] Swagger UI: Documentação interativa automática. <br>
[ ] Testes Unitários: Implementação de Pytest com cobertura de código. <br>
[ ] Filtros Avançados: Busca de tarefas por status ou título via Query Par. <br>

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor
Desenvolvido por Enio Jr como parte de um portfólio de Engenharia de Software Backend.

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
