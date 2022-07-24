vlr_produto = float(input('Digite o valor da COMPRA: R$  '))
print('Opções de pagamento:')
print('[ 1 ] - À Vista [Dinheiro|Cheque]')
print('[ 2 ] - À Vista [Débito|Cartão]')
print('[ 3 ] - 2x no Cartão de Crédito')
print('[ 4 ] - 3x ou mais no cartão')
opcao = int(input('Digite a OPÇÃO: '))

if opcao == 1:
    total = vlr_produto - (vlr_produto * (10 / 100))
    print('Valor Total = R$ {:.2f} - [10% Desconto]'.format(total))
elif opcao == 2:
    total = vlr_produto - (vlr_produto * (5 / 100))
    print('Valor Total = R$ {:.2f} - [5% Desconto]'.format(total))
elif opcao == 3:
    parcelamento = int(input('Quantas parcelas? '))
    total = vlr_produto / parcelamento
    print('Forma de Pagamento: {} x R$ {:.2f}'.format(parcelamento, total))
elif opcao == 4:
    parcelamento = int(input('Quantas parcelas? '))
    total = (vlr_produto + (vlr_produto * (20 / 100))) / parcelamento
    print('Forma de Pagamento: {} x R$ {:.2f}'.format(parcelamento, total))
