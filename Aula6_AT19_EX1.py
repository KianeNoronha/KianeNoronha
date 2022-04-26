from random import randint
re=int(input('Adivinhe um número:'))
n=randint(1,5)
if n==re:
    print('Perdeu')
else:
    print('Venceu')
