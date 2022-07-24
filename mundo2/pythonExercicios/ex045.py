from random import randint as rd 
from time import sleep as slp 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = rd(0, 2)  # rd é o nome que eu importei para o randint
print('')
print('{:=^20}'.format(' JOKENPÔ '))
print('')
print("""Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogador = int(input('Qual sua jogada? '))
print('')
print('JO')
slp(1)
print('KEN')
slp(1)
print('PO!!')
slp(0.5)
print('')
print('-=-' * 9 )
print('Computador escolheu: {}'.format(itens[computador]))
print('Jogador Escolheu: {}'.format(itens[jogador]))
print('-=-' * 9 )

if computador == 0: # Pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2: 
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: # Papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2: 
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # Tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2: 
        print('Empate!')
    else:
        print('JOGADA INVÁLIDA!')
