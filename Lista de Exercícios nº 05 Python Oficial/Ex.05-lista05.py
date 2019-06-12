# EXERCÍCIO Nº 05- LISTA 05 - LISTAS
print('\n Imposto')
print('############\n')

def somaImposto(taxaImposto,custo):
    imposto=custo*taxaImposto/100
    valor_final=custo+(imposto)
    return valor_final


custo=float(input('Insira o custo do produto (R$): '))
taxaImposto=float(input('Insira a taxa de imposto sobre o produto (%): '))

a=somaImposto(taxaImposto,custo)

print('O custo total do produto é de: R$',round(a,2))

