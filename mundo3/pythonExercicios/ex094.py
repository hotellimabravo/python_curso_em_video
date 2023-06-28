pessoa = dict()
cadastro = list()
soma = media = 0
while True:
    pessoa.clear() # método que faz o dicionário pessoa ficar em branco a cada repetição do laço.
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Qual o sexo?[F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Qual a idade?: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())  # ao final de cada cadastro de pessoa uma cópia é cria em cadastro.
    while True:
        resp = str(input('Continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break
media = soma / len(cadastro)
print('-=' * 30)
print(f'    => Foram cadastradas {len(cadastro)} pessoas.')
print(f'    => A média de idade do grupo é de {media:5.2f} anos.')
print(f'    => As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
for p in cadastro:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< Encerrado >>>')
