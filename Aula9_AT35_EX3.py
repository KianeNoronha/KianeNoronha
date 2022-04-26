num1=int(input('Digite o primeiro número:'))
num2=int(input('Digite o segundo número:'))

maior=num1
menor=num1

if num2>maior:
    maior=num2
    print(maior,'é o maior número')
if num2<menor:
    menor=num2
    print(menor,'é o menor número')

if num1 == num2:
    print('Não existe número maior.')