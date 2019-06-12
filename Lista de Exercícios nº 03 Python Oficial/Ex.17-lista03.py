#EXERCÍCIO Nº 17 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nCálculo de fatorial')
print('###################\n')

termo=int(input('Insira o número para fatorar: '))


i=1
fatorial=1
while i<=termo:
    fatorial=fatorial*i
    i+=1


print('O resultado do fatorial',termo,'! é:' ,fatorial)
