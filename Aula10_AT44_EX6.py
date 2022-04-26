from random import choice

escolha=float(input('Faça sua escolha: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n Digite o número referente: '))
lista=('pedra','papel','tesoura')
sorteio=choice(lista)

if escolha == 1:
    print('Você escolheu pedra e seu adversário escolheu {}.'.format(sorteio))

elif escolha == 2:
    print('Você escolheu papel e seu adversário escolheu {}.'.format(sorteio))

elif escolha == 3:
    print('Você escolheu tesoura e seu adversário escolheu {}.'.format(sorteio))