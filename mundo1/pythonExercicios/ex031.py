from time import sleep as slp

distancia = float(input('Olá, informe a distância da viagem: '))
print('Calculando...')
slp(3)
if distancia > 200:
    vlrViagem = distancia * 0.45
else:
    vlrViagem = distancia * 0.50
print('O valor da passagem é: R$ {:.2f}'.format(vlrViagem))
