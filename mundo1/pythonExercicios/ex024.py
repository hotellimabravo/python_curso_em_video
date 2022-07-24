print('============== Desafio 024 ===============')
city = input('Digite um nome de cidade: ')
strip_city = city.strip() # remove os espaços antes e depois
upper_city = strip_city.upper()
split_city = upper_city.split() # pega a string e transforma em uma lista
find_santos = 'SANTO' in split_city[0] # Aqui o algoritmo analisa a primeira palavra da Lista
print('A cidade que você digitou começa com Santo?: {}'.format(find_santos))
