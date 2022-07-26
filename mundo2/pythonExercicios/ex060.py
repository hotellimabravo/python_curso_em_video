from math import factorial as ft
n = int(input('Digite um número: '))
c = n
f = ft(n)
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))




