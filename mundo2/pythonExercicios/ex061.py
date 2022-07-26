# Eu atualizei o exercício para mostrar quantos termos da PA que o usuário escolher.
print(' * ' * 10)
print('{:=^30}'.format('PROGRESSÃO ARITMÉTICA'))
print(' * ' * 10)
t1 = int(input('Primeiro termo da PA: '))
r = int(input('razão para a PA: '))
termos = int(input('Quantos termos?: '))
cont = 1

while cont <= termos:  # enquanto o contador de termos for menor ou igual a quantidade de termos que o usuário selecionou, vai ser executado o programa abaixo, podendo o mesmo selecionar quantos termos ele quiser exibir.
    print(t1, end=' -> ')
    t1 = t1 + r  # fórmula para atualizar os termos da PA
    cont += 1
print('FIM')
