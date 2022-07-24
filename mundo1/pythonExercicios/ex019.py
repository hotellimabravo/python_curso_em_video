from random import choice
aluno1 = input('Nome 1: ')
aluno2 = input('Nome 2: ')
aluno3 = input('Nome 3: ')
aluno4 = input('Nome 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)
print('O aluno escolhido é: {}'.format(escolhido))
