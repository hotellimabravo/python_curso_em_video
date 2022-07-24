from math import sin, cos, tan, radians
print('=' * 30)
f = 'Seno, Cosseno e Tangente'
print('{:^30}'.format(f))
print('=' * 30)
ang = radians(float(input('Digite o angulo: ')))
# *** Radians converte o valor em radianos ***
sen = sin(ang)
cos = cos(ang)
tan = tan(ang)
print('** Seno = {:.2f} **'.format(sen))
print('** Cosseno = {:.2f} **'.format(cos))
print('** Tangente = {:.2f} **'.format(tan))
