#EXERCÍCIO Nº 28 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Hipermercado Tabajara')
print('#####################')

print('PROMOÇÃO DE CARNES\nHIPERMERCADO TABAJARA')
print('Carnes\t\t\tAté 5Kg\t\tAcima de 5 Kg\nFilé duplo (F)\tR$4,90/kg\tR5,80/kg\nAlcatra(A)\t\tR$5,90/kg\tR$6,80/kg\nPicanha(P)\t\tR$6,90/kg\tR$7,80\n')

carne_entrada=input('Tipo de Carne: Filé duplo (F); Alcatra(A); Picanha (P): ')

qtde=float(input('Quantidade de carne em kilos: '))

pagamento_entrada=input('Dinheiro ou cartão (D ou C): ')

pagamento=pagamento_entrada.upper()

carne=carne_entrada.upper()




cartão='cartão de crédito'

if carne=='F':
    if qtde<=5:
        preço=4.9
        carne='Filé duplo'
    else:
        preço=5.8
        carne = 'Filé duplo'
elif carne=='A':
    if qtde <= 5:
        preço = 5.9
        carne = 'Alcatra'
    else:
        preço = 6.8
        carne = 'Alcatra'
elif carne=='P':
    if qtde <= 5:
        preço = 6.9
        carne = 'Picanha'
    else:
        preço = 7.8
        carne = 'Picanha'
else:
    print('Opção inválida')

valor_total=round(preço*qtde,3)

if pagamento=='D':
    total_a_pagar=valor_total
    pagamento='Dinheiro'
else:
    total_a_pagar=valor_total*0.95
    pagamento='Cartão de crédito'

desconto=round(valor_total-total_a_pagar,3)

print('\n Carne:\t\t\t',carne,'\n','Quantidade:\t',qtde,'kg','\n','Preço total:\t R$',valor_total,'\n','Pagamento:\t\t',pagamento,'\n',
      'Desconto:\t\t R$',desconto,'\n\n','Total a pagar:\t R$',round(total_a_pagar,3))




