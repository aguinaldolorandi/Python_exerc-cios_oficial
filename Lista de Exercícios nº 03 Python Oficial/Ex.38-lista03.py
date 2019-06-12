# EXERCÍCIO Nº 38 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nReajuste de salários')
print('####################\n')


ano_atual=1997
salário = float(input('Insira seu salário:R$ '))
while salário<=0:
    print('O salário deve ser maior que zero')
    salário = float(input('Insira seu salário:R$  '))
while ano_atual<=1997:
    ano_atual = float(input('Insira o ano corrente: '))
    while (ano_atual) != int(ano_atual) or ano_atual<=0 or ano_atual<=1997:
        print('O número deve ser inteiro, maior que zero e maior que 1997')
        ano_atual = float(input('Insira o ano corrente: '))
    ano_atual = int(ano_atual)

    salário_atual=salário
    for ano in range(1997,ano_atual+1,1):
        salário_atual*=(1+0.015*2)




print('O reajuste até o ano de: ',ano,'foi de: ',round((salário_atual/salário -1)*100,2),'% o que corresponde a: R$ ',round(salário_atual,2))


