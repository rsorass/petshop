import tkinter as tk
import sqlite3
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

def listar_contas():
    cursor.execute("""SELECT id, usuario, senha FROM usuarios""")
    contas = cursor.fetchall()
    return contas

cor_fundo = "#00B9B0"
cor_texto = "#FFFFFF"
cor_campos = "#FFFFFF"
cor_texto_campos = "#333333"
cor_botao = "#FF9100"

janela = tk.Tk()
janela.title("Petshop")
janela.geometry("800x600")
janela.config(bg=cor_fundo)

login_page = tk.Frame(janela, bg=cor_fundo)
petshop_page = tk.Frame(janela, bg=cor_fundo)
login_page.pack()

def iniciar_sistema(usuario, usuario_id):
    login_page.pack_forget()
    petshop_page.pack()
    mensagem_boas_vindas = tk.Label(petshop_page, text=f"Olá {usuario}, seja bem vindo ao nosso petshop!", bg=cor_fundo, fg=cor_texto, font=('Arial', 18, 'bold'))
    mensagem_boas_vindas.pack(pady=20)

#TELA DO LOGIN#
tk.Label(login_page, text="Seja bem-vindo ao nosso petshop! Faça login para continuar!", bg=cor_fundo, fg=cor_texto, font=('Arial', 14, 'bold')).pack(pady=50)
tk.Label(login_page, text="Usuário:", bg=cor_fundo, fg=cor_texto, font=('Arial', 12, 'bold')).pack()
user_entry = tk.Entry(login_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 16))
user_entry.pack(pady=10)
tk.Label(login_page, text="Senha:", bg=cor_fundo, fg=cor_texto, font=('Arial', 12, 'bold')).pack(pady=10)
senha_entry = tk.Entry(login_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 16))
senha_entry.pack(pady=10)

login_message = tk.Label(login_page, text="", bg=cor_fundo, fg=cor_texto, font=('Arial', 14, 'bold'))
def login():
    user = user_entry.get()
    senha = senha_entry.get()
    for id_db, user_db, senha_db in listar_contas():
        if user == user_db and senha == senha_db:
            login_message['text'] = "Aceso liberado."
            iniciar_sistema(user, id_db)
            break
    else:
        login_message['text'] = "Acesso negado, credenciais inválidas."
        user_entry.delete(0, tk.END)
        senha_entry.delete(0, tk.END)


botao_login = tk.Button(login_page, text="Login", command=lambda:login(), bg=cor_botao, fg=cor_texto, font=('Arial', 15, 'bold'))
botao_login.pack(pady=30)
login_message.pack()

#TELA DO SISTEMA(AINDA VOU CODAR)#


janela.mainloop()