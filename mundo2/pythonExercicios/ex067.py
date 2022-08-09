while True:
    tabuada = int(input('Qual a tabuada?: '))
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada*c}')
print('Tabuada finalizada!')
