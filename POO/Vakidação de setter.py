class Pessoa:
    def __init__(self, nome, idade):
        self.__idade = 0
        self.set_idade(idade)
        self.nome = nome

    def set_idade (self, anos):
        if anos >= 0:
            self.__idade += anos
        else:
            print('não é possivel ter idade negativa')

    def get_idade (self):
        return self.__idade
            
Lucas = Pessoa('Lucas', -5)
print(Lucas.get_idade())
Lucas = Pessoa('Lucas', 25)
print(Lucas.get_idade())
Lucas = Pessoa('Lucas', -16)
print(Lucas.get_idade())
