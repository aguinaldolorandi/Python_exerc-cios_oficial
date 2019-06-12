# EXERCÍCIO Nº 40 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nEstatística das cidades')
print('#######################\n')
soma = 0
soma_2 = 0
a = 1
for i in range(1, 6):
    código_da_cidade = float(input('Insira o código da cidade: '))
    número_de_veículos_da_cidade = int(input('Insira o número de veículos da cidade: '))
    número_de_acidentes_com_vítima = int(input('Insira o número de acidentes com vítima na cidade: '))
    if número_de_veículos_da_cidade<2000:
        soma_2+=número_de_acidentes_com_vítima
        a+=1
    if 'maior_índice' not in vars() or número_de_acidentes_com_vítima > maior_índice:
        maior_índice = número_de_acidentes_com_vítima
        código_da_cidade_com_maior_número_de_vítimas = código_da_cidade

    if 'menor_índice' not in vars() or número_de_acidentes_com_vítima < menor_índice:
        menor_índice = número_de_acidentes_com_vítima
        código_da_cidade_com_menor_número_de_vítimas = código_da_cidade
    soma += número_de_veículos_da_cidade

média_de_acidentes_cidades = soma_2 / a
média = soma / 5
print('A cidade com maior índice de acidentes é a ', int(código_da_cidade_com_maior_número_de_vítimas), 'com',
      maior_índice, 'vítimas')
print('A cidade com menor índice de acidentes é a ', int(código_da_cidade_com_menor_número_de_vítimas), 'com',
      menor_índice, 'vítimas')
print('A média de véiculos por cidade é de: ', média, 'veículos')
print('A média de acidentes nas cidades com menos de 2000 véiculos é de: ',média_de_acidentes_cidades)
