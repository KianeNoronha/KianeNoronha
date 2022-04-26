num=int(input('Digite um número: '))
ttl=0

for c in range(1,num+1):
    if num%c==0:
        print('\033[33m',end=' ')
        ttl+=1

    else:
        print('\033[31m', end=' ')
    print(f'{c}',end= ' ')

print(f'\n\033[mO número {num} foi divisível {ttl} vezes.')

if ttl==2:
    print('E por isso ele é PRIMO!')

else:
    print('E por isso ele NÃO É PRIMO!')