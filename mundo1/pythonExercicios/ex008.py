print("========== EXERCICIO 008 ==========")
nMet = float(input('Digite o comprimento/altura em m: '))
nCm = nMet * 100
nMm = nMet * 1000
print('_____________________________')
print('| Altura/Comprimento: {:^4} |'.format(nMet))
print('-----------------------------')
print('')
print('==========================')
print('|** Em cm = {:^10} **|'.format(nCm))
print('|** Em mm = {:^10} **|'.format(nMm))
print('==========================')
