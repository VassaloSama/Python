class Pessoa:
    def __init__(self, nome, idade, endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço
    
    def alterar(self, endereço):
        self.endereço = endereço
    
    def exibir(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'endereço: {self.endereço}\n')

def main ():
    vassalo = Pessoa('Lucas Vassalo', '25 anos', 'Rua Mendes leal 134')
    cecconi = Pessoa('Gabriel Cecconi', '20 anos', 'Rua dos andrades 652')
    
    vassalo.exibir()
    cecconi.exibir()
    cecconi.alterar('Rua bartolomeu 888')
    cecconi.exibir()

if __name__=='__main__':
    main()

