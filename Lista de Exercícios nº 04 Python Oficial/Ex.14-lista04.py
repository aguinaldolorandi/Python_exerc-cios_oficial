# EXERCÍCIO Nº 14- LISTA 04 - LISTAS
print('\nDetetive')
print('########\n')

perguntas=['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']

resposta=0
for pergunta in perguntas:
    pessoa= input('%s (S/N): '%pergunta).upper()
    if 'S'.find(pessoa)>-1:
        resposta+=1
if resposta==2:
    print('Pessoa suspeita')
elif resposta<=4 and resposta>=3:
    print('Pessoa é cumplíce')
elif resposta==5:
    print('Pessoa é culpada')
else:
    print('Pessoa inocente')



