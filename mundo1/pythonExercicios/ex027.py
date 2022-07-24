print('============== Desafio 027 ===============')
name = input('Digite seu nome completo: ').strip()
split_name = name.split()
first_name = split_name[0]
last_name = split_name[-1]
print("""Primeiro Nome: {}
Último nome: {}""".format(first_name, last_name))
