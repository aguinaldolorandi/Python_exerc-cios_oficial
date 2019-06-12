#EXERCÍCIO Nº 09 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nNúmero par entre 0 e 150')
print('########################\n')

i=0
for i in range (0,150):
    if i/2!=int(i/2):
        print('Impar = ',i)
    elif i/2==int(i/2):
        print('Par= ',i)
    i+=1

print('fim')

for i in range(0, 150):
    if (i % 2 != 0):
        print (i)

