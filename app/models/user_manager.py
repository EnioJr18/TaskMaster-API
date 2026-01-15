import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class UserManager:
    def __init__(self, db_path='taskmaster.db'):
        self.db_path = db_path

    def __get__connection(self):
        return sqlite3.connect(self.db_path)
    
    def create_user(self, username, password):
        conn = self.__get__connection()
        cursor = conn.cursor()

        password_hash = generate_password_hash(password)

        try:
            cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
            
            conn.commit()
            sucesso = True
        except sqlite3.IntegrityError:
            sucesso = False
        
        conn.close()
        return sucesso
    
    def verify_user(self, username, password):
        conn = self.__get__connection()
        cursor = conn.cursor()

        cursor.execute('SELECT id, password_hash FROM users WHERE username = ?', (username,))
        user_data = cursor.fetchone()
        
        conn.close()

        if not user_data:
            return None
        
        id_usuario, hash_salvo = user_data
        
        if check_password_hash(hash_salvo, password):
            return id_usuario
        else:
            return None