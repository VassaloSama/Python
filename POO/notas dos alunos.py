alunos = {}

for i in range(5):
    ra = int(input("informe o RA do aluno: "))
    notas = []
    for x in range(3):
        nota = float(input(f"digite a nota {x+1} do aluno {ra}"))
        notas.append(nota)
    alunos[ra] = notas

for ra in alunos:
    notas = alunos[ra]
    total = 0
    for nota in notas:
        total += nota
    media = total / len(notas)
    print(f"RA: {ra} - Média: {media:.2f}")