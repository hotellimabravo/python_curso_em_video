from random import randint as rd
from time import sleep as sl
jogo = []
j = []
num = 0
frase = '***** BOA SORTE!!! *****'
frase1 = '***** MEGA SENA *****'
print('-=' * 20)
print(f'{frase1:^40}')
print('-=' * 20)
qtd_jogos = int(input('Quantos jogos quer sortear? '))
while True:
    print(f'Sorteando {qtd_jogos} jogos... ')
    for q in range(0, qtd_jogos):
        for c in range(1, 7):
            num = rd(1, 60)
            if num not in j:
                j.append(num)
            else:
                num = rd(1, 60)
                j.append(num)
                sl(1)
        j.sort()
        jogo.append(j[:])
        j.clear()
        print(f'Jogo {q+1}: {jogo[q]}')
        sl(0.5)
    print('-=' * 20)
    print(f'{frase:^40}')
    print('-=' * 20)
    break
