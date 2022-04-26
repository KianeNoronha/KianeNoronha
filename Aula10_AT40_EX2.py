reta=int(input('Informe o comprimento da primeira reta:'))
reta2=int(input('Informe o comprimento da segunda reta:'))
reta3=int(input('Informe o comprimento da terceira reta:'))


if reta+reta2<reta3 and reta+reta3<reta2 or reta2+reta3<reta:
    print('Não é um triângulo.')
    
elif reta == reta2 and reta == reta3:
    print('EQUILATERO')

elif reta == reta2 or reta == reta3 or reta2 == reta3:
    print('ISÓSCELES')

else:
    print('ESCALENO')