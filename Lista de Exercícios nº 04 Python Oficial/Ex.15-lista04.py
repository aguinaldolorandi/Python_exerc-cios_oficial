# EXERCÍCIO Nº 15- LISTA 04 - LISTAS
print('\nNotas e cálculos')
print('################\n')


lista=[]
nota=0
while nota!=-1:
    nota=float(input('Insira uma nota (número inteiro): '))
    if nota !=-1:
        lista.append(nota)
qtde=len(lista)
soma=sum(lista)
média=soma/qtde

a=0
acima_da_média=0
acima_de_sete=0
for i in lista:
    if lista[a]>média:
        acima_da_média+=1
    if lista[a]>7:
        acima_de_sete+=1
    a+=1

print('A quantidade de valores é de:',qtde)
print('Notas =',lista)
lista.reverse()
print('Notas inversa =', lista)
print('A soma das notas é de: ',soma)
print('A média das notas é de: ',média)
print('As quantidade das notas acima da média é de:',acima_da_média)
print('A quantidade das notas acima de sete é de:',acima_de_sete)
print('Fim do programa')
