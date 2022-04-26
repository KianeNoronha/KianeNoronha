num1=float(input('Digite o primeiro número:'))
num2=float(input('Digite o segundo número:'))
menu=int(input('De acordo com o número 1, 2 e 3 selecione o quê deseja ver de acordo com a especificidade 1: Média ponderada:, 2: Quadrado da soma:, 3: Cubo do menor número:'))


mediap=(num1*2+num2*3/5)
quadrado=(num1+num2)**2
if(num1<num2):
    cubo=num1**3    
else:
    cubo=num2**3

    

if menu==1:
    print('A média ponderada do menor número é igual a:', mediap)
else:
    if menu==2:
        print('O quadrado da soma dos números é igual a:',quadrado)
    else:
        if menu==3:
            print('O cubo do menor número é:', cubo)
        else:
            print('Opção inválida.')