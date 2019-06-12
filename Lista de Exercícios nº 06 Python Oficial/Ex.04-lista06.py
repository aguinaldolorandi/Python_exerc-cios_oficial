# EXERCÍCIO Nº 04- LISTA 06 - STRINGS
print('\n Nome na Vertical em Escada')
print('###########################\n')

nome=input('Insira o seu nome: ').upper()

for i in range(1,len(nome)+1):
    print('o %s'%nome[:i])

