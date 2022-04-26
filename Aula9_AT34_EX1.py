vcasa=float(input('Qual o valor da casa de desejo?'))
salario=float(input('Qual o seu salário mensal?'))
anos=float(input('Em quantos anos você pretende quitar as prestações?'))
mes=12*anos
prest=salario/mes
porcento=salario*0.30
if prest<salario:
    print('O empréstimo foi aprovado.')
else:
    print('O empréstimo foi reprovado.')