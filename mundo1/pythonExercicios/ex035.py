print('\033[0;31m-=-\033[m' * 10)
print('\033[1;30;46m** ANALISADOR DE TRIÂNGULOS **\033[m')
print('\033[0;31m-=-\033[m' * 10)
r1 = float(input('\033[1;36mSegmento 1: \033[m'))
r2 = float(input('\033[1;35mSegmento 2: \033[m'))
r3 = float(input('\033[1;34mSegmento 3: \033[m'))

if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r1 + r2:
    print('\033[0;31m-=-\033[m' * 14)
    print('\033[30;47mOs segmentos \033[32;47mPODEM\033[30;47m formar um triângulo!\033[m')
    print('\033[0;31m-=-\033[m' * 14)
else:
    print('\033[0;31m-=-\033[m' * 14)
    print('\033[31;43mOs segmentos NÃO PODEM formar um triângulo!\033[m')
    print('\033[0;31m-=-\033[m' * 14)
