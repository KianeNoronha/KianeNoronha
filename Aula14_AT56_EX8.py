n=int(input('Digite a quantidade de números a informar: '))

soma=0

for cont in range(n):
    num=float(input('Digite um número: '))
    soma+=num

me=soma/n
print(me)