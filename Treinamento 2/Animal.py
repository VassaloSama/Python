A = input()
B = input()
C = input()

if A == 'vertebrado':
    if B == 'ave':
        if C == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if B == 'mamifero':
            if C == 'onivoro':
                print('homem')
            else:
                print('vaca')
else:
    if B == 'inseto':
        if C == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if B == 'anelideo':
            if C == 'hematofago':
                print('sanguessuga')
            else:
                print('minhoca')