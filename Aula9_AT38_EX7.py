nota1=float(input('Diga a sua primeira nota:'))
nota2=float(input('Diga a sua segunda nota:'))

notas=(nota1+nota2/2)

if notas<5:
    print('Reprovado.')

if notas>=5 and notas<7:
    print('Recuperação')

if notas >= 7:
    print('Aprovado.')