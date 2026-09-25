import tkinter as tk
from tkinter import ttk
from datactrl import listar_contas, listar_pets, buscar_produtos, carregar_imagem_url, cadastrar_pet_banco, fechar_banco

def criar_page_com_scroll(parent_frame):
    aba_frame = tk.Frame(parent_frame, bg=cor_fundo)
    canvas = tk.Canvas(aba_frame, bg=cor_fundo, highlightthickness=0, width=1235, height=700)
    scrollbar = ttk.Scrollbar(aba_frame, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    frame_conteudo = tk.Frame(canvas, bg=cor_fundo)

    canvas_window = canvas.create_window((0, 0), window=frame_conteudo, anchor='nw')

    canvas.bind('<Configure>', lambda event:canvas.itemconfig(canvas_window, width=event.width))

    frame_conteudo.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox('all')))

    return aba_frame, frame_conteudo


cor_fundo = "#00B9B0"
cor_texto = "#FFFFFF"
cor_campos = "#FFFFFF"
cor_texto_campos = "#333333"
cor_botao = "#FF9100"
cor_barra = "#DF7E00"

janela = tk.Tk()
janela.title("Petshop")
janela.geometry("1250x700")
janela.config(bg=cor_fundo)

login_page = tk.Frame(janela, bg=cor_fundo)
petshop_page = tk.Frame(janela, bg=cor_fundo)
login_page.pack(fill="both", expand=True)

pets_page = tk.Frame(petshop_page, bg=cor_fundo)
aba_scroll_pets, sub_pets = criar_page_com_scroll(pets_page)
aba_scroll_pets.pack(fill='both', expand=True)

comidas_page = tk.Frame(petshop_page, bg=cor_fundo)
aba_scroll_comidas, sub_comidas = criar_page_com_scroll(comidas_page)
aba_scroll_comidas.pack(fill='both', expand=True)

brinquedos_page = tk.Frame(petshop_page, bg=cor_fundo)
aba_scroll_brinquedos, sub_brinquedos = criar_page_com_scroll(brinquedos_page)
aba_scroll_brinquedos.pack(fill='both', expand=True)

casinhas_page = tk.Frame(petshop_page, bg=cor_fundo)
aba_scroll_casinhas, sub_casinhas = criar_page_com_scroll(casinhas_page)
aba_scroll_casinhas.pack(fill='both', expand=True)

utilitarios_page = tk.Frame(petshop_page, bg=cor_fundo)
aba_scroll_utilitarios, sub_utilitarios = criar_page_com_scroll(utilitarios_page)
aba_scroll_utilitarios.pack(fill='both', expand=True)

sistema_page = tk.Frame(petshop_page, bg=cor_fundo)
aba_scroll_sistema, sub_sistema = criar_page_com_scroll(sistema_page)
aba_scroll_sistema.pack(fill='both', expand=True)

cadastro_pets_page = tk.Frame(petshop_page, bg=cor_fundo)
aba_scroll_cadastro_pets, sub_cadastro_pets = criar_page_com_scroll(cadastro_pets_page)
aba_scroll_cadastro_pets.pack(fill='both', expand=True)

def pet_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    cadastro_pets_page.pack_forget()
    pets_page.pack(expand=True, fill='both')
def comida_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    cadastro_pets_page.pack_forget()
    comidas_page.pack(expand=True, fill='both')
def casas_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    cadastro_pets_page.pack_forget()
    casinhas_page.pack(expand=True, fill='both')
def brinquedo_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    cadastro_pets_page.pack_forget()
    brinquedos_page.pack(expand=True, fill='both')
def utilitario_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    cadastro_pets_page.pack_forget()
    utilitarios_page.pack(expand=True, fill='both')
def cadastro_pet_page():
    pets_page.pack_forget()
    comidas_page.pack_forget()
    brinquedos_page.pack_forget()
    casinhas_page.pack_forget()
    utilitarios_page.pack_forget()
    cadastro_pets_page.pack(expand=True, fill='both')

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
#BOTÕES INFERIORES#
barra_inferior = tk.Frame(petshop_page, bg=cor_barra)
barra_inferior.pack(pady=15, side='bottom', fill='x')

botao_cadastrar_pets = tk.Button(barra_inferior, command=lambda:cadastro_pet_page(), text="Cadastre seu Pet aqui!", bg=cor_botao, fg=cor_texto, font=('Arial', 10, 'bold'))
botao_cadastrar_pets.pack(side='left', fill='both', expand=True)
#FIM#

