#EXERCÍCIO Nº 13 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nBase e Expoente')
print('###############\n')

base=float(input("Insira o número da base: "))

expoente=int(input("Insira o número do expoente: "))

while expoente<=0:
    print('O expoente deve ser positivo')
    expoente = int(input("Insira o número do expoente: "))

potencia=1
for i in range(1,expoente+1):
   potencia=potencia*base
print('O resultado é de: ',potencia)




