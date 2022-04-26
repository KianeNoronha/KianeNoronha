quantidade=float(input('Qual a distância percorrida em km:'))
preco1=quantidade*0.50
preco2=quantidade*0.45
if quantidade<=200:
    print('O valor da passagem é de {}.'.format(preco1))
else:
    print('O valor da passagem é de {}.'.format(preco2))
    