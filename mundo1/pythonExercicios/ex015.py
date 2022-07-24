day = int(input('Dias alugado: '))
km = float(input('Km rodados: '))
vDay = day * 60
vKm = km * 0.15
vTotal =vDay + vKm 
print('Foram rodados {} km, durante {} dias, o valor a ser pago é: R$ {:.2f}'.format(km, day, vTotal))
