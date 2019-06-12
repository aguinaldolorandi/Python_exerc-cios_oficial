#EXERCÍCIO Nº 15 - LISTA 01 - ESTRUTURA SEQUENCIAL
print('Cálculo do salário mensal')
print('#########################')

salário=float(input('Insira o valor da hora trabalhada: R$ '))
horas=float(input('Insira as horas trabalhadas no mês: '))

imposto_renda= 11
inss=8
sindicato=5

salário_bruto=salário*horas
descontos=(salário_bruto*imposto_renda/100)+(salário_bruto*inss/100)+(salário_bruto*sindicato/100)
salário_líquido=salário_bruto-descontos

print('Salário bruto: R$ ',salário_bruto)
print('Desconto do Imposto de Renda: R$ ',salário_bruto*imposto_renda/100)
print('Desconto do INSS: R$ ',salário_bruto*inss/100)
print('Desconto do Sindicato: R$ ',salário_bruto*sindicato/100)
print('Total dos descontos: R$ ',descontos)
print('Salário Líquido: R$ ',salário_líquido)
