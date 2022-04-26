salario=int(input('Qual o seu salário?'))
if salario>1250:
    aumento=salario*1.10
    print('Você recebeu um aumento e seu novo salário mensal será: {:.2f}.'.format(aumento))

else:
    aumento=salario*1.15
    print('Você recebeu um aumento e seu novo salário mensal será: {:.2f}.'.format(aumento))



#:.2F DIMINUI AS CASAS DECIMAIS DE UM RESULTADO E/OU CALCULO.
