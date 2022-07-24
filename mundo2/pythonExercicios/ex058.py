from random import randint as rd
from time import sleep as slp

print('-=-' * 18)
print('Vou pensar em um número, entre 1 e 10, tente adivinhar!')
print('-=-' * 18)
pcNumber = int(rd(1, 10)) #importei o randint da library random como rd, legal essa forma de import
print('Pensando...')
slp(2)
totTentativas = 0
playerNumber = int(input('Me diga o número que pensei: '))
while playerNumber != pcNumber:
    print('VOCÊ ERROU! TENTE NOVAMENTE!')
    totTentativas += 1
    playerNumber = int(input('Me diga qual número de 1 a 10 eu pensei: '))
print('VOCÊ ACERTOU!!!! eu pensei no {} e vc respondeu {}'.format(pcNumber, playerNumber))
print('Voce errou um total de {} vezes'.format(totTentativas))
