n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
listaNumbers = [n1, n2, n3]
ordemNumbers = sorted(listaNumbers)
print('O número {} é o maior, e o número {} é o menor'.format(ordemNumbers[2], ordemNumbers[0]))


