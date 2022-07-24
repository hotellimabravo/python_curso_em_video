# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado peça a digitação novamente até ter um valor correto.


sexo = str(input('Qual o sexo? [M/F]: ')).upper()
while sexo != 'F' or sexo != 'M':
    sexo = str(input('Entrada errada, digite novamente usando apenas [M] Masculino e [F] Feminino: ')).upper()

print('O sexo informado é: {}'.format(sexo))
