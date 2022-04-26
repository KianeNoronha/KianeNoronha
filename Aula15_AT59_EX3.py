soma=0
muie=0
media=0
maior=0
homeveio=0

for cont in range(1,4):
    nome=input('Digite o seu nome: ')
    sexo=input('Masculino ou feminino? [M/F]')
    idade=int(input('Digite a sua idade: '))
    print('-'*20)

    soma=soma+idade    #faz a soma entre todas as idades
    media=soma/cont    #pega soma das idades e divide pelo número de pessoas

    if sexo == 'M' and idade > maior:
        maior = idade
        homeveio = nome

    if sexo == 'F' and idade < 20:
        muie += 1

print('A média das idades é de {:.2f} ',format(media))
print('O nome do homem mais velho é {}'.format(homeveio))

if muie == 0:
    print('Não temos mulheres no grupo!')

else:
    print('Ao todo temos {} mulheres com menos de 20 anos'.format(muie))