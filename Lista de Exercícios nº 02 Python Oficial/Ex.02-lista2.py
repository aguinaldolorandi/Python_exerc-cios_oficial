#EXERCÍCIO Nº 02 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Número positivo ou negativo')
print('###########################')

número=float(input('Insira um número qualquer - positivo ou negativo: '))

if número>0:
    print('O número: ',número, 'é positivo')

elif número==0:
    print('O número: ',número, 'é zero')
else:
    print('O número: ',número, 'é negativo')

