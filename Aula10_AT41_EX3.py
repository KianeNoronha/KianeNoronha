massa=float(input('Qual o seu peso?'))
alt=float(input('Qual a sua altura?'))

imc=massa/alt**2

if imc <= 18.5:
    print ('Índice de massa corporal: ABAIXO DO PESO')

elif imc <= 18.5 and imc>25:
    print ('Índice de massa corporal: PESO IDEAL')

elif imc <= 25 and imc>30:
    print ('Índice de massa corporal: SOBREPESO')

elif imc <= 30 and imc>40:
    print ('Índice de massa corporal: OBESIDADE')

elif imc >= 40:
    print ('Índice de massa corporal: OBESIDADE MÓRBIDA')