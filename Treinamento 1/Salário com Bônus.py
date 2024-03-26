vendedor = input ()
salario = float (input())
vendas = float (input())
comisao = (vendas * 0.15)
total = comisao + salario

print (f'TOTAL = R$ {total:.2f}')