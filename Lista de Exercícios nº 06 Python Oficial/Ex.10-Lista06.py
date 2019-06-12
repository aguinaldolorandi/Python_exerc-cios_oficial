# EXERCÍCIO Nº 10- LISTA 06 - STRINGS
print('\n Número por extenso')
print('###################\n')

número = input('Insira um número de 0 a 99: ')
número_int = int(número)
unidade = {0:'zero', 1:'um', 2:'dois', 3:'três', 4:'quatro', 5:'cinco', 6:'seis', 7:'sete', 8:'oito', 9:'nove'}
teen = {10:'dez', 11:'onze', 12:'doze', 13:'treze', 14:'quatorze', 15:'quinze', 16:'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'}
dezena = {20:'vinte', 30:'trinta', 40:'quarenta', 50:'cinquenta', 60:'sessenta', 70:'setenta', 80:'oitenta', 90:'noventa'}


if número_int < 10 or número_int>=0:
    for i in unidade:
        if i == número_int:
            unid = unidade[i]
            print('O número digitado é %d (%s)' % (número_int,unid))

if número_int >=10 and número_int <=19:
    for i in teen:
        if i == número_int:
            teen = teen[i]
            print('O número digitado é %d (%s)' % (número_int, teen))
            
if número_int >=20 and número_int <=99:
    dezena_int = int(número[1])
    unidade_int = int(número[0])
    for i in dezena:
        if i == unidade_int*10:
            dez = dezena[i]
    for i in unidade:
        if i == dezena_int:
            unid_dez=unidade[i]
    if dezena_int == 0:
        print('O número digitado é %d (%s)' % (número_int, dez))
    else:
        print('O número digitado é %d (%s e %s)' % (número_int, dez,unid_dez))
#
