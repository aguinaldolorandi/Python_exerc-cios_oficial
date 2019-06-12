# EXERCÍCIO Nº 21- LISTA 04 - LISTAS
print('\nConsumo de Combustível')
print('######################\n')
carros=[]
consumos=[]
for i in range(1,6):
    carro = input('Digite o modelo do %dº carro: ' %i).upper()
    consumo=float(input('Digite o consumo de combustível do %dº carro: '%i))
    carros.append(carro)
    consumos.append(consumo)
litros='litros'
print('--------------------Relatório Final--------------------')
print('-------------------------------------------------------')
print(' Carro \t\t\t km/l\tConsumo/1000km\t\tCusto Total')
for i in range(0,5):
    print('o %d - %-10s %-6.2f %-7.2f %-10s  R$%.2f'%(i+1,carros[i],consumos[i],(1000/consumos[i]),litros,(1000/consumos[i]*2.25)))
print('-------------------------------------------------------')


