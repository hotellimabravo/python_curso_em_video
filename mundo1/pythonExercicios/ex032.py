from datetime import date as dt
ano = int(input('Digite o ano para saber se é BISSEXTO ou não: '))
if ano == 0:
    ano = dt.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('{} é BISSEXTO'.format(ano))
else:
    print('{} NÃO É BISSEXTO'.format(ano))
