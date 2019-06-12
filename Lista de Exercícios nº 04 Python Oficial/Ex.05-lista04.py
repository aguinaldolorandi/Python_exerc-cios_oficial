# EXERCÍCIO Nº 05- LISTA 04 - LISTAS
print('\nNúmeros pares e ímpares')
print('#######################\n')

pares=[]
ímpares=[]
números=[]
for i in range (0,20):
    número=int(input('Insira um número inteiro: '))
    números.append(número)
    if número%2==0:
        pares.append(número)
    else:
        ímpares.append(número)

print('Lista de números = ',números)
print('Lista de números pares =',pares)
print('Lista de números ímpares = ',ímpares)
