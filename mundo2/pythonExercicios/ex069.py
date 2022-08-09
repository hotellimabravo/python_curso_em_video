tot18 = totH = totM = 0
while True:
    age = int(input('Idade: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if gender == 'M':
        totH += 1
    if gender == 'F' and age < 20:
        totM += 1
    answer = ' '
    while answer not in 'SN':
        answer = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if answer == 'N':
        break
print('*' * 35)
print(f'Pessoas com mais de 18 anos: {tot18}')
print(f'Homens cadastrados: {totH}')
print(f'Mulheres < 20 anos: {totM}')
print('*' * 35)
print('Acabou!')
