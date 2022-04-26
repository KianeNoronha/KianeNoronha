km=float(input('Quantos km o carro percorreu?'))
dias=float(input('Quantos dias o carro esteve com você?'))
dia2=60*dias
km2=0.15*km
preco=dia2+km2
print('Você terá que pagar {} pelos {} dias e {} km rodados.'.format(preco,km,dias))
