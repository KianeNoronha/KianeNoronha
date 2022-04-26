menor=0
maior=0

for data in range(7):
    data=int(input('Informe o ano de nascimento: '))

    ano=2022-data

    if ano>=18:
        maior=maior+1
    else:
        menor=menor+1
print('{} são menores de idade e {} são maiores'.format(menor, maior))


# -------------------------------------------------------- #

'''from daterime import date

atual=date.today().year
totmaior=0
totmenor=0

for pess in range(1,8):
    nasc=int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade=atual-nasc
    if idade>=18:
        totmaior+=1
        
    else:
        totmenor+=1
        
print('Ao todo {} pessoas maiores de idade.'.format(totmaior))
print('Ao todo tem {} pessoas menores de idade.'.format(totmenor))'''

# ----------------JEITO DA SORA DE FAZER------------------- #