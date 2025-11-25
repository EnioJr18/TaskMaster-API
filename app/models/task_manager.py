import sqlite3
from app.models.task import Task


class TaskManager:
    def __init__(self):
        self.db_path = 'taskmaster.db'

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

    def get_all_tasks(self):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT id, title, description, status FROM tasks')
        rows = cursor.fetchall()

        tasks = []
        for row in rows:
            task = Task(id=row[0], title=row[1],
                        description=row[2], status=bool(row[3]))
            tasks.append(task)

        conn.close()

        return [task.to_dict() for task in tasks]

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
    
        