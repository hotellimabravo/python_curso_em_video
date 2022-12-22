palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')

#   Maneira de se printar fora da tupla os items que digitei
# for item in range(0, len(palavras)):
#     print(palavras[item])

#   Outra maneira de printar fora da tupla os items que digitei
# for item in palavras:
#     print(item)

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
