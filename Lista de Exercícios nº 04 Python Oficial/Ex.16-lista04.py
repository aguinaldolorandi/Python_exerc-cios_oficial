# EXERCÍCIO Nº 16- LISTA 04 - LISTAS
print('\nVendedoes e comissões')
print('#####################\n')

faixas_salariais=[(200,299),(300,399),(400,499),(500,599),(600,699),(700,799),(800,899),(900,999),(1000,'em diante')]
salarioBase=200
valorvendas=1
vendas = [0, 0, 0, 0, 0, 0, 0, 0, 0]
a=0
while valorvendas!=0:
    valorvendas = float(input('Informe o valor das vendas do vendedor ou digite "0" para encerrar: '))
    if valorvendas != 0:
        salario = valorvendas * 0.09 + salarioBase
        indice = int(salario / 100)-1
        if indice >=9:
            indice=9
        vendas[indice-1]+=1
        a=+1
if valorvendas!=0 or a!=0:
    print('###############################################')
    print('As vendas foram as seguintes:')
    for i in range (0,9):
        print('-',vendas[i],'vendas','na faixa de',faixas_salariais[i],'reais')
    print('###############################################')
    print('As vendas foram as seguintes:')
    for i in range (0,9):
        print('-',vendas[i],'vendas','na faixa de R$',(i*100+salarioBase),'a R$',(i+1)*100+199)
elif valorvendas==0 and a==0:
    print('Programa encerrado')

