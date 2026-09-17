import sqlite3
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha TEXT NOT NULL
                )""")

conexao.commit()
conexao.close()