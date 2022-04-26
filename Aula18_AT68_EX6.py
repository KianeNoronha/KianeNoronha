print('Código de cargo: \n 1: Enfermeiro \n 2: Nutricionista \n 3: Médico:')

qtdenutri=0
tsn=0

while True:
    cargo=int(input('Informe um código de cargo: '))
    if cargo>=1 and cargo<=3:
        salario=float(input('Salário R$: '))
        if cargo ==2:
            qtdenutri+=1
            tsn+=salario

        resp=input('Deseja continuar: [S/N]: ')
        if resp.upper()=='N':
            break
    else:
        print('Código inválido!')


if qtdenutri>0:
    media=tsn/qtdenutri
    print(f'Média salarial das nutricionistas R$: {media:.2f}')

else:
    print('Não foram inseridos dados sobre os nutricionistas.')