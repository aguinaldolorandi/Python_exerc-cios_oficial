# EXERCÍCIO Nº 22- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nNúmero Primo')
print('############\n')

a=0
número_inteiro=0
while número_inteiro>=0:
    número_inteiro =float(input('Insira um número inteiro (N)>0: '))
    while número_inteiro!=int(número_inteiro):
        print('O número deve ser inteiro')
        número_inteiro =float(input('Insira um número inteiro (N)>0: '))
    número_inteiro=int(número_inteiro)
    lista_de_divisores = []
    divisores = 0
    for i in range(1, número_inteiro):
        lista_de_divisores.append(i)
        if número_inteiro % i == 0:
            divisores = divisores + 1
            if divisores > 1:
                break
    print('O número',número_inteiro,'foi dividido', len(lista_de_divisores), 'vezes para a determinação se é ou não um número Primo')
    if divisores > 1 or número_inteiro == 1:
        print("O número não é primo")
        não_primo = número_inteiro
        lista_dos_divisores_dos_não_primos = []
        divisores2 = 0
        for i2 in range(1, número_inteiro):
            if número_inteiro % i2 == 0:
                lista_dos_divisores_dos_não_primos.append(i2)
                divisores2 += 1
        print('Os divisores do número',número_inteiro,'são:', lista_dos_divisores_dos_não_primos)
    else:
        print('É primo')
    nova_entrada = input('Deseja inserir outro número(S/N): ').upper()
    while 'SN'.find(nova_entrada) < 0:
        print('Digite S ou N')
        nova_entrada = input('Deseja inserir outro número(S/N): ').upper()
    if nova_entrada == 'S':
        a += 1
    else:
        break
print('Fim do programa')