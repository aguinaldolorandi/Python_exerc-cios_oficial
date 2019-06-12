# EXERCÍCIO Nº 07- LISTA 05 - LISTAS
print('\n Valor do Pagamento')
print('###################\n')

def valorPagamento (valorPrestação,diasAtraso):
    if diasAtraso>0:
        prestação=valorPrestação+valorPrestação*0.03+valorPrestação*0.01*diasAtraso
    if diasAtraso<=0:
        prestação=valorPrestação
    return prestação

valorFinal=0
qtdePagamentos=0
prestação=1
while prestação!=0:
    prestação=float(input('Insira o valor da prestação ou zero para encerrar: R$ '))
    if prestação !=0:
        atraso=int(input('Insira os dias de atraso: '))
        valorPrestação=valorPagamento(prestação,atraso)
        valorFinal+=valorPrestação
        qtdePagamentos+=1


print('Foram efetuados %d pagamentos, totalizando R$%.2f de prestações pagas no dia'%(qtdePagamentos,valorPrestação))



