#EXERCÍCIO Nº 12 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Folha de pagamento')
print('##################')

valor_hora=float(input('Insira o valor da hora trabalhada: R$ '))
horas_trabalhada=float(input('Insira a quantidade de horas trabalhadas no mês: '))

salário_bruto=valor_hora*horas_trabalhada
#Tabela do Imposto de Renda
if salário_bruto<=900:
    IR=0
elif salário_bruto <=1500:
    IR=0.05
elif salário_bruto <=2500:
    IR=0.10
else:
    IR:0.20

if IR >0:
    IR1=IR*100
else:
    IR1='Isento'

INSS=0.10
FGTS=0.11

#Salário líquido, bruto e descontos:
if IR>0:
    salário_liquído=salário_bruto-(salário_bruto*IR+salário_bruto*INSS)
    desconto_IR=salário_bruto*IR1/100
    total_descontos=(salário_bruto*IR+salário_bruto*INSS)
else:
    salário_liquído = salário_bruto - (salário_bruto * INSS)
    desconto_IR=0.00
    total_descontos = salário_bruto * INSS

print('⃝ SALÁRIO BRUTO: (',valor_hora,'*',horas_trabalhada,') : R$ ',salário_bruto )
print('⃝ (-) IR   (',IR1,'$)              : R$ ',desconto_IR )
print('⃝ (-) INSS (',INSS*100,'$)             : R$ ',salário_bruto*INSS)
print('⃝ FGTS     (',FGTS*100,'$)             : R$ ',salário_bruto*FGTS)
print('⃝ TOTAL DE DESCONTOS             : R$ ',total_descontos)
print('⃝ SALÁRIO LÍQUIDO                : R$ ',salário_liquído)
