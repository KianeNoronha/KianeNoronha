maior = 0
menor = 500

for c in range(1, 6):
    peso = float(input('Informe o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso foi {}Kg e o menor peso foi {}Kg'.format(maior, menor))

