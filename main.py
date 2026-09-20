import tkinter as tk
from tkinter import ttk
import time
import sqlite3
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

def listar_contas():
    cursor.execute("""SELECT id, usuario, senha FROM usuarios""")
    contas = cursor.fetchall()
    return contas

def listar_pets(dono_id):
    cursor.execute("""SELECT nome, idade_meses FROM pets WHERE dono_id = ?""", (dono_id,))
    return cursor.fetchall()

cor_fundo = "#00B9B0"
cor_texto = "#FFFFFF"
cor_campos = "#FFFFFF"
cor_texto_campos = "#333333"
cor_botao = "#FF9100"
cor_barra = "#DF7E00"

janela = tk.Tk()
janela.title("Petshop")
janela.geometry("900x700")
janela.config(bg=cor_fundo)

login_page = tk.Frame(janela, bg=cor_fundo)
petshop_page = tk.Frame(janela, bg=cor_fundo)
login_page.pack(fill="both", expand=True)

pets_page = tk.Frame(petshop_page, bg=cor_fundo)
comidas_page = tk.Frame(petshop_page, bg=cor_fundo)
brinquedos_page = tk.Frame(petshop_page, bg=cor_fundo)
casinhas_page = tk.Frame(petshop_page, bg=cor_fundo)
utilitarios_page = tk.Frame(petshop_page, bg=cor_fundo)
sistema_page = tk.Frame(petshop_page, bg=cor_fundo)

def pet_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    pets_page.pack()
def comida_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    comidas_page.pack()
def casas_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    casinhas_page.pack()
def brinquedo_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    brinquedos_page.pack()
def utilitario_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    utilitarios_page.pack()

#BARRA DO MENU DO SISTEMA#
barra_menu = tk.Frame(petshop_page, bg=cor_barra)
barra_menu.pack(pady=15, side='top', fill='x')

botao_pets_page = tk.Button(barra_menu, text='Meus Pets', command=lambda:pet_page(), bg=cor_botao, fg=cor_texto, font=('Arial', 10, 'bold'))
botao_pets_page.pack(side='left', fill='both', expand=True)
botao_comida_page = tk.Button(barra_menu, text='Comidas', command=lambda:comida_page(), bg=cor_botao, fg=cor_texto, font=('Arial', 10, 'bold'))
botao_comida_page.pack(side='left', fill='both', expand=True)
botao_casinhas_page = tk.Button(barra_menu, text='Casinhas', command=lambda:casas_page(), bg=cor_botao, fg=cor_texto, font=('Arial', 10, 'bold'))
botao_casinhas_page.pack(side='left', fill='both', expand=True)
botao_brinquedos_page = tk.Button(barra_menu, text='Brinquedos', command=lambda:brinquedo_page(), bg=cor_botao, fg=cor_texto, font=('Arial', 10, 'bold'))
botao_brinquedos_page.pack(side='left', fill='both', expand=True)
botao_utilitarios_page = tk.Button(barra_menu, text='Utilitários(Guias, etc)', command=lambda:utilitario_page(), bg=cor_botao, fg=cor_texto, font=('Arial', 10, 'bold'))
botao_utilitarios_page.pack(side='left', fill='both', expand=True)
#FIM#

pet_cadastro_label = tk.Label(pets_page, text="", bg=cor_fundo, fg=cor_texto, font=('Arial', 12, 'bold'))

def iniciar_sistema(usuario, usuario_id):
    login_page.pack_forget()
    petshop_page.pack(fill="both", expand=True)
    mensagem_boas_vindas = tk.Label(sistema_page, text=f"Olá {usuario}, seja bem vindo ao nosso petshop!", bg=cor_fundo, fg=cor_texto, font=('Arial', 16, 'bold'))
    mensagem_boas_vindas.pack(pady=20)

    meus_pets = listar_pets(usuario_id)

    tabela_pets = ttk.Treeview(pets_page, columns=("nome", "idade"), show="headings")
    tabela_pets.heading("nome", text="Nome do Pet")
    tabela_pets.heading("idade", text="Idade do Pet")

    tabela_pets.column("nome", width=200, anchor="center")
    tabela_pets.column("idade", width=100, anchor="center")

    tabela_pets.pack(pady=20)

    tk.Label(pets_page, text="Digite o nome do seu pet(Não é necessário caso seu(s) pet(s) já está/estejam cadastrado(s)):", bg=cor_fundo, fg=cor_texto, font=('Arial', 14, 'bold')).pack()
    pet_nome_entry = tk.Entry(pets_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 14, 'bold'))
    pet_nome_entry.pack(pady=15)
    tk.Label(pets_page, text="Idade do animal(Digite a idade em meses):", bg=cor_fundo, fg=cor_texto, font=('Arial', 16, 'bold')).pack()
    idade_pet_entry = tk.Entry(pets_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 16, 'bold'))
    idade_pet_entry.pack(pady=15)

    pet_nome = pet_nome_entry.get()
    idade_pet = idade_pet_entry.get()

    for pet in meus_pets:
        tabela_pets.insert("", "end", values=(pet[0], pet[1]))

    def salvar_pet():
        pet_cadastro_label.pack()

        if pet_nome.replace(" ", "").isalpha() and idade_pet.isdigit():
            cursor.execute("""INSERT INTO pets
                        (nome, idade_meses, dono_id) VALUES
                        (?, ?, ?)""", (pet_nome, idade_pet, usuario_id))
            conexao.commit()
            pet_cadastro_label['text'] = "Pet cadastrado com sucesso!"
        else:
            pet_cadastro_label['text'] = "Houve um erro na hora de cadastrar seu pet, digite apenas letras para o nome e números para a idade."

    botao_add_pet = tk.Button(pets_page, text="Adicionar pet aos seus pets", command=salvar_pet, bg=cor_botao, fg=cor_texto, font=('Arial', 16, 'bold'))
    botao_add_pet.pack(pady=15)
    return meus_pets

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

janela.mainloop()