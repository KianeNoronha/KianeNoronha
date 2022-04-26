from calendar import isleap

ano=int(input('Digite um ano e lhe direi se ele é bissexto:'))

if isleap(ano):

    print('É bissexto!')
else:
    print('Não é bissexto.')


    #Com - if ano%4 == 0: também da pra fazer.