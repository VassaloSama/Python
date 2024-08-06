salario = float(input(digite o salario))

if salario < 280:
    aumento = salario * 0.2
    salario_reajustado = salario + aumento
    porcentagem = "20%"
    print(salario)
    print(porcentagem)
    print(aumento)
    print(salario_reajustado)
elif salario < 700:
    aumento = salario * 0.15
    salario_reajustado = salario + aumento
    porcentagem = "15%"
    print(salario)
    print(porcentagem)
    print(aumento)
    print(salario_reajustado)
elif salario < 1500:
    aumento = salario * 0.1
    salario_reajustado = salario + aumento
    porcentagem = "10%"
    print(salario)
    print(porcentagem)
    print(aumento)
    print(salario_reajustado)
else:
    aumento = salario * 0.05
    salario_reajustado = salario + aumento
    porcentagem = "5%"
    print(salario)
    print(porcentagem)
    print(aumento)
    print(salario_reajustado)

    

    