from math import hypot
print('=' * 20)
f = 'Cálculo Hipotenusa'
print('{:^20}'.format(f))
print('=' * 20)
catetoOp = float(input('cateto oposto: '))
catetoAd = float(input('cateto adjacente: '))
hipotenusa = hypot(catetoOp, catetoAd)
print('=' * 24)
print('A hipotenusa mede: {:.2f}'.format(hipotenusa))
print('=' * 24)



