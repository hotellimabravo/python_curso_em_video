# Desafio 48
s = 0
cont = 0
for c in range(1, 500+1):
    if c % 2 == 1:  # acha os números ímpares
        if c % 3 == 0:  # acha os divisíveis por 3
            cont += 1
            s += c
print('A soma de todos os {} números ímpares e divisíveis por 3 dentro do intervalo de 1 a 500 é: {}'.format(cont, s))  # informa a soma de todos os números que são ímpares e divisíveis por 3

