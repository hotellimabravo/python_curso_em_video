estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estados: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k.upper()} - {v}')
