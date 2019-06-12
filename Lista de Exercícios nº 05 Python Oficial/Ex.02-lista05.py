# EXERCÍCIO Nº 02- LISTA 05 - LISTAS
print('\n Impresão II')
print('############\n')


def impressaoII(n):
    for i in range(1,n+1):
        print('-',end=" ")
        if i <=2:
            print(i)
        if i>=3:
            a=1
            for z in range (1,i+1):
                print(a,end=' ')
                a+=1
            print()
n=int(input('Informe um número inteiro: '))

impressaoII(n)
