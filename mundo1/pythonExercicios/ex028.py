from random import randint as rd
from time import sleep as slp
# playerName = str(input('Digite seu nome: ')).strip()
# print('Olá {}, vamo jogar um jogo?'.format(playerName))
print('-=-' * 18)
print('Vou pensar em um número, entre 0 e 5, tente adivinhar!')
print('-=-' * 18)
pcNumber = int(rd(0, 5)) #importei o randint da library random como rd, legal essa forma de import
print('Pensando...')
slp(2)
playerNumber = int(input('Me diga o número que pensei: '))
if playerNumber == pcNumber:
    print('VOCÊ ACERTOU!!!! eu pensei no {} e vc respondeu {}'.format(pcNumber, playerNumber))
else:
    print('VC ERROU! TENTE NOVAMENTE!!!'.format(pcNumber))
