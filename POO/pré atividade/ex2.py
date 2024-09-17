class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.verificar_idade(idade)
    
    def verificar_idade(self, value):
        while value < 18:
            print(f' Funcionario {self.nome} tem idade inferior a 18 anos')
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

class Departamento:
    def __init__ (self, nome):
        self.nome = nome
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def calcular_total_salarios(self):
        if len(self.funcionarios) > 0:
            total = 0
            for funcionario in self.funcionarios:
                total += funcionario.calcular_salario_anual()
            return total
        else:
            print('Departamento sem funcionários')
    
    def listar_funcionarios(self):
        if len(self.funcionarios) > 0:
            print(f'Funcionários:')
            for funcionario in self.funcionarios:
                print(f'Nome: {funcionario.nome}, salario anual de R$ {funcionario.calcular_salario_anual()}')
        else:
            print('Não possui nenhum funcionario')
     

Marcio= Funcionario('Marcio', 30, 6000)
Alex= Funcionario('Alex', 40, 10000)
Lucas= Funcionario('Lucas', 17,4000)

TI = Departamento('Tecnologia da Informação')

TI.adicionar_funcionario(Marcio)
TI.adicionar_funcionario(Alex)
TI.adicionar_funcionario(Lucas)
TI.listar_funcionarios()
print(TI.calcular_total_salarios())

