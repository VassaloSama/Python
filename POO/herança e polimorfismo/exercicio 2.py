class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print(f'nome: {self.nome} cor: {self.cor} numero de patas {self.numero_patas}')

class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raça = raca

    def exibir_dados(self):
        print(f'nome: {self.nome} cor: {self.cor} numero de patas {self.numero_patas}')

animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados() # exibe os atributos do animal
dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados() # exibe os atributos do cachorro