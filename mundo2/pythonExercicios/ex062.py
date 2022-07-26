primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('razão para a PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você mostrar a mais?: '))
print('Foram exibidos {} termos da sua PA'.format(total))
