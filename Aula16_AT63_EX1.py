from mailbox import NotEmptyError

parar=False
homeveio=0
muieqlqr=0


print('PROGRAMA DE CONTAGEM PRESTES A SER INICIADO, PARA CONTINUAR RESPONDA AS PERGUNTAS, PARA ENCERRA-LO TECLE UM NÚMERO NEGATIVO.')

while not parar:
    sexo=input('Informe seu sexo: [F/M]').upper() .strip()
    idade=int(input('Informe sua idade em números inteiros: '))
    

    if sexo=='M' and idade>=18:
        homeveio+=1

    if sexo == 'F':
        muieqlqr+=1

    if idade<0:
            parar=True
            
print('Existem um total de {} homens com 18 anos ou mais.'.format(homeveio))
print('Existem {} mulheres nessa turma.'.format(muieqlqr))


