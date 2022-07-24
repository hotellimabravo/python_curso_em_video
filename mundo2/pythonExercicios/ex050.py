# Desafio 50
s = 0
for c in range(1, 6+1):
    n = int(input('{} - Digite um número: '.format(c)))
    if n % 2 == 0:
        s = s + n
print('A soma de todos os números pares é: {}'.format(s))
