from flask import jsonify, request
from app import app
from app.models.task_manager import TaskManager
from app.utils.auth import token_required

manager = TaskManager()


@app.route('/tasks', methods=['GET'])
@token_required
def list_tasks():
    """
    Listar tarefas (com filtro opcional)
    ---
    tags:
      - Tarefas
    security:
      - Bearer: []
    parameters:
      - name: status
        in: query
        type: boolean
        required: false
        description: Filtre por 'true' (concluídas) ou 'false' (pendentes)
    responses:
      200:
        description: Lista de tarefas recuperada com sucesso
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              description:
                type: string
              status:
                type: boolean
    """
    status = request.args.get('status')
    print(f"👀 O Controller recebeu o filtro: {status}")
    tasks_lists = manager.get_all_tasks(status)
    return jsonify(tasks_lists), 200


@app.route('/tasks', methods=['POST'])
@token_required
def create_task():
    """
    Criar uma nova tarefa
    ---
    tags:
      - Tarefas
    security:
      - Bearer: []
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - title
          properties:
            title:
              type: string
              example: "Estudar Swagger"
            description:
              type: string
              example: "Aprender a documentar APIs"
    responses:
      201:
        description: Tarefa criada com sucesso
      400:
        description: Erro de validação
    """
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Dados inválidos'}), 400
    
    desc = data.get('description', '') 
    new_task = manager.add_task(data['title'], desc)
    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(task_id):
    """
    Deletar uma tarefa pelo ID
    ---
    tags:
      - Tarefas
    security:
      - Bearer: []
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa a ser deletada
    responses:
      200:
        description: Tarefa deletada com sucesso
      404:
        description: Tarefa não encontrada
    """
    sucesso = manager.delete_task(task_id)
    if sucesso:
        return jsonify({'message': 'Tarefa deletada com sucesso'}), 200
    else:
        return jsonify({'error': 'Tarefa não encontrada'}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
@token_required
def update_task(task_id):
    """
    Atualizar uma tarefa pelo ID
    ---
    tags:
      - Tarefas
    security:
      - Bearer: []
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Novo Título"
            description:
              type: string
              example: "Nova Descrição"
            status:
              type: boolean
              example: true
    responses:
      200:
        description: Tarefa atualizada com sucesso
      400:
        description: Erro de validação
      404:
        description: Tarefa não encontrada
    """
    data = request.json
    campos_validos = ['title', 'description', 'status']
    
    if not any(campo in data for campo in campos_validos):
        return jsonify({'erro': 'Envie pelo menos um campo para atualizar'}), 400

    sucesso = manager.update_task(task_id, data)

    if sucesso:
        return jsonify({"message": "Tarefa atualizada com sucesso!"}), 200
    else:
        return jsonify({"erro": "Tarefa não encontrada!"}), 404
