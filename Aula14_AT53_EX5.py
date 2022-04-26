from html.entities import name2codepoint


n1=int(input('Digite um número inteiro:'))
n2=int(input('Digite um número inteiro:'))
n3=int(input('Digite um número inteiro:'))
n4=int(input('Digite um número inteiro:'))
n5=int(input('Digite um número inteiro:'))
n6=int(input('Digite um número inteiro:'))

lista=n1,n2,n3,n4,n5,n6

if n1%3==0:
    n1=0

if n2%3==0:
    n2=0

if n3%3==0:
    n3=0

if n4%3==0:
    n4=0

if n5%3==0:
    n5=0

if n6%3==0:
    n6=0

print(n1+n2+n3+n4+n5+n6)
