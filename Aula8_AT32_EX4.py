from secrets import choice


alu1=input('Digite o nome do primeiro aluno:')
alu2=input('Digite o nome do segundo aluno:')
alu3=input('Digite o nome do terceiro aluno:')
alu4=input('Digite o nome do quarto aluno:')
lista=(alu1,alu2,alu3,alu4)
sorteio=choice(lista)
print('O aluno sorteado foi {}.'.format(sorteio))