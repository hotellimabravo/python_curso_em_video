# Desafio 51

print(' * ' * 10)
print('{:=^30}'.format('PROGRESSÃO ARITMÉTICA'))
print(' * ' * 10)
t1 = int(input('Primeiro termo da PA: '))
r = int(input('razão para a PA: '))
decimo = t1 + (10 - 1) * r  # fórmula matemática para encontrar o décimo termo de uma progressão aritmética
for c in range(t1, decimo + r, r):
    print('{}'.format(c), end=' -> ')
print('FIM')
