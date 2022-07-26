
cont = soma = 0
n = int(input('Digite um número ou [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número ou [999 para parar]: '))
print('Você digitou 999 e o programa parou de rodar!')
print('Foram digitados {} números'.format(cont))
print('A soma entre eles é {}'.format(soma))
