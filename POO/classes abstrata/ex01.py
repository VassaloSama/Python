## Exercício 1: Funções como argumentos para outras funções
## Implemente uma função chamada `executar_operacao` que receba uma função de operação matemática e dois números.
## A função deve executar a operação matemática nos dois números fornecidos.
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def executar_operacao(funcao, x, y):
    operacao = funcao(x, y)
    return operacao

##Teste a função 'executar_operacao' passando as funções 'somar' e 'subtrair'

print(executar_operacao(somar, 5, 5))
print(executar_operacao(subtrair, 5, 5))
print(executar_operacao(multiplicar, 5, 5))
print(executar_operacao(dividir, 5, 5))

##Desafio: Adicione mais operações, como multiplicação e divisão.

