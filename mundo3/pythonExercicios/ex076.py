listagem = ('Lápis', 1.78,
            'Caderno', 9.90,
            'Compasso', 15.90,
            'Computador i7', 1987.80,
            'Canetas Bic', 2.50,
            'Livro', 34.90,
            'Mochila', 129.75)
# for item in listagem:
#     print(item)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print('-' * 40)
