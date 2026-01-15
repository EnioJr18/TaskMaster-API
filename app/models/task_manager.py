import sqlite3
from app.models.task import Task


class TaskManager:
    def __init__(self, db_path='taskmaster.db'):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def add_task(self, title, description):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO tasks (title, description, status)
            VALUES (?, ?, 0)
        ''', (title, description))

        conn.commit()
        new_id = cursor.lastrowid
        conn.close()

        return Task(new_id, title, description).to_dict()

    def get_all_tasks(self, status_filter=None, limit=None, offset=None):
        conn = self._get_connection()
        cursor = conn.cursor()

        query = 'SELECT * FROM tasks'
        params = []

        if status_filter is not None:
            query += ' WHERE status = ?'

            
            if str(status_filter).lower() == 'true':
                params.append(1)
            else:
                params.append(0)

        if limit is not None and offset is not None:
            query += ' LIMIT ? OFFSET ?'
            params.append(limit)
            params.append(offset)

        cursor.execute(query, params)
        tasks = cursor.fetchall()
        conn.close()

        task_list = []
        for task in tasks:
            task_list.append({
                'id': task[0],
                'title': task[1],
                'description': task[2],
                'status': bool(task[3])
            })

        return task_list

    def delete_task(self, task_id):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()

        rows_affected = cursor.rowcount
        conn.close()

        return rows_affected > 0

    def update_task(self, task_id, data):
        conn = self._get_connection()
        cursor = conn.cursor()

        campos_para_atualizar = []
        valores = []

        if 'title' in data:
            campos_para_atualizar.append("title = ?")
            valores.append(data['title'])

        if 'description' in data:
            campos_para_atualizar.append("description = ?")
            valores.append(data['description'])

        if 'status' in data:
            campos_para_atualizar.append("status = ?")
            valores.append(int(data['status']))

        if not campos_para_atualizar:
            conn.close()
            return False

        valores.append(task_id)
        sql = f"UPDATE tasks SET {', '.join(campos_para_atualizar)} WHERE id = ?"
        cursor.execute(sql, valores)
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()

        return rows_affected > 0
