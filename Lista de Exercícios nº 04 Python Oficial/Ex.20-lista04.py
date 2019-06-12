# EXERCÍCIO Nº 20- LISTA 04 - LISTAS
print('\nAbono salarial Tabajara')
print('#######################\n')

salários={}
abonos=[]
salário=1
total_de_funcionários=0
total_abono=0
valor_mínimo=0
while salário!=0:
    salário = float(input('Digite o salário do colaborador ou 0 para finalizar: R$ '))
    while salário<0:
        print('Digite um número inteiro ou zero para encerrar')
        salário = float(input('Digite o salário do colaborador ou 0 para finalizar: '))
    if salário!=0:
        abono=salário*0.2
        if abono<=100:
            abono=100
            salário_com_abono=salário+abono
            valor_mínimo+=1
        else:
            salário_com_abono=salário+abono
        total_abono+=abono
        abonos.append(abono)
        salários[salário_com_abono]=abono
        total_de_funcionários+=1

print('----------------------------------------')
print('Projeção de gastos com Abono:')
for salário_com_abono in salários:
    print('Salário: R$%-25.2f' %salário_com_abono)
print('----------------------------------------')
print(' Salário\t\t\tAbono')
for (salário_com_abono,abono) in salários.items():
    print('R$%-17.2f R$%.2f'%(salário_com_abono,abono))
print('----------------------------------------')
print('Foram processados %d colaboradores' %total_de_funcionários)
print('----------------------------------------')
print('Valor total gasto com abonos: R$%.2f' %total_abono,)
print('Valor mínimo pago a %d colaboradores' %valor_mínimo)
print('Maior valor de abono pago: R$%.2f' % max(abonos))
print('----------------------------------------')