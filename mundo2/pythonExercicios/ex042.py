print('\033[0;31m-=-\033[m' * 10)
print('\033[1;30;46m** ANALISADOR DE TRIÂNGULOS **\033[m')
print('\033[0;31m-=-\033[m' * 10)
r1 = float(input('\033[1;36mSegmento 1: \033[m'))
r2 = float(input('\033[1;35mSegmento 2: \033[m'))
r3 = float(input('\033[1;34mSegmento 3: \033[m'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;31m-=-\033[m' * 18)
    print('Os segmentos PODEM formar um triângulo! ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
    print('\033[0;31m-=-\033[m' * 18)
else:
    print('\033[0;31m-=-\033[m' * 14)
    print('Os segmentos NÃO PODEM formar um triângulo!')
    print('\033[0;31m-=-\033[m' * 14)

