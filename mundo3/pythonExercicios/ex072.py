contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20:'))
    if 0 <= numero <= 20:
        break
print(f'Você digitou o número {contagem[numero]}')
# resp = 'S'
# while resp == 'S':
#     numero = int(input('Digite um número entre 0 e 20:'))
#     if 0 <= numero <= 20:
#         print(f'Você digitou o número {contagem[numero]}')
#         resp = str(input('Deseja continuar [S|N]?: ')).upper().strip()[0]

