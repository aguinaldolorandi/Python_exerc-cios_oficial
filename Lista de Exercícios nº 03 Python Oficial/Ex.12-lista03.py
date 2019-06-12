#EXERCÍCIO Nº 12 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nGerador de tabuada')
print('##################\n')

tabuada=int(input("Insira o número da tabuada (entre 1 e 10): "))

while tabuada>10 or tabuada<1:
    tabuada = int(input("Insira o número da tabuada (entre 1 e 10): "))


print('\nTabuada do ',tabuada,':\n')
for i in range(1,11):
    resultado=i*tabuada
    print('⃝',tabuada ,'X',i,'=', resultado)
