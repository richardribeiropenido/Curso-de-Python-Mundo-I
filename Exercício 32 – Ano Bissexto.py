from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
    print('0 ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NÃO é Bissexto'.format(ano))
