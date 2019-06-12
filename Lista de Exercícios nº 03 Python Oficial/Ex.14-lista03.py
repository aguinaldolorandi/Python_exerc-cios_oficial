#EXERCÍCIO Nº 14 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nPares e impares')
print('###############\n')
impar=0
par=0
for i in range(0,10):
    número=int(input('Insira um número inteiro: '))
    if número%2==0:
        par+=1
    else:
        impar+=1

print('O total de números pares é de: ',par,'\nO total de números impares é de: ',impar)

