speed = float(input('Digite a velocidade:'))
if speed > 80:
    multa = int((speed - 80) * 7)
    print('-*-' * 12)
    print('MULTADO!, o limite da via é 80 Km/h')
    print('O valor da multa é de R$ {},00'.format(multa))
    print('-*-' * 12)
else:
    print('-*-' * 15)
    print('Prossiga você está na velocidade permitida!!!')
    print('-*-' * 15)
