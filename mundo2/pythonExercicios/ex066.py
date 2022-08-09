cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'Foram digitados {cont} números, e a soma entre eles é {soma}.')
