nome = str(input('Qual é seu nome?:'))

if nome == 'Hugo':
    print('Hugos são pessoas muito legais!!!!')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('Seu nome é um bocado normal')

elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Seu nome é bem feminino!!!')

else:
    print('Pessoa Normal')

print('Olá {}, tenha um bom dia!'.format(nome))
