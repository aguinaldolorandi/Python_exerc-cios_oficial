# EXERCÍCIO Nº 09- LISTA 04 - LISTAS
print('\nSoma dos quadrados')
print('##################\n')

vetor =[]
for i in range(1,11):
    número= int(input('Insira o %dº número inteiro: '%i))
    quadrado=número*número
    vetor.append(quadrado)

print('Vetor = ',vetor)
print('A soma dos quadrados dos elementos do vetor é: ',sum(vetor))



