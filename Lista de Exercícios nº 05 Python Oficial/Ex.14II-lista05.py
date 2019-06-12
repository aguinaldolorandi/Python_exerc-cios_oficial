# EXERCÍCIO Nº 14II- LISTA 05 - LISTAS
print('\n Quadrado Mágico')
print('################\n')

import random
import numpy

n=int(input('Insira matriz quadrada (qtde de linhas ou colunas): '))
matriz=numpy.arange(1,(n*n+1))
matriz.shape=(n,n)


resultado=False
def quadradoMagico():
    global resultado
    s = (n + n * n * n) / 2
    sl = numpy.sum(matriz,axis=1)
    sc = numpy.sum(matriz, axis=0)
    sd1 = numpy.diagonal(matriz).sum()
    secundária = matriz[::-1]
    sd2=numpy.diagonal(secundária).sum()
    if numpy.all(sl==s) and numpy.all(sc==s) and sd1==sd2:
        resultado=True
    else:
        resultado = False
    return resultado

while resultado==False:
    seq = []
    for k in range(1, n * n + 1):
        seq.append(k)
    for i in range(n):
        for j in range(n):
            z = random.choice(seq)
            matriz[i][j] = z
            x = seq.index(z)
            seq = seq[:x] + seq[x + 1:]
    quadradoMagico()

for número in matriz:
    print(número)
