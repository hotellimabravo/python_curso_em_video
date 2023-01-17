valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescenete são {valores}')
if 5 in valores:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')
