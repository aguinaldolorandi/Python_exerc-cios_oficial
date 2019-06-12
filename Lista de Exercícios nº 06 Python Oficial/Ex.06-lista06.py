# EXERCÍCIO Nº 06- LISTA 06 - STRINGS
print('\n Data por extenso')
print('#################\n')


data_nascimento=input('A Data de Nascimento(dd/mm/aaaa): ')

meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agsoto','setembro','outubro','novembro','dezembro']


dia=(data_nascimento[0]+data_nascimento[1])
mm=int(data_nascimento[3]+data_nascimento[4])-1
ano=data_nascimento[6:]
mes=meses[mm]

print('O Você nasceu em %s de %s de %s' %(dia,mes,ano))

