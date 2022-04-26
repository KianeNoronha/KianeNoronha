idade=int(input('Idade: '))

mn=idade
mv=idade

while True:
    idade=int(input('Idade: '))
    if idade <0:
        break

    if idade<mn:
        mn=idade
    
    elif idade>mv:
        mv=idade

media=(mn+mv)/2

print(f'Menor idade: {mn}. \nMaior idade: {mv}. \n Média entre as idades: {media:.2f}.')