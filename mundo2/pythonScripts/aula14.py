# Numa repetição onde você não sabe onde ela acaba, como no for...Você pode usar o Loop While (enquanto) Por exemplo (no caso da aula) você não sabe quantos passos o personagem precisa dar para chegar na maçã ao invés de usar uma estrutura de repetição com variável de controle você pode usar uma estrutura de repetição com teste lógico

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ').upper())
print('Você finalizou!')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Par: {}'.format(par))
print('Impar: {}'.format(impar))
