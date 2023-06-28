#  função que calcula area de um terreno
def cabeçalho(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)


def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg}x{comp} é de {a}m²')


#  programa principal
while True:
    cabeçalho(f'{"Calcule a Área":^30}')
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    área(l, c)
    resp = input('Continuar? [S/N]: ').upper()[0]
    if resp in 'Nn':
        break
cabeçalho(f'{"Volte Sempre!":^30}')
