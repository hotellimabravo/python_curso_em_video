from time import sleep as slp


def maior(* num):  # o * é para indicar que será um número variável de termos que a função irá receber
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        slp(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
