numeros = []
impares = []
pares = []
while True:
    n = int(input('Digite um número: '))
    if n >= 0:
        numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('~' * 35 )
print(f'Lista completa {numeros}')
print('~' * 35 )
print(f'Pares: {pares}')
print('~' * 35 )
print(f'Impares: {impares}')
print('~' * 35 )
