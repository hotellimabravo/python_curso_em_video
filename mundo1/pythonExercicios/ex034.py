salario = float(input('Digite o salário: R$'))
if salario > 1250.00:
    aumento = (salario * 10/100) + salario
    print('** 10% de aumento! ** - Salário: R${:.2f}'.format(aumento))
else:
    aumento = (salario * 15/100) + salario
    print('** 15% de aumento! ** - Salário: R${:.2f}'.format(aumento))
