#EXERCÍCIO Nº 06 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nMaior de 5 números')
print('##################\n')

num1=int(input('Insira o primeiro número: '))
num2=int(input('Insira o segundo número: '))
num3=int(input('Insira o terceiro número: '))
num4=int(input('Insira o quarto número: '))
num5=int(input('Insira o quinto número: '))

lista_números=[num1,num2,num3,num4,num5]
lista_números_ordenada=sorted(lista_números)
print(lista_números_ordenada)

print('O maior número é: ',lista_números_ordenada[4])
print('O menor número é: ',lista_números_ordenada[0])

