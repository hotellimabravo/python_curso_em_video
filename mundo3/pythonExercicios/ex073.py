brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
               'Athlético Paranaense', 'Atlético Mineiro', 'Fortaleza', 'São Paulo',
               'América Mineiro', 'Botafogo', 'Santos', 'Goiás', 'RedBull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará',
               'Atlético Goianiense', 'Avaí', 'Juventude')
#   Exibe os 5 primeiros colocados na tabela
print('-=' * 15)
print(brasileirao[0:5])
print('-=' * 15)
#   Exibe os 4 ultimos colocados
print(brasileirao[-4:])
print('-=' * 15)
#   Exibe em ordem alfabética
print(sorted(brasileirao))
print('-=' * 15)
for cont in range(0, len(brasileirao)):
    if brasileirao[cont] == 'RedBull Bragantino':
        print(f' RedBull Bragantino está na posição: {cont+1}')
        print('-=' * 15)

#   Outra forma de fazer a letra D é assim:
print(f'Santos está na {brasileirao.index("Santos")+1}')
print('-=' * 15)