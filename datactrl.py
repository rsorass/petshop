import sqlite3
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha TEXT NOT NULL
                )""")

user_procurado = "NIJfaueenej"

cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (user_procurado,))
resultado = cursor.fetchone()
if resultado == None:
    print(f"O usuário {user_procurado} não existe, por favor, insira valores válidos.")
else:
    print(resultado)

conexao.commit()
conexao.close()