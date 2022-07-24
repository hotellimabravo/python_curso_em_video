from datetime import date as dt

# cabeçalho
print('=' * 16)
print('CÁLCULO DE IDADE')
print('=' * 16)

# captura data de nascimento
dia = int(input('Digite o dia do nascimento: '))
mes = int(input('Digite o mês do nascimento: '))
ano = int(input('Digite o ano do nascimento: '))
data_nascimento = dt(ano, mes, dia)
diff = (dt.today() - data_nascimento)

# calculos e resultados
result = (diff.days / 365.25)

# mostra idade na tela
print(int(result))
