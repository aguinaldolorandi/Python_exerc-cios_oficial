# EXERCÍCIO Nº 02- LISTA 04 - LISTAS
print('\nVetor de 10 números inverso')
print('###########################\n')

vetor=[]
for i in range(0,10):
    número=int(input('Insira um número inteíro: '))
    vetor.append(número)
vetor.reverse()
#print(vetor[::-1]) outra forma
print(vetor)