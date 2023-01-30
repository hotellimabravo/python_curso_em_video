# 7 valores numericos e cadastrar em uma lista única
numeros = [[], []]
for c in range(1, 8):
    numero = int(input(f'{c}- Digite um número: '))
    if numero % 2 == 1:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(f'Valores pares: {sorted(numeros[1])}')
print(f'Valores ímpares: {sorted(numeros[0])}')
