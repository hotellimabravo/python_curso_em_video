n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('Soma: {}'.format(s))
print(f'A soma vale {s}') # formatando com FSTRINGS
# é uma forma de escrever o .format de uma maneira mais rápida e curta.
