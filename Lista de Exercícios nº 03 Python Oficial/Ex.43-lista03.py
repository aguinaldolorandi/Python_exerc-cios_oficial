# EXERCÍCIO Nº 43- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nCardápio Lanchonete')
print('###################\n')

print('\t\t\tCARDÁPIO')
print('#####################################')
print('Produto\t\t\t\tCódigo\tPreço(R$)')
print('Cachorro quente\t\t100\t\tR$ 1,20')
print('Bauru simples\t\t101\t\tR$ 1,30')
print('Bauru com ovo\t\t102\t\tR$ 1,50')
print('Hamburguer\t\t\t103\t\tR$ 1,20')
print('Cheeseburguer\t\t104\t\tR$ 1,30')
print('Refrigerante\t\t105\t\tR$ 1,00')
print('#####################################')

código=100
sub_total_100=0
sub_total_101=0
sub_total_102=0
sub_total_103=0
sub_total_104=0
sub_total_105=0
while código>=100 and código<=105:
    código=float(input('Insira o código do produto ou código inválido para encerrar: '))
    if código==100:
        pedido_100='Cachorro quente'
        quantidade = float(input('Insira a quantidade do %s: ' %pedido_100))
        sub_total_100+=quantidade
    elif código==101:
        pedido_101='Bauru simples'
        quantidade = float(input('Insira a quantidade do %s: ' %pedido_101))
        sub_total_101 += quantidade
    elif código==102:
        pedido_102='Bauru com ovo'
        quantidade = float(input('Insira a quantidade do %s: ' %pedido_102))
        sub_total_102 += quantidade
    elif código==103:
        pedido_103='Hamburger'
        quantidade = float(input('Insira a quantidade do %s: ' %pedido_103))
        sub_total_103 += quantidade
    elif código==104:
        pedido_104='Cheeseburguer'
        quantidade = float(input('Insira a quantidade do %s: ' %pedido_104))
        sub_total_104 += quantidade
    elif código == 105:
        pedido_105 = 'Refrigerante'
        quantidade = float(input('Insira a quantidade do %s: ' % pedido_105))
        sub_total_105 += quantidade
print('###############################################')
print('################## - CONTA - ##################')
if sub_total_100!=0:
    print(pedido_100,'\t',sub_total_100,'x R$ 1,20 =\tR% ',round(sub_total_100*1.2,2))
if sub_total_101!=0:
    print(pedido_101,'\t\t', sub_total_101, 'x R$ 1,30 =\tR$ ', round(sub_total_101 * 1.3,2))
if sub_total_102!=0:
    print(pedido_102,'\t\t', sub_total_102, 'x R$ 1,50 =\tR$ ', round(sub_total_102 * 1.5,2))
if sub_total_103!=0:
    print(pedido_103,'\t\t\t', sub_total_103, 'x R$ 1,20 =\tR$ ', round(sub_total_103 * 1.2,2))
if sub_total_104!=0:
    print(pedido_104,'\t\t', sub_total_104, 'x R$ 1,30 =\tR$ ', round(sub_total_104 * 1.3,2))
if sub_total_105 != 0:
    print(pedido_105,'\t\t', sub_total_105, 'x R$ 1,00 =\tR$ ', round(sub_total_105 * 1.0, 2))

soma= round((sub_total_100*1.2+sub_total_101 * 1.3+sub_total_102 * 1.5+sub_total_103 * 1.2+sub_total_104 * 1.3+sub_total_105 * 1.0),2)
print('\t\t\t\t\t TOTAL = R$ ',soma)
print('###############################################')