pet_cadastro_label = tk.Label(sub_cadastro_pets, text="", bg=cor_fundo, fg=cor_texto, font=('Arial', 12, 'bold'))

def iniciar_sistema(usuario, usuario_id):
    login_page.pack_forget()
    petshop_page.pack(fill="both", expand=True)
    pets_page.pack(expand=True, fill='both')
    sub_pets.pack(fill='both', expand=True)
    mensagem_boas_vindas = tk.Label(sistema_page, text=f"Olá {usuario}, seja bem vindo ao nosso petshop!", bg=cor_fundo, fg=cor_texto, font=('Arial', 16, 'bold'))
    mensagem_boas_vindas.pack(pady=20)
    mensagem_boas_vindas_2 = tk.Label(sistema_page, text="Escolha uma aba para continuar!", bg=cor_fundo, fg=cor_texto, font=('Arial', 16, 'bold'))
    mensagem_boas_vindas_2.pack()

    meus_pets = listar_pets(usuario_id)

    meus_pets_label = tk.Label(pets_page, text="Meus Pets", bg=cor_fundo, fg=cor_texto, font=('Arial', 16, 'bold'))
    meus_pets_label.pack()

    tabela_pets = ttk.Treeview(sub_pets, columns=("nome", "idade"), show="headings")
    tabela_pets.heading("nome", text="Nome do Pet")
    tabela_pets.heading("idade", text="Idade do Pet em Meses")

    tabela_pets.column("nome", width=300, anchor="center")
    tabela_pets.column("idade", width=200, anchor="center")

    tabela_pets.pack()

    tk.Label(sub_cadastro_pets, text="Digite o nome do seu pet(Não é necessário caso seu(s) pet(s) já está/estejam cadastrado(s)):", bg=cor_fundo, fg=cor_texto, font=('Arial', 14, 'bold')).pack()
    pet_nome_entry = tk.Entry(sub_cadastro_pets, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 16, 'bold'))
    pet_nome_entry.pack(pady=15)
    tk.Label(sub_cadastro_pets, text="Idade do animal(Digite a idade em meses):", bg=cor_fundo, fg=cor_texto, font=('Arial', 16, 'bold')).pack()
    idade_pet_entry = tk.Entry(sub_cadastro_pets, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 16, 'bold'))
    idade_pet_entry.pack(pady=15)

    def salvar_pet():
        pet_cadastro_label.pack()
        pet_nome = pet_nome_entry.get()
        pet_idade = idade_pet_entry.get()

        if pet_nome.replace(" ", "").isalpha() and pet_idade.isdigit():
            sucesso = cadastrar_pet_banco(pet_nome, pet_idade, usuario_id)

            if sucesso:
                pet_cadastro_label['text'] = "Pet cadastrado com sucesso!"

                tabela_pets.insert("", "end", values=(pet_nome, pet_idade))
            else:
                pet_cadastro_label['text'] = "Houve um erro na hora de salvar no banco de dados."
        else:
            pet_cadastro_label['text'] = "Houve um erro na hora de cadastrar. Use apenas letras para o nome e números para a idade."

    for pet in meus_pets:
        tabela_pets.insert("", "end", values=(pet[0], pet[1]))

    botao_add_pet = tk.Button(sub_cadastro_pets, text="Adicionar pet aos seus pets", command=salvar_pet, bg=cor_botao, fg=cor_texto, font=('Arial', 16, 'bold'))
    botao_add_pet.pack(pady=15)
    return meus_pets

#TELA DO LOGIN#
tk.Label(login_page, text="Seja bem-vindo ao nosso petshop! Faça login para continuar!", bg=cor_fundo, fg=cor_texto, font=('Arial', 18, 'bold')).pack(pady=50)
tk.Label(login_page, text="Usuário:", bg=cor_fundo, fg=cor_texto, font=('Arial', 14, 'bold')).pack()
user_entry = tk.Entry(login_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 18))
user_entry.pack(pady=10)
tk.Label(login_page, text="Senha:", bg=cor_fundo, fg=cor_texto, font=('Arial', 14, 'bold')).pack(pady=10)
senha_entry = tk.Entry(login_page, bg=cor_campos, fg=cor_texto_campos, font=('Arial', 18))
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

botao_login = tk.Button(login_page, text="Login", command=lambda:login(), bg=cor_botao, fg=cor_texto, font=('Arial', 18, 'bold'))
botao_login.pack(pady=30)
login_message.pack()

janela.mainloop()