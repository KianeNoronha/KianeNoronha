menu=int(input('*************************************** \n CÁLCULO DE GRANDEZAS ELÉTRICAS \n *************************************** \n 1. Tensão (em Volt) \n 2. Resistência (em Ohm) \n 3. Corrente (em Ampére) \n *************************************** \n Qual grandeza deseja calcular? '))
if menu==1:
    valo1=float(input('Digite o valor da resistência:'))
    valo2=float(input('Digite o valor da corrente:'))
    ten=valo1*valo2
    print('O valor de tensão será', ten)

elif menu==2:
    valo1=float(input('Digite o valor de tensão:'))
    valo2=float(input('Digite o valor de corrente:'))
    res=valo1/valo2
    print('O valor da resistência será de', res)

elif menu==3:
    valo1=float(input('Digite o valor de tensão:'))
    valo2=float(input('Digite o valor de resistência:'))
    ten=valo1/valo2
    print('O valor da tensão será de', ten)