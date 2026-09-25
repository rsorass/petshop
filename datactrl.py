import sqlite3
import io
import requests
from PIL import Image, ImageTk
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


cursor.execute("""CREATE TABLE IF NOT EXISTS table_comidas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                imagem_url TEXT,
                tabela_origem TEXT NOT NULL,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS table_brinquedos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                imagem_url TEXT,
                tabela_origem TEXT NOT NULL,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS table_casinhas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                imagem_url TEXT,
                tabela_origem TEXT NOT NULL,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS table_utilitarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                imagem_url TEXT,
                tabela_origem TEXT NOT NULL,
                preço FLOAT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS table_serviços (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                imagem_url TEXT,
                preço FLOAT NOT NULL,
                tabela_origem TEXT NOT NULL,
                data TEXT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS table_historico (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                imagem_url TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                valor_total FLOAT NOT NULL,
                tabela_origem TEXT NOT NULL,
                data TEXT NOT NULL,


                cliente_id INTEGER,
                FOREIGN KEY (cliente_id) REFERENCES usuarios(id)
)""")

def carregar_imagem_url(url):
    try:

        if url and "://pinimg.com" in url:
            if "/originals/" in url: url = url.replace("/originals/", "/236x/")
            elif "/736x/" in url: url = url.replace("/736x/", "/236x/")
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        with io.BytesIO(resposta.content) as arquivo_virtual:
            with Image.open(arquivo_virtual) as imagem_pil:
                imagem_redimensionada = imagem_pil.resize((150, 150), Image.Resampling.LANCZOS)
                imagem_final = ImageTk.PhotoImage(imagem_redimensionada)
                imagem_final.image = imagem_final
                return imagem_final

    except Exception as erro:
        print(f"Erro ao carregar imagem: {erro}")
        return None

# tabelas_para_deletar = ['comidas', 'brinquedos', 'serviços', 'casinhas', 'utilitarios', 'historico']
# for tabela in tabelas_para_deletar:
#      comando = f"""DROP TABLE IF EXISTS {tabela}"""
#      cursor.execute(comando)
#      print(f"Tabela {tabela} deletada(se existia).")

def buscar_produtos(nome_pesquisado):
    query = """
    SELECT id, nome, imagem_url, tabela_origem, preço FROM comidas WHERE nome LIKE ? UNION ALL
    SELECT id, nome, imagem_url, tabela_origem, preço FROM brinquedos WHERE nome LIKE ? UNION ALL
    SELECT id, nome, imagem_url, tabela_origem, preço FROM casinhas WHERE nome LIKE ? UNION ALL
    SELECT id, nome, imagem_url, tabela_origem, preço FROM utilitarios WHERE nome LIKE ?
    """

    termo = f"%{nome_pesquisado}%"

    cursor.execute(query, (termo, termo, termo, termo))
    resultados = cursor.fetchall()

    produtos_formatados = []
    for linha in resultados:
        id_prod, nome, url_imagem, tabela, preco = linha
        imagem_tkinter = carregar_imagem_url(url_imagem)

        produtos_formatados.append({
            "id": id_prod,
            "nome": nome,
            "preco": preco,
            "tabela": tabela,
            "foto": imagem_tkinter
        })

    return produtos_formatados

def fechar_banco():
    """FUNÇÃO PARA SER USADA NO BANCO !APENAS! QUANDO O USUÁRIO FECHAR O SISTEMA"""
    conexao.close()
try:
     cursor.execute("""
                 INSERT INTO table_comidas
                 (nome, imagem_url, tabela_origem, preço) VALUES
                 ("Ração para Cachorros Filhotes", "https://i.pinimg.com/1200x/cc/5d/27/cc5d2725c40cba7afc4c768a19488452.jpg?w=300", "comidas", 89.90)
                 """)
     conexao.commit()
     print("Suceso ao inserir dados ao data base!")
except Exception as erro:
     print(f"\nHouve um erro ao inserir algo no banco de dados: {erro}\n")

def listar_contas():
    cursor.execute("""SELECT id, usuario, senha FROM usuarios""")
    contas = cursor.fetchall()
    return contas

def listar_pets(dono_id):
    cursor.execute("""SELECT nome, idade_meses FROM pets WHERE dono_id = ?""", (dono_id,))
    return cursor.fetchall()

def cadastrar_pet_banco(nome, idade, dono_id):
    try:
        cursor.execute("""INSERT INTO pets
                        (nome, idade_meses, dono_id) VALUES
                        (?, ?, ?)""", (nome, idade, dono_id))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro no banco: {e}")
        return False

user_procurado = None
cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (user_procurado,))
resultado = cursor.fetchone()
if resultado == None:
    print(f"O usuário {user_procurado} não existe, por favor, insira valores válidos.")
else:
    print(resultado)

conexao.commit()