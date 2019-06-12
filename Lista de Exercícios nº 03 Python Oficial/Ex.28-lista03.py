# EXERCÍCIO Nº 28- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nColecionador de CDs')
print('###################\n')

cd=0
while cd<=0:
    cd =float(input('Insira a quantidade de CDs: '))
    while (cd) != int(cd) or cd<=0:
        print('A quantidade de CDs deve ser um número inteiro e maior que zero')
        cd = float(input('Insira a quantidade de CDs: '))
    cd=int(cd)
    soma=0
    for cd in range(1,cd+1):
        valor = float(input('Insira o valor do CD: R$ '))
        while valor <= 0:
            print('O valor do CD deve ser um valor maior que zero')
            valor = float(input('Insira o valor do CD: R$ '))
        soma +=valor
    print('O valor total investido em CDs é de:R$',soma, '\nO valor médio por CD é de: R$',round(soma/cd,2))
    break