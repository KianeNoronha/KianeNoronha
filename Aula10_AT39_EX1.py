age=float(input('Diga a sua idade para retornar sua categoria:'))

if age <= 9:
    print ('Categoria: MIRIM')

if age <= 14 and age>9:
    print ('Categoria: INFANTIL')

if age <= 19 and age>14:
    print ('Categoria: JUNIOR')

if age <= 25 and age>19:
    print ('Categoria: SÊNIOR')

if age >= 25:
    print ('Categoria: MATER')




