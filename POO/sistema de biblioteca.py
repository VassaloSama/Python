class Livro:
    def __init__ (self, titulo, autor, ano, disp):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disp = disp

    def emprestar(self):
        if self.disp == 'disponivel':
            self.disp = 'indisponivel'
            print('O livro foi emprestado com Sucesso!\n')
        else:
            print('Sem livros disponivel\n')

    def devolver(self):
        if self.disp == 'indisponivel':
            self.disp = 'disponivel'
            print('O livro foi devolvido com Sucesso!\n')
        else:
            print('O livro já estáva disponível\n')

    def show(self):
        print(f'{self.titulo}, {self.autor}, {self.ano}, {self.disp}\n')

def main():
    crepusculo = Livro('Anoitecer', 'Jorge', 2012, 'disponivel')
    culpa = Livro('A culda das estrelas', 'Elaine', 2010, 'indisponivel')

    crepusculo.show()
    culpa.show()
    culpa.emprestar()
    culpa.devolver()
    culpa.emprestar()
    crepusculo.devolver()
    crepusculo.emprestar()
    crepusculo.devolver()
    crepusculo.show()
    culpa.show()


if __name__ == '__main__':
    main()