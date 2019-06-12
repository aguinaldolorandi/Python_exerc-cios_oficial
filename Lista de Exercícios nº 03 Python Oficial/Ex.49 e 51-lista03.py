# EXERCÍCIO Nº 49 e 51- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nSérie com n termos')
print('##################\n')
n=int(input("Insira o termo n da série: "))
print('S = ',end='')

m=1
for i in range (1,n):
    if i==1:
        m=1
    else:
        m+=2
    print(i,'/',m,end=' + ')
print('n / m.')