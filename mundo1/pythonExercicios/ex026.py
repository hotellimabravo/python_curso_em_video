print('============== Desafio 026 ===============')
frase = input('Digite uma frase: ').strip()
qtsA = frase.upper().count('A')
print('A letra "a" aparece {} vezes na frase.'.format(qtsA))
first_A = frase.upper().find('A')+1
last_A = frase.upper().rfind('A')+1
print('A letra "a" aparece pela primeira vez na posição: {}\nE pela última vez na posição: {}'.format(first_A, last_A))
