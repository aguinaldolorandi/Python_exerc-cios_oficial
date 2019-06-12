#EXERCÍCIO Nº 08 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nSoma e média de 5 número')
print('##################\n')
lista_de_numeros=[]



soma=0
for i in range(0,5):
    numero = int(input('Informe um numero: '))
   # lista_de_numeros.append(numero)
    soma=numero+soma


#soma=sum(lista_de_numeros)
media=soma/5

print(media,soma)
print(lista_de_numeros)



