class Pessoa:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome

class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome,CNPJ):
        super().__init__(identificador, nome)
        self.CNPJ = CNPJ

class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome,RG,CPF):
        super().__init__(identificador, nome)
        self.RG = RG
        self.CPF = CPF

pessoa1 = Pessoa(1, "Nome da Pessoa")
p_juridica = PessoaJuridica(2, "Nome da Pessoa Juridica", "1111111111")
p_fisica = PessoaFisica(3, "Nome da Pessoa Fisica", "222222222", "333333333")
print(pessoa1.identificador)
print(pessoa1.nome)
print(p_juridica.identificador)
print(p_juridica.nome)
print(p_juridica.CNPJ)
print(p_fisica.identificador)
print(p_fisica.nome)
print(p_fisica.RG)
print(p_fisica.CPF) 