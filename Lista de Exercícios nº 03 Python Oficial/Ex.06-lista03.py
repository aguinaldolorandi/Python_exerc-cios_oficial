#EXERCÍCIO Nº 06 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nNúmeros de 1 a 20')
print('#################\n')

i=1
lista_de_numeros=[]

while i<=20:
    lista_de_numeros.append(i)
    i+=1
print('Lista de números')
for numero in lista_de_numeros:
    print('\t',numero)

print(lista_de_numeros)

for i in range(1, 21):
    print (i,end="  ")



