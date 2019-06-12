# EXERCÍCIO Nº 50 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nCálculo do H da série com n termos')
print('##################################\n')
n=int(input("Insira o termo n da série: "))
print('H = ',end='')

h=1
for i in range (1,n):
    i+=1
    h+=(1/i)
print(round(h,2))