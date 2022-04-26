nasc=float(input('Quantos anos você tem?'))

if nasc == 18:
    print('Você deve comparecer a junta miliar o quanto antes.')

if nasc <= 18:
    result=18-nasc
    print('Você tem {} ano até ter que comparecer a junta militar.'.format (result))

if nasc >= 18:
    result2=nasc-18
    print('Você já passou {} anos de comparecer a junta miliar.'.format (result2))
