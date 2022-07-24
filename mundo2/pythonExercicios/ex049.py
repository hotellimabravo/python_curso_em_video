# Desafio 49

print(' * ' * 10)
print('{:=^30}'.format('TABUADA'))
print(' * ' * 10)
n = int(input('Qual tabuada?: '))

for c in range(1, 10+1):
    z = n * c
    print('{} x {} = {}'.format(n, c, z))
