from tarfile import _Bz2ReadableFileobj


sexo=''
while sexo!='F' or sexo!='M':
    sexo=str(input('Qual o seu sexo? [M/F]:')).upper()
    if sexo=='M':
        print('Seu sexo é masculino')
        break

    if sexo=='F':
        print('Seu sexo é feminino')
        break
    