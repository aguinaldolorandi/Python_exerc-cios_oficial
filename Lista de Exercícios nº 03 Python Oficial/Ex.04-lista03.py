#EXERCÍCIO Nº 04 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nCrescimento Populacional')
print('########################\n')


habitantes_A=80000
taxa_anual_A=0.03
habitantes_B=200000
taxa_anual_B=0.015

i=1
a=80000
b=200000
while a<=b:
    a=int(a+a*taxa_anual_A)
    b=int(b+b*taxa_anual_B)
    i+=1

print('A população A é de: ',a,' habitantes\n\nA população B é de: ',b,' habitantes')

print('\nEste crescimento ocorreu em: ',i,' anos')