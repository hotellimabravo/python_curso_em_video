print('============== Desafio 022 ===============')
name = input('Digite o seu nome:')
print('Em maiúsculas: {}'.format(name.upper()))
print('Em minúsculas: {}'.format(name.lower()))
tirandoVazios = name.strip()
espacosVazios = name.replace(" ", "")
contaLetras = len(espacosVazios)
print('Seu nome tem {} letras.'.format(contaLetras))
separaName = name.split()
firstName = separaName[0]
qtsLetrasFirstName = len(firstName)
print('Seu primeiro nome tem {} letras.'.format(qtsLetrasFirstName))
