class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar(self, quantidade):
        self.quantidade += quantidade

    def remover(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print('Vai dá não!')

    def show(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.quantidade}')

def main():
     caneta = Produto('Caneta', 5, 100)
     caneta.show()
     caneta.remover(50)
     caneta.show()
     caneta.remover(150)
     caneta.adicionar(200)
     caneta.show()

if __name__ == '__main__':
    main()