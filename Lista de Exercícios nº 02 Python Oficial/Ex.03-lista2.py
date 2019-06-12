#EXERCÍCIO Nº 03 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Sexo: Masculino ou Feminino')
print('###########################')

sexo=input("Insira seu sexo (M/F): ")

if sexo.upper()=='M':
    print('Sexo Masculino')
elif sexo.upper()=='F':
    print('Sexo Feminino')
else:
    print('Opção inválida')
