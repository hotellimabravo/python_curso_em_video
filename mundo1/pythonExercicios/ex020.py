from random import shuffle
n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')
n4 = input('Nome do aluno 4: ')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem das apresentações será: {}')
print('=' * 52)
print('{}'.format(alunos))
print('=' * 52)

