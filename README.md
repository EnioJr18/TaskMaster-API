# 🛡️ TaskMaster API

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/flask-2.3.x-lightgrey?style=flat&logo=flask)
![Security](https://img.shields.io/badge/security-JWT-orange?style=flat&logo=json-web-tokens)
![Status](https://img.shields.io/badge/status-active-success?style=flat)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

## 📖 Sobre o Projeto

O **TaskMaster API** não é apenas um gerenciador de tarefas; é um estudo prático sobre **Arquitetura de Software** e **Desenvolvimento Backend Moderno**. 

O objetivo principal deste projeto foi construir uma aplicação que fugisse dos básico, implementando padrões reais de mercado como **MVC (Model-View-Controller)**, separação de responsabilidades e manipulação direta de banco de dados SQL sem dependência excessiva de ORMs, garantindo performance e controle total sobre as queries.

Este projeto simula o backend de uma aplicação de produtividade (como Todoist ou Trello), pronto para ser consumido por clientes Front-end (React, Vue) ou Mobile.

---

## 🧠 Arquitetura e Design

O projeto segue estritamente o padrão **MVC (Model-View-Controller)** adaptado para APIs, garantindo a separação de responsabilidades (SoC).

### Fluxo da Aplicação<br>
graph LR<br>
    A[Cliente] -->|Request + Token| B(Middleware Auth)<br>
    B -->|Aprovado| C{Controller}<br>
    C -->|Regras de Negócio| D[Model Manager]<br>
    D -->|SQL Query| E[(SQLite Database)]<br>
    E -->|Dados| D<br>
    D -->|Objetos| C<br>
    C -->|JSON| A<br>

## 📂 Estrutura de Pastas
A organização do código reflete a separação lógica:

projeto_taskmaster/ <br>
│ <br>
├── app/ <br>
│   ├── __init__.py          # Inicialização do App e Flask<br>
│   ├── controllers/         # Rotas e validação de entrada (HTTP)<br>
│   │   ├── auth_controller.py<br>
│   │   └── task_controller.py<br>
│   ├── models/              # Lógica de negócios e acesso a dados (DAO)<br>
│   │   ├── task.py<br>
│   │   ├── task_manager.py<br>
│   │   └── user_manager.py<br>
│   └── utils/               # Utilitários e Decorators<br>
│       └── auth.py          # Lógica de verificação JWT<br>
│<br>
├── db_setup.py              # Script de migração/criação do banco<br>
├── run.py                   # Ponto de entrada do servidor<br>
├── config.py                # Variáveis de ambiente e segredos<br>
└── requirements.txt         # Dependências do projeto<br>

## ⚙️ Funcionalidades
**Gerenciamento de Tarefas (CRUD)** <br>
-Criação de Tarefas: Adicionar novas tarefas com título e descrição.<br>
-Listagem de Tarefas: Visualizar todas as tarefas cadastradas no sistema.<br>
-Atualização Inteligente: Editar tarefas existentes. O sistema suporta edição parcial (ex: mudar apenas o status para "Concluído" sem precisar reescrever o título).<br>
-Exclusão de Tarefas: Remover tarefas permanentemente do banco de dados.<br>

**Gerenciamento de Usuários (Autenticação)** <br>
-Registro de Conta: Permite que novos usuários criem uma conta fornecendo usuário e senha.<br>
-Login Seguro: Autenticação via credenciais que retorna um Token de Acesso (JWT) temporário.<br>
-Sessão Stateless: Não requer cookies de sessão; o acesso é garantido puramente via token.<br>

## ⚙️ Funcionalidades Técnicas (Engenharia e Código) <br>
**Segurança Avançada**<br>
-Criptografia de Senhas: Utiliza o algoritmo pbkdf2:sha256 para hashing. As senhas nunca são salvas em texto puro no banco.<br>
-Proteção via Decorators: Implementação de um middleware @token_required que intercepta requisições e valida a assinatura do JWT antes de permitir o acesso à rota.<br>
-Prevenção contra SQL Injection: Uso estrito de Parameterized Queries (placeholders ?) em todas as camadas de acesso ao banco.<br>

**Arquitetura e Design** <br>
-Padrão MVC: Separação clara entre Rotas (Controllers), Lógica de Negócio/Dados (Models) e Utilitários.<br>
-Persistência SQL: Uso de banco de dados relacional (SQLite) com criação automática de tabelas e relacionamentos.<br>
-API RESTful: Endpoints padronizados utilizando os verbos HTTP corretos (GET, POST, PUT, DELETE) e códigos de status semânticos (200, 201, 400, 401, 404).<br>

**Lógica Otimizada** <br>
-Construtor de Queries Dinâmico: O método de atualização (UPDATE) detecta quais campos foram enviados no JSON e monta a string SQL sob demanda, evitando sobrescrita acidental de dados.<br>

## 🚀 Destaques Técnicos
**Autenticação JWT (JSON Web Token)**: Implementação manual de um sistema de login seguro. O token é exigido no Header para rotas protegidas.

**Password Hashing**: As senhas são criptografadas com pbkdf2:sha256 antes de serem salvas, garantindo que nem mesmo o admin tenha acesso às senhas originais.

**Smart Updates (PATCH/PUT)**: O sistema utiliza construção dinâmica de SQL para permitir atualizações parciais. Você pode enviar apenas o campo que deseja alterar (ex: status) sem sobrescrever o resto do objeto.

**Prevenção de SQL Injection**: Uso rigoroso de Parameterized Queries (placeholders ?) em todas as interações com o banco.

**Tratamento de Erros**: Respostas HTTP padronizadas (400 para erro do cliente, 401 para não autorizado, 404 para não encontrado).

## 🛠️ Instalação e Execução
Pré-requisitos<br>
Python 3.10 ou superior

Passo a Passo
Clone o repositório:

git clone [https://github.com/EnioJr18/TaskMaster-API.git](https://github.com/EnioJr18/TaskMaster-API.git)
cd TaskMaster-API

Crie e ative o ambiente virtual:
# Windows
python -m venv venv<br>
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv<br>
source venv/bin/activate

Instale as dependências:<br>
pip install -r requirements.txt

Prepare o Banco de Dados:<br>
python db_setup.py<br>
(Isso criará o arquivo taskmaster.db e as tabelas necessárias)

Inicie o Servidor:<br>
python run.py

## 🔑 Documentação da API

Autenticação
Método     Endpoint     Descrição             Body Necessário<br>
POST       /register    Cria novo usuário     "{""username"": ""..."", ""password"": ""...""}" <br>
POST       /login       Retorna o Token JWT   "{""username"": ""..."", ""password"": ""...""}" <br>

Tarefas (Requer Token)
Header Obrigatório: Authorization: <SEU_TOKEN_AQUI>

Método     Endpoint      Descrição                  Exemplo de Body <br>
GET        /tasks        Lista todas as tarefas     N/A <br>
POST       /tasks        Cria nova tarefa           "{""title"": ""Estudar"", ""description"": ""SQL""}" <br>
PUT        /tasks/<id>,  Atualiza (Parcial/Total)   "{""status"": true}" <br>
DELETE     /tasks/<id>,  Remove uma tarefa          N/A <br>




## 🧪 Testes Automatizados
O projeto inclui scripts para validação de funcionamento e segurança.

Para testar o fluxo completo (Auth + CRUD): Certifique-se que o servidor está rodando e execute:
python testador_seguro.py

## 🚧 Roadmap & Melhorias Futuras
Este projeto está em constante evolução. Os próximos passos incluem:

[ ] Docker: Containerização da aplicação para fácil deploy. <br>
[ ] Swagger UI: Documentação interativa automática. <br>
[ ] Testes Unitários: Implementação de Pytest com cobertura de código. <br>
[ ] Filtros Avançados: Busca de tarefas por status ou título via Query Par. <br>

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor
Desenvolvido por Enio Jr como parte de um portfólio de Engenharia de Software Backend.

📧 Entre em contato: eniojr100@gmail.com 🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ 📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
