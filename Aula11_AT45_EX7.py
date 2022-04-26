cargo=float(input('SELECIONE SEU CARGO \n 1- Programador de sistemas; \n 2- Analista de Sistemas; \n 3- Analista de Banco de dados. \n De acordo com a tabela, digite o número do seu respectivo cargo: '))
salario=float(input('Qual o seu salário?'))

if cargo == 1:
    result1=salario+(salario*0.30)
    print('Seu salário atual é de {}.'.format(result1))


if cargo == 2:
    result2=salario+(salario*0.20)
    print('Seu salário atual é de {}.'.format(result2))

if cargo == 3:
    result3=salario+(salario*0.15)
    print('Seu salário atual é de {}.'.format(result3))