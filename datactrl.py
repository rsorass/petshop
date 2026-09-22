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


cursor.execute("""CREATE TABLE IF NOT EXISTS comidas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                comida TEXT NOT NULL,
                imagem_url TEXT,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS brinquedos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                brinquedo TEXT NOT NULL,
                imagem_url TEXT,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS casinhas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                casinha TEXT NOT NULL,
                imagem_url TEXT,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS utilitarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                utilitario TEXT NOT NULL,
                imagem_url TEXT,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS serviços (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                serviço TEXT NOT NULL,
                imagem_url TEXT,
                preço FLOAT NOT NULL,
                data TEXT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS historico (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                produto_ou_serviço TEXT NOT NULL,
                imagem_url TEXT,
                preço FLOAT NOT NULL,
                data TEXT NOT NULL,

                cliente_id INTEGER,
                FOREIGN KEY (cliente_id) REFERENCES usuarios(id)
)""")

cursor.execute("""INSERT INTO comidas
                (comida, imagem_url, preço) VALUES
                ("Ração Premium Para Cachorro Adulto", "https://images.unsplash.com/photo-1684882726821-2999db517441?q=80&w=300", 89.90)""")

user_procurado = None
cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (user_procurado,))
resultado = cursor.fetchone()
if resultado == None:
    print(f"O usuário {user_procurado} não existe, por favor, insira valores válidos.")
else:
    print(resultado)

conexao.commit()
conexao.close()