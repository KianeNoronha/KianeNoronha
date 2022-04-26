velocarro=float(input('Qual a velocidade do carro?'))
acima=velocarro-80
multa=acima*7
if velocarro>80:
    print('O motorista foi multado, deverá pagar {} de multa.'.format(multa))
else:
    print('O motorista não foi multado.')
    