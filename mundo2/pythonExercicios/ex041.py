from datetime import date as dt
print('*' * 35)
print(' Confederação Nacional de Natação')
print('*' * 35)
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = dt.today().year
idade_atleta = ano_atual - ano_nascimento

print('O atleta tem {} anos'.format(idade_atleta))
if idade_atleta > 25:
    print('Categoria: MASTER')
elif 19 < idade_atleta <= 25:
    print('Categoria: SÊNIOR')
elif 14 < idade_atleta <= 19:
    print('Categoria: JUNIOR')
elif 9 < idade_atleta <= 14:
    print('Categoria: INFANTIL')
else:
    print('Categoria: MIRIM')
