erros=0
parar=False

for c in range(3,0,-1):  
    senha=int(input('Digite sua senha: '))
    if senha == 123456:
        print('Seja bem vindo!')
        break
    elif senha != 123456:
        senha=int(input('Senha incorreta, você tem {} tentativas: '.format(c)))
        if senha == 123456:
            print('Seja bem vindo!')
            break
        else:
            print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')
