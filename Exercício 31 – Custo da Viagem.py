distancia = float(input('Qual é a distância da sua vigem? '))
print('Você esta prestes a começar uma viagem de {}KM.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))

