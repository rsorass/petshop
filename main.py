import tkinter as tk
import sqlite3
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

contas = []

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

tk.Label(login_page, text="Seja bem-vindo ao nosso petshop! Faça login para continuar!", bg=cor_fundo, fg=cor_texto, font=('Arial', 14, 'bold')).pack(pady=50)
tk.Label(login_page, text="Usuário:", bg=cor_fundo, fg=cor_texto, font=('Arial', 12, 'bold')).pack()
user_entry = tk.Entry(login_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 16))
user_entry.pack(pady=10)
tk.Label(login_page, text="Senha:", bg=cor_fundo, fg=cor_texto, font=('Arial', 12, 'bold')).pack(pady=10)
senha_entry = tk.Entry(login_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 16))
senha_entry.pack(pady=10)



botao_login = tk.Button(login_page, text="Login", bg=cor_botao, fg=cor_texto, font=('Arial', 15, 'bold'))
botao_login.pack(pady=30)

janela.mainloop()