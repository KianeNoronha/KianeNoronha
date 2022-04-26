num=int(input('Digite um número:'))
menu=int(input('Escolha a base de conversão 1=Binário, 2=Octal ou 3=Hexadecimal.'))

if menu==1:
    print('A conversão binária é igual a:', bin(num))
else:
    if menu==2:
        print('A conversão octal é igual a:', oct(num))
    else:
        if menu==3:
            print('A conversão hexadecimal é igual a:', hex(num))
        else:
            print('Opção inválida.')