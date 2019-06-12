# EXERCÍCIO Nº 01- LISTA 05 - LISTAS
print('\n Impresão')
print('#########\n')


def impressaoI(n):
    for i in range(1,n+1):
        print('-',end=" ")
        for z in range (0,i):
            print(i,end=' ')
        print()


n=int(input('Informe um número inteiro: '))

impressaoI(n)
