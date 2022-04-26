frase=input('Digite uma grase: ').strip().upper() # Apos a sopa

palavras=frase.split() # apos a sopa
junto=''.join(palavras) # aposasopa
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra] # COLOCANDO A PALAVRA NO INVERSO
    
if inverso==junto:
    print('Temos um palíndromo')

else:
    print('A frase digitada não é um palíndromo!')