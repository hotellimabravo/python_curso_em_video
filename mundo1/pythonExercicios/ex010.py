wallet = float(input('Quanto vc tem na carteira?: R$ '))
dollarCot = 3.27
dollarCompra = wallet / dollarCot
print('Você tem R$ {}'.format(wallet), end=' ')
print('e pode comprar = US$ {:.2f}'.format(dollarCompra))

