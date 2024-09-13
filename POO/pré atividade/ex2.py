class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.verificar_idade(idade)
    
    def verificar_idade(self, value):
        while value < 18:
            print('Idade inferior a 18 anos')
            value = int(input('Informe a idade:'))
        self.idade = value

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.__salario = salario 

    def get_salario(self):
        return self.__salario
    
    def set_salario(self, value):
        if value > 0:
            self.__salario = value
        else:
            print('O valor precisa ser maior que 0')
    
    def calcular_salario_anual(self):
        return self.__salario * 12
     
Lucas = Funcionario ('Lucas',5,200)