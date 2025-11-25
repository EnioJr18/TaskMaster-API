import sqlite3

conn = sqlite3.connect('taskmaster.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status INTEGER DEFAULT 0
    );
''');

conn.commit()
conn.close()
print("Banco de dados e tabela criados com sucesso.")
