class Motor:
    def __init__(self,cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

    def exibir_dados(self):
        print(f"Motor: {self.cilindrada} cc, {self.potencia} cv")

class Veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    def exibir_dados(self):
        print(f'ano: {self.ano}')
        print(f'preco:{self.preco:.2f}')
        self.motor.exibir_dados()

class Carro(Veiculo):
    def __init__(self, ano, preco, motor,cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Carro: {self.modelo}, Cor: {self.cor}")
        super().exibir_dados()

class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        print(f'Caminhão: Comprimento: {self.comprimento} metros')
        super().exibir_dados()

motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)
carro.exibir_dados()
caminhao.exibir_dados()