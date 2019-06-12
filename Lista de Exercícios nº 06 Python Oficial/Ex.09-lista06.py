# EXERCÍCIO Nº 09- LISTA 06 - STRINGS
print('\n Verificação de CPF')
print('###################\n')


cpf= input('Digite seu CPF (xx.xxx.xxx-xx): ' )

for i in cpf:
    if '0123456789.-'.find(i)>=0 and len(cpf)==14:
        continue
    else:
        print('CPF inválido - digite no formato CPF (xx.xxx.xxx-xx) e apenas números, ponto e traço')
        cpf = input('Digite seu CPF (xx.xxx.xxx-xx): ')

#verificação do CPF:

digito01 = float(10*int(cpf[0]) + 9*int(cpf[1]) + 8*int(cpf[2]) + 7*int(cpf[4])+ 6*int(cpf[5]) + 5*int(cpf[6]) + 4*int(cpf[8]) + 3*int(cpf[9]) + 2*int(cpf[10]))

if digito01%11 == 0 or digito01%11== 1:
    digito_J = 0
else:
    digito_J = 11 - digito01%11


digito02 = float(11*int(cpf[0]) + 10*int(cpf[1]) + 9*int(cpf[2]) + 8*int(cpf[4])+ 7*int(cpf[5]) + 6*int(cpf[6]) + 5*int(cpf[8]) + 4*int(cpf[9]) + 3*int(cpf[10]) + 2*int(digito_J))

if digito02%11 == 0 or digito02%11== 1:
    digito_K = 0
else:
    digito_K = 11 - digito02%11

if digito_J==int(cpf[12]) and digito_K==int(cpf[13]):
    print('CPF Válido')
else:
    print('CPF inválido')

