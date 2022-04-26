soma=0

nome = input('Nadador 1: ')
tempo = int(input('Qual o tempo do nadador? '))

mn=nome
mt=tempo
pn=nome
pt=tempo

somatempo=0
somatempo+=tempo
tempo12s15s=0

if 12 <= tempo <= 15:
    tempo12s15s+=1

for nadador in range(2,8):
    nome = input(f'Nadador {nadador}: ')
    tempo = float(input(f'Tempo do nadador {nadador}: '))

    if tempo<mt:
        mn=nome
        mt=tempo

    elif tempo>pt:
        pn=nome
        pt=tempo

somatempo+=tempo

if 12<=tempo<=15:
    tempo12s15s+=1

print(F'{mn} é o melhor nadador com {mt} seg. \n {pn} é o pior nadador com {pt}.')

media=somatempo/7

print(f'Média dos tempos = {media:.2f} seg. \n Atletas entre 12 seg e 15 seg: {tempo12s15s}.')
