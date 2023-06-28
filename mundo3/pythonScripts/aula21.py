# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c} ', end='')
#         c += p
#     print('Fim')
#
#
# contador(0, 100, 10)
# contador(0, 10)
#
# help(contador)
#
# Argumentos (parâmetros opicionais)
# def somar(a=0, b=2, c=5):
#     s = a + b + c
#     print (f'A soma vale {s}')
#
# somar(1)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


s1 = somar(1, 2, 3)
s2 = somar(10, 5, 3)
s3 = somar(5, 2)

print(f'A somas são {s1}, {s2}, {s3}')
