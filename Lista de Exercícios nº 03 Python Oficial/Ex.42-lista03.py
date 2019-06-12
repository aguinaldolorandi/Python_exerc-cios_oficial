# EXERCÍCIO Nº 42 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nIntervalos de números')
print('#####################\n')

intervalo_a=0
intervalo_b=0
intervalo_c=0
intervalo_d=0
número=0
while número<=0:
    número =float(input('Insira um número inteiro: '))
    if número==-1:
        print('No intervalo [00-25]  temos:',intervalo_a,'números')
        print('No intervalo [26-50]  temos:', intervalo_b,'números')
        print('No intervalo [51-75]  temos:', intervalo_c,'números')
        print('No intervalo [76-100] temos:', intervalo_d,'números')
        break
    for i in range(0,25):
        if número==i:
            intervalo_a+=1
    for i in range(26,50):
        if número==i:
            intervalo_b+=1
    for i in range(51,75):
        if número==i:
            intervalo_c+=1
    for i in range(76,100):
        if número==i:
            intervalo_d+=1
    número=0


