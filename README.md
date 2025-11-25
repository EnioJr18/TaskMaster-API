# 🚀 TaskMaster API

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Microframework-lightgrey?style=flat&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=flat&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green)


## 📖 Sobre o Projeto

O **TaskMaster API** não é apenas um gerenciador de tarefas; é um estudo prático sobre **Arquitetura de Software** e **Desenvolvimento Backend Moderno**. 

O objetivo principal deste projeto foi construir uma aplicação que fugisse dos básico, implementando padrões reais de mercado como **MVC (Model-View-Controller)**, separação de responsabilidades e manipulação direta de banco de dados SQL sem dependência excessiva de ORMs, garantindo performance e controle total sobre as queries.

Este projeto simula o backend de uma aplicação de produtividade (como Todoist ou Trello), pronto para ser consumido por clientes Front-end (React, Vue) ou Mobile.

---

## 🏗️ Arquitetura do Projeto

O sistema segue o padrão **MVC (Model-View-Controller)** adaptado para APIs, garantindo separação de responsabilidades e facilidade de manutenção.


CLIENTE (Postman/Frontend)
      ⬇️  (Requisição HTTP)
[ CONTROLLER ] --> Gerencia as rotas e valida a entrada de dados.
      ⬇️  (Chama métodos)
[   MODEL    ] --> Regras de negócio e manipulação de objetos.
      ⬇️  (SQL)
[ DATABASE ] --> Persistência dos dados (SQLite).


## ⚙️ Funcionalidades
**CRUD Completo**: Criação, Leitura, Atualização e Exclusão de tarefas.

**Update Dinâmico** (Smart Patch): Permite atualizar apenas um campo (ex: status) sem precisar re-enviar todo o objeto.

**Persistência de Dados**: Uso de banco SQL para armazenamento seguro.

**Tratamento de Erros**: Retornos HTTP adequados (200, 201, 400, 404).

## 🏆 Destaques Técnicos

O diferencial deste projeto reside nas decisões de implementação:

* **Design Pattern MVC:** O código não está jogado em um único arquivo. A lógica de rotas (`Controllers`) está totalmente desacoplada da lógica de dados (`Models`), facilitando a manutenção e testes.
* **Smart Updates (PATCH Logic):** A implementação do método `PUT` possui lógica dinâmica. O sistema detecta quais campos foram enviados e monta a query SQL em tempo de execução, permitindo atualizações parciais eficientes sem sobrescrever dados não informados.
* **Segurança (SQL Injection):** Todas as interações com o banco de dados utilizam *Parameterized Queries* (Placeholders `?`), prevenindo ataques de injeção de SQL.
* **Tratamento de Dados:** Conversão automática de tipos (booleans do JSON para integers do SQLite e vice-versa) garantindo a integridade dos dados na persistência.

## 🛠️ Instalação e Configuração
Siga os passos abaixo para rodar a API localmente:

##### 1. Clone o repositório

git clone [https://github.com/SEU-USUARIO/projeto_taskmaster.git](https://github.com/SEU-USUARIO/projeto_taskmaster.git)
cd projeto_taskmaster

##### 2. Configure o Ambiente Virtual
É recomendado usar um ambiente virtual para isolar as dependências.

##### Windows
python -m venv venv
.\venv\Scripts\activate

##### Linux/macOS
python3 -m venv venv
source venv/bin/activate

##### 3. Instale as Dependências

pip install flask requests

##### 4. Inicialize o Banco de Dados

python db_setup.py
Isso criará o arquivo taskmaster.db na raiz do projeto.

##### 5. Execute o Servidor

python run.py
O servidor iniciará em http://127.0.0.1:5000.

## 📡 Documentação da API

*1. Listar Tarefas*
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

*2. Criar Tarefa*
URL: /tasks
Método: POST
Corpo (JSON):
JSON
{
  "title": "Comprar Café",
  "description": "Café em grãos arábica"
}

*3. Atualizar Tarefa (Dinâmico)*
Você pode enviar apenas os campos que deseja alterar.
URL: /tasks/<id>
Método: PUT
Corpo (Exemplo - Mudar só status):
JSON
{
  "status": true
}

*4. Deletar Tarefa*
URL: /tasks/<id>
Método: DELETE


## 🧪 Testes Automatizados
O projeto inclui um script de testes de integração (testador.py) que simula um cliente real realizando todas as operações do CRUD.

Para rodar os testes (com o servidor ligado):

python testador.py

## 🚧 Roadmap & Melhorias Futuras

Este projeto está em evolução constante. Os próximos passos para a versão 2.0 incluem:

- [ ] **Autenticação JWT:** Implementar login e cadastro de usuários para que cada um veja apenas suas tarefas.
- [ ] **Dockerização:** Criar um `Dockerfile` e `docker-compose` para rodar a aplicação em containers isolados.
- [ ] **Testes Unitários:** Migrar do script de teste atual para o framework `pytest` com cobertura de código.
- [ ] **Swagger UI:** Adicionar documentação interativa automática das rotas.

## 👨‍💻 Autor
Desenvolvido por Enio Jr como parte de um portfólio de Engenharia de Software Backend.

📧 Entre em contato: eniojr100@gmail.com 🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ 📷 Instagram: https://www.instagram.com/enio_juniorrr/
