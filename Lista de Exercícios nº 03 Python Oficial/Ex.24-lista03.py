# EXERCÍCIO Nº 24- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nMédia Aritmética')
print('################\n')

n=0
while n>=0:
    n =float(input('Insira a quantidade de notas (N): '))
    while (n) != int(n):
        print('O número (N) deve ser inteiro')
        n =float(input('Insira a quantidade de notas (N): '))
    n=int(n)
    soma = 0
    for i in range(1, n + 1):
        nota = float(input('Insira a nota entre 0 e 10.0: '))
        while nota<0 or nota>10:
            print('A nota deve ser entre 0 e 10.0: ')
            nota = float(input('Insira a nota entre 0 e 10.0: '))
        soma = (nota + soma)
    print('A média final é: ', soma / n)
    break


