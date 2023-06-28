time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))  # Entre com o nome do jogador
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))  # aqui informe quantas partidas o jogador jogou
    partidas.clear()
    for c in range(0, tot):  # Aqui o código pega a quantidade de partidas e pede para o usuário informar quantos gols o jogador realizou por partida
        partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez no {c+1}º jogo?:  ')))
    jogador['gols'] = partidas[:]  # Cria uma cópia de quantidade de gols dentro da lista "partidas"
    jogador['total'] = sum(partidas)  # Aqui o código somará a quantidade de gols que o jogador fez em todos os jogos informados
    time.append(jogador.copy())
    while True:
        resp = str(input('Continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda com S ou N')
    if resp  == 'N':
        break
print('-=' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')  # código que cria o cabeçalho de resultado
print()
print('-' * 40)
for k, v in enumerate(time):  # código que mostra os resultados de cada jogador
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
