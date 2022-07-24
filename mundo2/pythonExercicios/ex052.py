# Desafio 052

print(' * ' * 10)
print('{:=^30}'.format('NÚMEROS PRIMOS'))
print(' * ' * 10)


n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número \033[32m{}\033[m foi divisível \033[32m{}\033[m vezes.'.format(n, tot))

if tot == 2:
    print('\033[32mNÚMERO PRIMO\033[m')
else:
    print('\033[41mNÃO É UM NÚMERO PRIMO\033[m')
