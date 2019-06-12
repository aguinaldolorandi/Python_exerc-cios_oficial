# EXERCÍCIO Nº 22- LISTA 04 - LISTAS
print('\nSuporte de Informática')
print('######################\n')

print('Códigos de defeito para mouse')
print('-----------------------------')
lista=['Necessita da esfera?','Necessita de limpeza?','Necessita de troca de cabo ou conector?','Está quebrado ou inutilizado?']
for i in range(0,4):
    print(i+1,'-',lista[i])
lista2=[0]*5
print('\n')
mouses=0
defeito=1
while defeito!=0:
    defeito=int(input('Insira o código do defeito (1 a 4) ou zero para finalizar: '))
    if 4 >= defeito > 0:
        lista2[defeito]+=1
        mouses+=1
print('Quantidade de mouses: ',mouses)
print('\tDefeito\t\t\t\t\t\t\t\t\t\t\tQuantidade\t\t\tPercentual(%)')
for i in range(0,4):
    print('%d - %-50s %-20d %.2f' %(i+1,lista[i],lista2[i+1],lista2[i+1]/mouses*100))

