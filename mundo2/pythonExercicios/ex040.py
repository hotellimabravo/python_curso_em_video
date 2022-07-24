n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2

print('Média = {}'.format(media))

if media >= 7:
    print('APROVADO!')
elif media >= 5 and media < 7:  # if 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO!!!!!')
