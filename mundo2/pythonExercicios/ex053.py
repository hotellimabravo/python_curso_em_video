# Desafio 053

print(' * ' * 11)
print('{:=^32}'.format('DETECTOR DE PALÍNDROMOS'))
print(' * ' * 11)
phrase = input('Digite uma frase: ').strip().upper()
print(' * ' * 11)
words = phrase.split()
together = ''.join(words)
invert = ''

for letter in range(len(together) - 1, -1, -1):
    invert += together[letter]
print('O inverso de {} é {}'.format(together, invert))
print(' * ' * 11)

if invert == together:
    print('\033[32mTEMOS UM PALÍNDROMO!!!!\033[m')
    print(' * ' * 11)
else:
    print('\033[41mNÃO É UM PALÍNDROMO!!!!\033[m')
    print(' * ' * 11)


# outra solução
'''Outra solução'''

# No lugar do for escrever a função de inversão dessa maneira:

invert1 = together[::-1]
print(invert1)
