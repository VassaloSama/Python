class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.verificar_idade(idade)
    
    def verificar_idade(self, value):
        while value < 18:
            value = int(input('você precisa ter mais de 18 anos'))
        self.idade = value


