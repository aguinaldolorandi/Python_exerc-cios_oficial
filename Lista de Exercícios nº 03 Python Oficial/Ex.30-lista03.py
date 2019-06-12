# EXERCÍCIO Nº 30- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nPanificadora Pão de Ontem')
print('#########################\n')

preço_do_pão=0
while preço_do_pão<=0:
    preço_do_pão=float(input('Insira o preço do pão:R$ '))
    if preço_do_pão<=0:
        print('O preço do pão deve ser maior que zero')



print('Panificadora Pão de Ontem - Tabela de Preços')
print('--------------------------------------------')
print('\tPreço do Pão: R$ ',preço_do_pão)
print('--------------------------------------------')
for i in range(1,51):
    print('\t⃝ ', i,' -  R$',round(preço_do_pão*i, 2))