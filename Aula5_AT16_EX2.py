from math import hypot

cateto1=float(input('Qual o cateto oposto?'))
cateto2=float(input('Qual o cateto adjacente?'))
m=hypot(cateto1,cateto2)
print('O valor da hipotenusa é:',m)
