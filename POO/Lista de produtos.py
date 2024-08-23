produtos = {}

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço de {nome}: R$ "))
    produtos[nome] = preco


for nome in produtos:
    if produtos[nome] > 50.00:
        print(f"{nome}: R$ {produtos[nome]:.2f}")