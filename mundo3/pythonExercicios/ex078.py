numeros = []
maior = 0
menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {n}: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print('=-' * 30)
print(f'Você digitou os valores {numeros}')
print(f'O maior número digitado foi {maior}. Ele aparece nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {menor}. Ele aparece nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
print()
