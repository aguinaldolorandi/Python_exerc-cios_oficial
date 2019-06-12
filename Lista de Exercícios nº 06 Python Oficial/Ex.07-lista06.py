# EXERCÍCIO Nº 07- LISTA 06 - STRINGS
print('\n Conta Espaços e Vogais')
print('#######################\n')

frase=input('Insira uma frase: ').upper()
k=0
j=0
for i in frase:
    if i ==' ':
        k+=1
    else:
        k+=0
    if 'AEIOUÉÔÃÍ'.find(i)>=0:
        print('AEIOUÉÔÃÍ'.find(i))
        j+=1
    else:
        j+=0


print('\nA frase possui %d espaços vazios e %d vogais' %(k,j))

