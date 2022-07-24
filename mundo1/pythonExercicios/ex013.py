print("========== EXERCICIO 013 ==========")
salarioFunc = float(input('Digite o salário = R$ '))
aumento = float(input('Digite o valor do aumento = '))
novoSalario = salarioFunc + ((aumento / 100) * salarioFunc)
print('O salário é = R$ {}'.format(salarioFunc))
print('O aumento de será de {}%'.format(aumento))
print('O valor do Salário com aumento = R$ {:.2f}'.format(novoSalario))


