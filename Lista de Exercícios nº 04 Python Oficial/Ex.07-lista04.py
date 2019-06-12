# EXERCÍCIO Nº 07- LISTA 04 - LISTAS
print('\nCálculos de um vetor de 5 números')
print('#################################\n')

vetor=[]
soma=0
multiplicação=1
for i in range(0,5):
    número=int(input('Insira um número inteíro: '))
    vetor.append(número)
    soma+=número
    multiplicação*=número

print('Vetor = ',vetor)
print('A soma dos númeors é de: ',soma)
print('A multiplicação dos números é de: ',multiplicação)