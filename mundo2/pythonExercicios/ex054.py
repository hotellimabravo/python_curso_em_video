# exercício 054

from datetime import date as dt
totmaior = 0
totmenor = 0

for pessoas in range(0, 7):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pessoas+1)))
    atual = dt.today().year
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade.'. format(totmaior))
print('E também tivemos {} pessoas menor de idade.'.format(totmenor))
