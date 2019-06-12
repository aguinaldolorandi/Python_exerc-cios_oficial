# EXERCÍCIO Nº 34- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nNúmeros Primos')
print('##############\n')

n=0
while n<=0:
    n =float(input('Insira um número inteiro e >0: '))
    while (n) != int(n) or n<=0:
        print('O número deve ser inteiro e maior que zero')
        n = float(input('Insira um número inteiro e >0: '))
    n=int(n)
    divisores=0
    for i in range (1,n+1):
        if n%i==0:
            divisores+=1
    if divisores ==2:
        print('O número', n, 'é primo')
    else:
        print('O número', n, 'não é primo')
    n=0

