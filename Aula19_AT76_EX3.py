nmr=int(input('Digite um número: '))

mn=nmr
mv=nmr

while True:
    nmr=int(input('Digite um número:\n Caso deseje parar digite ¨S¨. '))
    if nmr == 'S':
        break

    if nmr<mn:
        mn=nmr
    
    elif nmr>mv:
        mv=nmr

media=(mn+mv)/2

print(f'Menor idade: {mn}. \nMaior idade: {mv}. \n Média entre as idades: {media:.2f}.')