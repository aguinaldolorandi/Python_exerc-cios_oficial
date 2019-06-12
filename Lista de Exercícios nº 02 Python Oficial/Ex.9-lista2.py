#EXERCÍCIO Nº 09 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Ordem descrescente')
print('##################')

num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
num3 = int(input('Informe mais um numero: '))

lista=[num1,num2,num3]
lista.sort(reverse=True)

print(lista)

