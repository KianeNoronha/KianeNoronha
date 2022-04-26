from operator import truediv
from random import randint

pc=randint(0,10)

print('Pensei em um número de 0 a 10, tente adivinhar: ')

acertou=False
palpites=0

while not acertou:
    jogador=int(input('Qual seu palpite? '))
    palpites+=1
    if jogador==pc:
        acertou=True
    else:
        if jogador<pc:
            print('Mais ... tente mais uma vez.')
        elif jogador>pc:
             print('Menos ... tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns! '.format(palpites))