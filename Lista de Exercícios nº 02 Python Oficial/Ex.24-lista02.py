#EXERCÍCIO Nº 24 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Número: par; +/-; inteiro ou decimal')
print('############################')

num1=float(input('Insira um número: '))

num2=float(input('Insira outro número: '))

operação= input('Indique a operação: (+); (-); (*); (/) : ')

if operação=='+':
    resultado= (num1+num2)
elif operação=='-':
    resultado = (num1 - num2)
elif operação=='*':
    resultado = (num1 * num2)
elif operação=='/':
    resultado = round((num1/num2),4)
else:
    print('Operação Inválida')

if resultado==int(resultado):
    numin='Número Inteiro'
else:
    numin='Número Decimal'

if resultado/2==int(resultado/2):
    numpar='Número Par'
else:
    numpar='Número Impar'

if resultado>=0:
    numpos='Número Positivo'
else:
    numpos='Número Negativo'

print('Resultado = ',resultado,'é',numpar,'é', numpos,'é', numin)

