from random import randint as rd
wins = 0
while True:
    jogador = int(input('[ 1 ]-Par | [ 2 ]-Ímpar: '))
    if jogador == 1:
        print('Você escolheu Par | Computador será Ímpar')
        jogNumber = int(input('Digite seu número de 0 a 10: '))
        computador = rd(0, 10)
        soma = computador + jogNumber
        if soma % 2 == 0:
            print(f'Jogador = {jogNumber}')
            print(f'Computador = {computador}')
            print(f'Resultado = Você ganhou!')
            wins = wins + 1
        else:
            print(f'Jogador = {jogNumber}')
            print(f'Computador = {computador}')
            print(f'Resultado = Computador ganhou!')
            break
    else:  # condição quando o jogador escolher ímpar
        print('Você escolheu Ímpar | Computador será Par')
        jogNumber = int(input('Digite seu número de 0 a 10: '))
        computador = rd(0, 10)
        soma = computador + jogNumber
        if soma % 2 != 0:
            print(f'Jogador = {jogNumber}')
            print(f'Computador = {computador}')
            print(f'Resultado = Você ganhou!')
            wins = wins + 1
        else:
            print(f'Jogador = {jogNumber}')
            print(f'Computador = {computador}')
            print(f'Resultado = Computador ganhou!')
            break
    print('-' * 30)
    print('{:^30}'.format('* Vamos jogar novamente! *'))
    print('-' * 30)

#  Analise pela quantidade de vitórias para usar corretamente plural e singular
if wins > 1:
    print(f'Você ganhou {wins} vezes!')
if wins == 1:
    print(f'Você ganhou apenas {wins} vez!')
if wins == 0:
    print('Você é muito ruim não ganhou nenhuma vez!!')
