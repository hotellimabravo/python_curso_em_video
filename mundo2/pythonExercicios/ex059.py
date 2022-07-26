n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
options = 0
while options != 5:
    options = int(input('''Escolha uma das opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Digitar novos números
    [5] Sair do programa
    Digite a opção: '''))
    if options == 1:
        soma = n1 + n2
        print('A soma dos números {} + {} é igual a {}'.format(n1, n2, soma))
    if options == 2:
        multiplicar = n1 * n2
        print('{} x {} é igual a {}'.format(n1, n2, multiplicar))
    if options == 3:
        if n1 > n2:
            print('O 1° número ({}) é o maior'.format(n1))
        else:
            print('O 2° número ({}) é o maior'.format(n2))
    if options == 4:
        print('Escolha novamente...')
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
print('Saindo...')
