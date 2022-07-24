print('\033[0;31m-=-\033[m' * 10)
print('\033[1;30;46m** Índice de Massa Corporal **\033[m')
print('\033[0;31m-=-\033[m' * 10)
altura = float(input('Qual sua altura? (m) '))
peso = float(input('Qual seu peso? (Kg) '))

IMC = peso / (altura ** 2)

print('{:.1f}'.format(IMC))

if IMC < 18.5:
    print('ABAIXO DO PESO')
    print('\033[7;33m** CUIDADO! **\033[m')
elif IMC >= 18.5 and IMC < 25:
    print('PESO IDEAL')
    print('\033[7;32m** TUDO OK  **\033[m')
elif IMC >= 25 and IMC < 30:
    print('SOBREPESO')
    print('\033[7;33m** CUIDADO! **\033[m')
elif IMC >= 30 and IMC < 40:
    print('OBESIDADE GRAU I')
    print('\033[7;31m** CUIDADO! ALIMENTAÇÃO! **\033[m')
else:
    print('OBESIDADE GRAU II')
    print('\033[7;31m** VAI MORRER NOVO! **\033[m')
