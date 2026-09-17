class VendasEHistorico():
    def __init__(self, produto, preco, data):
        self.produto = produto
        self.preco = preco
        self.data = data

class Usuario():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self.historico = []
        self.pets = []

    def adicionar_ou_adotar_pet(self, pet, idade):
        self.pets.append(pet)
        Pet(pet, idade)

    def adicionar_compra(self, compra):
        self.historico.append(compra)

class Pet():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Servicos():
    def __init__(self, servico, preco_servico):
        self.servico = servico
        self.preco = preco_servico

joao = Cliente("João")
joao.adicionar_compra("Arranhador")
print(joao.historico)
joao.adicionar_ou_adotar_pet("Anubis", 1)
print(joao.pets)