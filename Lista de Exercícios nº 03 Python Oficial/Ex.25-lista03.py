# EXERCÍCIO Nº 25- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nPessoa jovem, adulta ou idosa')
print('#############################\n')

n=0
while n>=0:
    n =float(input('Insira a quantidade de pessoas (n): '))
    while (n) != int(n) or n<=0:
        print('O número (n) deve ser inteiro e maior que zero')
        n =float(input('Insira a quantidade de pessoas (n): '))
    n=int(n)
    i = 0
    while i >= 0:
        soma = 0
        for pessoa in range(1, n + 1):
            i = float(input('Insira a idade da pessoa entre zero e 99 anos (i): '))
            while (i) != int(i)or i<0 or i>99:
                print('A idade deve ser um número inteiro e ser entre zero e 99 anos')
                i = float(input('Insira a idade da pessoa entre zero e 99 anos (i): '))
            soma = soma + i
        media = int(soma/n)
        print('A média da idade da Turma é de: ',media,'anos')
        if media>=0 and media<=25:
            print('A turma é jovem')
        elif media>=26 and media<=60:
            print('A Turma é adulta')
        else:
            print('A Turma é idosa')
        break
    break



