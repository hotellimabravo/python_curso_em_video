def escreva(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'{msg:^{tam}}')
    print('=' * tam)


# Programa Principal
mensagem = input('Escreva algo: ')
escreva(mensagem)
