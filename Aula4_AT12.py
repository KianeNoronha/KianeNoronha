from math import sqrt


p1x=float(input('Digite o primeiro ponto do plano cartesiano:'))
p1y=float(input('Digite o segundo ponto do plano cartesiano:'))
p2x=float(input('Digite o terceiro ponto do plano cartesiano:'))
p2y=float(input('Digite o quarto ponto do plano cartesiano:'))
d=sqrt(p1x-p1y)**2 + (p2x+p2y)**2
print(d)