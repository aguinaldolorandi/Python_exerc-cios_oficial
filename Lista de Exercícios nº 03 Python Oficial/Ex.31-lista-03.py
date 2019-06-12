# EXERCÍCIO Nº 31- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nLojas Tabajara')
print('##############\n')
print('Lojas Tabajara')
print('--------------')
print('--------------')
preço_do_produto=1
soma=0
i=1
while preço_do_produto>0:
    preço_do_produto = float(input('Insira o preço do produto %d: R$ '%i))
    soma+=preço_do_produto
    i+=1
print('⃝\tTotal :R$%.2f' %soma)
dinheiro=float(input('⃝\tQual o valor em dinheiro? R$ '))
while dinheiro<=soma:
    print('O valor do troco deve ser maior que o total da compra')
    dinheiro = float(input('⃝\tQual o valor em dinheiro? R$ '))


print('⃝\tTroco :R$%.2f'%(dinheiro-soma))







