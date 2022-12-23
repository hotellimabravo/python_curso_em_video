num = []
resp = 'S'

while resp == 'S':
    n = (int(input('Digite um número: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valores repetidos não serão adicionados...')
    resp = str(input('Deseja continuar [S|N]? : ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-' * 35)
print(f'Essa é a lista >>> {sorted(num)} <<<')
print('=-' * 35)
