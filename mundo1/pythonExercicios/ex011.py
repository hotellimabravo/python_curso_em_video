print("========== EXERCICIO 011 ==========")
altura = float(input('Altura da parede = '))
largura = float(input('Largura/base da parede = '))
A = altura * largura
tinta = A / 2
print('Dimensão = {}m x {}m'.format(altura, largura))
print('Área = {} m²'.format(A))
print('{:.2f} litros de tinta'.format(tinta))
