N = float(input())

if N >= 0 and N <= 25.0000:
    print('Intervalo [0,25]')

if N > 25.0000 and N <= 50.0000000:
    print('Intervalo (25,50]')

if N > 50.0000000 and N <= 75.0000000000:
    print('Intervalo (50,75]')

if N > 75.0000000000 and N <= 100.0000000000000:
    print('Intervalo (75,100]')
    
if N < 0 or N > 100.0000000000000000:
    print('Fora de intervalo')