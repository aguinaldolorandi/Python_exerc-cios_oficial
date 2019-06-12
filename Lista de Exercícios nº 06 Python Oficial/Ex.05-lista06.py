# EXERCÍCIO Nº 05- LISTA 06 - STRINGS
print('\n Nome na Vertical em Escada')
print('###########################\n')

nome=input('Insira o seu nome: ').upper()
letra=len(nome)
for i in range(1,len(nome)+1):
    print('o %s'%nome[:letra])
    letra-=1


for i in range(len(nome)-1,-1,-1):
    for j in range(0,i+1):
        print('%s' %nome[j], end='')
    print()
