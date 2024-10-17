## Exercício 3: Decoradores
## Crie um decorador chamado `log_execucao` que registre no console toda vez que uma função
## for chamada e quando terminar sua execução, mostrando o nome da função e o tempo gasto.
from time import perf_counter

def log_execucao(funcao):
    # Implemente o decorador
    def envelope():
        t1 = perf_counter()
        funcao()
        t2 = perf_counter()
        print(f'{funcao.__name__} executada em {t2 - t1:.3e}s')
    return envelope

@log_execucao
def exemplo():
    # Função de exemplo
    return "Função exemplo executada"

# Teste a função decorada
exemplo()

## Desafio: Modifique o decorador para também exibir os argumentos que foram passados para a função.
