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

    def adicionar_ou_adotar_pet(self, pet):
        self.pets.append(pet)

    def adicionar_compra(self, compra):
        self.historico.append(compra)

class Pet():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Gato(Pet):
    def __init__(self, nome, idade, cor, raca):
        super().__init__(nome, idade)

        self.cor = cor
        self.raca = raca


class Servicos():
    def __init__(self, servico, preco_servico):
        self.servico = servico
        self.preco = preco_servico

joao = Cliente("João")
joao.adicionar_compra("Arranhador")
pet_joao = Gato("Anubis", 1, "Preto", "SRD")
joao.adicionar_ou_adotar_pet(pet_joao)
print(joao.pets[0].nome)
joao.adicionar_compra("Caixa de areia")
print(joao.historico)