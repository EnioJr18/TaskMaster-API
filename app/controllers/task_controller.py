from flask import jsonify, request
from app import app
from app.models.task_manager import TaskManager

manager = TaskManager()


@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks_lists = manager.get_all_tasks()
    return jsonify(tasks_lists), 200


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Dados inválidos'}), 400

    new_task = manager.add_task(data['title'], data['description'])
    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    sucesso = manager.delete_task(task_id)
    if sucesso:
        return jsonify({'message': 'Tarefa deletada com sucesso'}), 200
    else:
        return jsonify({'error': 'Tarefa não encontrada'}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json

    campos_validos = ['title', 'description', 'status']
    if not any(campo in data for campo in campos_validos):
        return jsonify({'erro': 'Envie pelo menos um campo para atualizar'}), 400

    sucesso = manager.update_task(task_id, data)

    if sucesso:
        return jsonify({"message": "Tarefa atualizada com sucesso!"}), 200
    else:
        return jsonify({"erro": "Tarefa não encontrada!"}), 404
