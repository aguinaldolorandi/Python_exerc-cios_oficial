# EXERCÍCIO Nº 12- LISTA 06 - STRINGS
print('\nVALIDA E CORRIGE TELEFONE')
print('#########################\n')


fone = False
while fone == False:
    fone = input('\nInsira o telefone no formato(3xxx-xxxx): ')
    numero = [c for c in fone]
    for i in numero:
        if i == '-':
            numero.remove('-')
        else:
            numero=numero
    if ''.join(numero).isdigit() == True:
        if len(numero) == 7:
            print('Telefone: ', fone)
            fone_3 = '3'+ ''.join(numero)
            print('Telefone possui 7 digitos. Será acrecentado o digito três na frente')
            print('Telefone corrigido sem formatação: ', fone_3)
            fone_3_form= (fone_3[0:4]+'-'+fone_3[4:8])
            print('Telefone corrigido com formatação: ', fone_3_form)
            fone = True
        elif len(numero) == 8 and numero[0] == '3':
            print('Telefone: ', fone)
            fone_correto = ''.join(numero[0:4])+'-'+''.join(numero[4:8])
            print('Telefone com formatação: ', fone_correto)
            fone = True
        elif len(numero) == 8 and numero[0] != '3':
            print('Telefone: ', fone)
            print('O primeiro digito deve ser 3 ou nenhum')
            fone = False
        else:
            print('Telefone com formato inválido, é necessário pelo menos 7 digitos')
            fone = False
    else:
        print('Telefone com formato inválido')
        fone = False

