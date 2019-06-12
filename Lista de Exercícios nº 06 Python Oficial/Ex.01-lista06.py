# EXERCÍCIO Nº 01- LISTA 06 - STRINGS
print('\n Tamanho da String')
print('##################\n')

print('O Compara duas Strings')
string_1= input('O String 1: ')
string_2= input('O String 2: ')
comprimento_string_1=len(string_1)
comprimento_string_2=len(string_2)

print('O Tamanho de %s : %d caracteres'%(string_1,comprimento_string_1))
print('O Tamanho de %s : %d caracteres'%(string_2,comprimento_string_2))

if len(string_1)==len(string_2):
    print('O As duas strings são do mesmo tamanho')
else:
    print('O As duas strings são de tamanhos diferentes')
if string_1==string_2:
    print('O As duas strings possuem o mesmo conteúdo')
else:
    print('O As duas strings não possuem o mesmo conteúdo')