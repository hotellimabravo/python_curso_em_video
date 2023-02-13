from random import randint as rd
from time import sleep as sl
from operator import itemgetter as itg
jogo = {'jogador1': rd(1, 6),
        'jogador2': rd(1, 6),
        'jogador3': rd(1, 6),
        'jogador4': rd(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sl(0.5)
ranking = sorted(jogo.items(), key=itg(1), reverse=True)
print('-=' * 15)
print(f'{"RANKING":^30}')
print('-=' * 15)
for i, v in enumerate(ranking):
        print(f'O {i+1}º lugar foi: {v[0]} com {v[1]}')
        sl(0.5)
print('-=' * 15)

