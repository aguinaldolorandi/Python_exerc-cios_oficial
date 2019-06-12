# EXERCÍCIO Nº 14- LISTA 05 - LISTAS
print('\n Quadrado Mágico')
print('################\n')
import numpy
import random
matriz = [[1, 2, 3],  # i(linha)
          [4, 5, 6],
          [7, 8, 9]]
resultado=False

def quadradoMagico():
    global resultado
    sl = numpy.sum(matriz, axis=1)
    sc = numpy.sum(matriz, axis=0)
    sd1 = numpy.diagonal(matriz).sum()
    sd2 = matriz[0][2] + matriz[1][1] + matriz[2][0]
    if sl[0]==sl[1]==sl[2]==sc[0]==sc[1]==sc[2]==sd1==sd2:
        resultado=True
    else:
        resultado=False
    return resultado
while resultado==False:
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            z = random.choice(seq)
            matriz[i][j] = z
            x = seq.index(z)
            seq = seq[:x] + seq[x + 1:]

    quadradoMagico()

for número in matriz:
    print(número)
