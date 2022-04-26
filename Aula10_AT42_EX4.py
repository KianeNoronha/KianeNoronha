valor=float(input('Qual o valor do produto?'))
fpgto=int(input(' ------------------------------------------ \n SELECIONE A FORMA DE PAGAMENTO \n ------------------------------------------ \n 1. À vista em dinheiro/cheque \n 2. À vista no cartão \n 3. em até 2x no cartão \n ------------------------------------------ \n Digite o número seguindo a sequência de seleção do menu:'))


if fpgto == 1:
    result= valor-0.10
    print('O seu valor final da sua compra é de {}.'.format(result))

elif fpgto == 2:
    result2= valor-0.50
    print('O seu valor final da sua compra é de {}.'.format(result2))

elif fpgto == 3:
    result3= valor
    print('O seu valor final da sua compra é de {}.'.format(result3))
