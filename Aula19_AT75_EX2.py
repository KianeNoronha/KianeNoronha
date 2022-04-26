nu=int(input('Digite quantos números inteiros quiser \n Quando quiser parar digite [999]'))
soma=1

while nu!=999:
    nu=int(input('Digite quantos inteiros quiser; \n Quando quiser parar digite [999]'))
    soma+=nu
if nu==999:
    print(soma-999)