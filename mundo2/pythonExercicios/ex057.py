# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado peça a digitação novamente até ter um valor correto.


sexo = str(input('Informe o sexo [F]eminino ou [M]asculino: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite novamente [F] ou [M]: ')).upper()
if sexo == 'M':
    print('Masculino')
if sexo == 'F':
    print('Feminino')
