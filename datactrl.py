import sqlite3
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha TEXT NOT NULL
                )""")

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""CREATE TABLE IF NOT EXISTS pets (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade_meses INTEGER NOT NULL,

                dono_id INTEGER,
                FOREIGN KEY (dono_id) REFERENCES usuarios(id)
                )""")

user_procurado = None
cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (user_procurado,))
resultado = cursor.fetchone()
if resultado == None:
    print(f"O usuário {user_procurado} não existe, por favor, insira valores válidos.")
else:
    print(resultado)

conexao.commit()
conexao.close()