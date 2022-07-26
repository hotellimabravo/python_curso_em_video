resp = 'S'
cont = maior = menor = soma = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar [S|N]? : ')).upper().strip()[0]
media = (soma / cont)
print('FIM')
print('~'*65)
print('Você digitou {} números e a média dos valores digitados foi {}'.format(cont, media))
print('~'*65)
print('Dentre eles o maior número digitado é o {}, e o menor {}'.format(maior, menor))
print('~'*65)
