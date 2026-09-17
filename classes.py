class VendasEHistorico():
    def __init__(self, cliente: "Cliente", pet: "Pet", servico, data):
        self.cliente = cliente
        self.pet = pet
        self.servico = servico
        self.data = data
        self.valor_total = servico.preco

        self.cliente.adicionar_compra(self)

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

    
    def miar(self):
        print(f"{self.nome}: Meow!")

class Cachorro(Pet):
    def __init__(self, nome, idade, cor, raca):
        super().__init__(nome, idade)

        self.cor = cor
        self.raca = raca

    def latir(self):
        print(f"{self.nome}: Woof!")

class Servicos():
    def __init__(self, servico, preco_servico):
        self.servico = servico
        self.preco = preco_servico

joao = Cliente("João")
banho = Servicos("Banho Completo", 50.00)
pet_joao = Gato("Anubis", 1, "Preto", "SRD")
joao.adicionar_ou_adotar_pet(pet_joao)
print("Pet(s):")
for pet in joao.pets:
    print(pet.nome)
print(f"Serviço: {banho.servico} | Preço: {banho.preco}")
nova_venda = VendasEHistorico(joao, pet_joao, banho, "17/09/2026")
print(f"O cliente {nova_venda.cliente.nome} comprou {nova_venda.servico.servico} para seu pet {nova_venda.pet.nome} no dia {nova_venda.data}")
print(f"Valor a pagar: R${nova_venda.valor_total}")
pet_joao.miar()
print(joao.historico[0].servico.servico)