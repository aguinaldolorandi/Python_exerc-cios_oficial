# EXERCÍCIO Nº 35- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nNúmeros Primos')
print('##############\n')

intervalo=0
while intervalo<=0:
    intervalo =float(input('\nInsira um número inteiro e >0: '))
    while (intervalo) != int(intervalo) or intervalo<=0:
        print('O número deve ser inteiro e maior que zero')
        n = float(input('Insira um número inteiro e >0: '))
    intervalo=int(intervalo)
    print('Os números primos até',intervalo,'são os seguintes: ',end='')
    for n in range(0, intervalo + 1):
        divisores = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divisores += 1
        if divisores == 2:
            print(n, end=',')
    intervalo=0
