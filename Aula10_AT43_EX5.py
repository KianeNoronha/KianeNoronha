price=float(input('Qual o valor da peça?'))
quant=float(input('Quantas peças foram compradas?'))

if quant <= 5:
    result1= price-(price*0.03)
    print('O preço final da sua compra é de {}.'.format(result1))


elif quant <= 10 and quant>5:
    result2 = price-(price * 0.05)
    print('O preço final da sua compra é de {}.'.format(result2))

elif quant > 10:
    result3 = price-(price*0.07)
    print('O preço final da sua compra é de {}.'.format(result3)) 