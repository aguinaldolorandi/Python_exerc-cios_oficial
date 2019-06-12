# EXERCÍCIO Nº 21- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nNúmero Primo')
print('############\n')
lista=[2,3,5,7,11,13,17]
a=0
número_inteiro=0
while número_inteiro>=0:
    número_inteiro =float(input('Insira um número inteiro >0: '))
    while número_inteiro!=int(número_inteiro):
        print('O número deve ser inteiro')
        número_inteiro =float(input('Insira um número inteiro >0: '))
    número_inteiro=int(número_inteiro)
    divisores = 0
    for i in range(1, número_inteiro):
        if número_inteiro % i == 0:
            divisores=divisores+1
            if divisores>1:
                break
    if divisores > 1:
        print("O número não é primo")
    elif número_inteiro == 1:
        print("O número não é primo")
    else:
        print('O número é primo')
    nova_entrada = input('Deseja inserir outro número(S/N): ').upper()
    while 'SN'.find(nova_entrada) < 0:
        print('Digite S ou N')
        nova_entrada = input('Deseja inserir outro número(S/N): ').upper()
    if nova_entrada == 'S':
        a += 1
    else:
        break

