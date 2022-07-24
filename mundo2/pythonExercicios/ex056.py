# exercício 056

# media de idade do grupo
# nome do homem mais velho
# quantas melhores tem menos de 21

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0

for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomemaisvelho))

if totmulher20 > 1:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
else:
    print('Apenas {} mulher com menos de 20 anos'.format(totmulher20))
