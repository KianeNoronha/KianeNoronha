reta=int(input('Informe o comprimento da primeira reta:'))
reta2=int(input('Informe o comprimento da segunda reta:'))
reta3=int(input('Informe o comprimento da terceira reta:'))
if reta>reta2/reta3 and reta<reta2+reta3:
    print('As retas podem sim formar um triângulo')
else:
    print('As retas não podem formar um triângulo')