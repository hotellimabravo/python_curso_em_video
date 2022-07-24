valor_casa = float(input('Qual o valor do imóvel?: R$ '))
salario_comprador = float(input('Informe o valor da renda mensal: R$ '))
qtd_parcelas = int(input('Informe o número de parcelas: '))

vlr_parcela_possivel = salario_comprador * (30 / 100)  # vlr de parcela que o comprador pode pagar

vlr_parcela_imovel = valor_casa / qtd_parcelas  # vlr que vai dar a parcela do imóvel (valor do imovel dividido pela
# quantidade de parcelas)

vlr_pcl_se_reprovado = valor_casa / vlr_parcela_possivel

if vlr_parcela_possivel >= vlr_parcela_imovel and qtd_parcelas <= 360:
    print(' ')
    print('*' * 35)
    print('Financiamento APROVADO!')
    print('Seu financiamento ficou: {} x R$ {:.2f}'.format(qtd_parcelas, vlr_parcela_imovel))
    print('*' * 35)
elif qtd_parcelas > 360:
    print('*' * 35)
    print('Verificar quantidade de parcelas e simular novamente')
    print('Quantidade parcelas máxima é *** 360 ***')
    print('*' * 35)
else:
    print('Financiamento REPROVADO!')
    print("""Sua renda R$ {:.2f} é incompatível com o financiamento
O valor do Imóvel é R$ {:.2f} em {} x R$ {:.2f} 
Simule o financiamento aumentando a 
quantidade de parcelas para {:.0f} x""".format(salario_comprador, valor_casa, qtd_parcelas, vlr_parcela_imovel, vlr_pcl_se_reprovado))


# O algoritmo, caso o financiamento seja reprovado, pode sugerir
# o número de parcelas que dê para aprovar, ou valor,
# ou quanto o cliente deveria ganhar de renda para que seu financiamento possa ser aprovado.

