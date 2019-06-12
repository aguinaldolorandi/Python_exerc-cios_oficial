# EXERCÍCIO Nº 32- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nFatorial de um número inteiro')
print('#############################\n')

n=0
while n<=0:
    n =float(input('Insira um número inteiro >0: '))
    while (n) != int(n) or n<=0:
        print('O número deve ser inteiro e maior que zero')
        n = float(input('Insira um número inteiro >0: '))
    n=int(n)
fatorial=1
for i in (range(1,n+1)):
    fatorial *= i
print('○ Fatorial de:',n)
print('⃝',n,'! = ',end='')
for i in reversed(range(2,n+1)):
    print(i,end=' . ')
print('1 =',fatorial)



