matriz3x3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz3x3[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz3x3[l][c]:^5}] ', end='')
        if matriz3x3[l][c] % 2 == 0:
            spar += matriz3x3[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {spar}')
for l in range(0, 3):
    scol += matriz3x3[l][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz3x3[1][c]
    elif matriz3x3[1][c] > mai:
        mai = matriz3x3[1][c]
print(f'O maior valor da segunda linha é: {mai}')
