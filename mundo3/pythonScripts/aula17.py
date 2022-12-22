a = [2, 3, 4, 7]
b = a[:] # método utilizado para se criar uma cópia de a
b[2] = 8

# no exemplo acima ele cria uma lista A, e cria uma segunda lista B que recebe todos os valores de A
# Ao tentar adicionar b[2] = 8 ele também altera em A, porém o método descrito acima
# Faz com que b receba uma cópia de A e tudo que você alterar em B não terá mais efeito em A.

print(f'Lista A: {a}')
print(f'Lista B: {b}')
