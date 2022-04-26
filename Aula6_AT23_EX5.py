numero=int(input('Digite um número inteiro positivo:'))
if numero%2==0:
    quadrado=numero**2
    print('{} é par e seu quadrado é {}.'.format(numero,quadrado))
else:
    cubo=numero**3
    print('{} é impar e seu cubo fica{}.'.format(numero,cubo))
    