#EXERCÍCIO Nº 18- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nConjunto de N números')
print('#####################\n')

n = 0
while (n <= 0):
    n = int(input('Insira a quantidade de ´numeros (N) do conjunto: '))
    if (n <= 0):
        print ('Quantidade (N) deve ser positiva!')




soma=0
for i in range(0,n):
   número=int(input('Insira um número: '))
   soma =número+soma
   if 'maior' not in vars() or número > maior:
       maior = número

   if ('menor' not in vars()) or (número < menor):
       menor = número

print('A soma dos números é: ',soma)
print('O maior número é: ',maior)
print('O menor número é: ',menor)






