nome_e_media = dict()
nome_e_media['nome'] = str(input('Nome: '))
nome_e_media['media'] = float(input(f'Média de {nome_e_media["nome"]}: '))
if nome_e_media['media'] >= 7:
    nome_e_media['situacao'] = 'Aprovado'
elif 5 <= nome_e_media['media'] < 7:
    nome_e_media['situacao'] = 'Recuperação'
else:
    nome_e_media['situacao'] = 'Reprovado'
print('-=' * 15)
for k, v in nome_e_media.items():
    print(f'{k} é igual a {v}')
print('-=' * 15)
