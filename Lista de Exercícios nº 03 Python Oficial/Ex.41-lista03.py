# EXERCÍCIO Nº 41 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nParcelas e Juros')
print('################\n')

inicial=int(input('Insira o valor da dívida: R$ '))

print('\t⃝ Qtde de parcelas\t%Juros sobre o valor inicial')
print('\t⃝\t\t ',1,'\t\t\t\t',0,'%')
a=10
for i in range (3,12+1,3):
    print('\t⃝\t\t ', i, '\t\t\t\t',a,'%')
    a+=5
print('\t⃝ Valor da dívida\t\tValor dos Juros\t\tQtde de Parcelas\t\tValor da Parcela')
print('\t⃝\tR$',inicial,'\t\t\t\tR$',0,'\t\t\t\t',1,'\t\t\t\t\t\tR$',inicial)
a=10
for i in range (3,12+1,3):
    dívida=inicial+inicial*int(a)/100
    juros=inicial*int(a)/100
    valor_da_parcela=round(dívida/i,2)
    print('\t⃝\tR$',dívida,'\t\t\t\tR$',juros,'\t\t\t',i,'\t\t\t\t\t\tR$',valor_da_parcela)
    a+=5