#EXERCÍCIO Nº 06 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Maior de três números')
print('#####################')

num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
num3 = int(input('Informe mais um numero: '))

if (num1 == num2) and (num1 == num3):
    print ('Os numeros sao iguais')
else:
    if(num1>num2) and (num1>num3):
        print ('O maior numero é:', num1)
    elif (num2 > num3):
        print ('O maior numero é:', num2)
    else:
        print ('O maior numero é:', num3)
    if (num1<num2) and (num1<num3):
        print('O menor numero é:', num1)
    elif (num2 < num3):
        print ('O menor numero é:', num2)
    else:
        print('O menor numero é:', num3)