class ContaBancaria:
    def __init__(self, saldo , titular):
        self.__saldo = 0
        self.depositar(saldo)
        self.titular = titular
    
    def depositar (self, valor):
        if valor >= 0:
            self.__saldo += valor
        else:
            print('O valor para deposito deve ser positivo')

    def exibir(self):
        return self.__saldo

conta1 = ContaBancaria(1000, 'Lucas Vassalo')
print(conta1.exibir())
conta1.depositar(10)
print(f'seu saldo é: {conta1.exibir()}')
conta1.depositar(-10)

