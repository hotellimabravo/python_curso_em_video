contador = tot = totMil = barato = caro = 0
cheapName = ''
while True:
    print('*' * 30)
    print('{:^30}'.format('CADASTRO DE COMPRAS'))
    print('*' * 30)
    contador += 1
    print(f'Produto: {contador}')
    pdpName = str(input('Nome do produto: ')).strip().upper()
    pdpPrice = float(input('Valor do Produto: R$'))
    answer = ' '
    while answer not in 'SN':
        answer = str(input('Deseja cadastrar outro produto? [Sim/Não]: ')).strip().upper()[0]
    tot = tot + pdpPrice
    if contador == 1 or pdpPrice < barato:
        barato = pdpPrice
        cheapName = pdpName
    if pdpPrice > 1000:
        totMil += 1
    if answer == 'N':
        break
print('*' * 30)
print('{:^30}'.format('PROGRAMA FINALIZADO!'))
print('*' * 30)
print(f'Total Gasto: R${tot}')
print(f'Na sua compra {totMil} produtos custam mais de Mil Reais')
print(f'O produto mais barato da sua compra é: {cheapName} que custa R${barato}')
