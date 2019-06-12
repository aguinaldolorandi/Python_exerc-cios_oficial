#EXERCÍCIO Nº 15 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nSérie Fibonacci')
print('###############\n')


termo=0
while termo<=0:
    termo=int(input('Insira o termo da série: '))
    if termo <=0:
        print("Insira um termo maior que zero")



primeiro=0
print (primeiro)
segundo=1
for i in range(0,termo):
    print(segundo)
    terceiro=primeiro+segundo
    primeiro=segundo
    segundo=terceiro


