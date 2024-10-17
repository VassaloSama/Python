## Exercício 2: Funções como valor de retorno de outras funções
## Implemente uma função chamada `criar_multiplicador` que receba um número `n` e retorne uma função que multiplica
## o argumento de entrada por `n`.
def criar_multiplicador(n):
    # Retorne uma função que multiplique por 'n'
    def multiplica_por_3(x):
        r = n * x 
        return r
    return multiplica_por_3

# Teste a função retornada
multiplica_por_3 = criar_multiplicador(3)
print(multiplica_por_3(10))  # Deve imprimir 30

## Desafio: Crie uma função `criar_calculadora` que retorne diferentes operações matemáticas baseadas em um parâmetro