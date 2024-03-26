n1,n2,n3,n4 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

peso = (n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)
media = peso / 10
print(f'Media: {media:.1f}')

if media >= 5 and media < 7:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    mf = (media + exame) / 2
    
    if mf >=5:
        print('Aluno aprovado.')
        print(f'Media final: {mf:.1f}')
            
    else :
        print('Aluno reprovado.')
        print(f'Media final: {mf:.1f}')

else :
    if media >= 7:
        print('Aluno aprovado.')

    else:
        print('Aluno reprovado.')