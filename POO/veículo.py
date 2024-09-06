class Veiculo:
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
    
    def dirigir(self,km):
        self.quilometragem += km

    def exibir(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Quilometragem {self.quilometragem}')

def main ():
    volvo = Veiculo ('volvo', 'xc60', '2020', 0)
    volvo.exibir()
    volvo.dirigir(5000)
    volvo.exibir()

if __name__ == '__main__':
    main()