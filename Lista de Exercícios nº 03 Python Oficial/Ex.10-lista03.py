#EXERCÍCIO Nº 10 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nNúmero inteiro compreendidos entre dois números')
print('###############################################\n')

num1=int(input('Insira um número: '))

num2=int(input('Insira um número: '))

if num1<num2:
    range=range(num1+1,num2)
elif num1==num2:
    print('Não há números inteiros no intervalo')
    range=range(0,0)
else:
    range=range(num2+1,num1)

for i in range:
    numero=int(i)
    print(i)

soma=0
for i in range:
    numero=int(i)
    soma=numero+soma

print('A soma total é de: ',soma)

