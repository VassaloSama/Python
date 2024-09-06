class Lampada:
    def __init__(self, estado):
        self.__estado = None
        self.set_estado(estado)

    def set_estado (self, value):
        if value == 'ligado' or 'desligado':
            self.__estado = value
        else:
            print('Valor do estado invalido')

    def get_estado (self):
        return self.__estado

quarto = Lampada ('teste')
print(quarto.get_estado())
quarto.set_estado ('desli')
print(quarto.get_estado())