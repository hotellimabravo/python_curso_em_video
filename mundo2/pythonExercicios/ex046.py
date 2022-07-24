# Desafio 46
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep as slp
from emoji import emojize as emj

for c in range(10, 0, -1):
    print(c)
    # print(emj(':firecracker:'))
    slp(0.5)
print(emj(':fireworks:') * 10)
