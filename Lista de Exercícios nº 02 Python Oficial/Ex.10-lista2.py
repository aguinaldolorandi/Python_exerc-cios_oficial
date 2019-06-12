#EXERCÍCIO Nº 10 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Bom dia, Boa tarde e Boa noite')
print('##############################')

turno=input("Qual turno você estuda? (M/V/N): ")

if 'MVN'.find(turno.upper())>=0:
    if turno.upper()=='M':
        print('Bom dia!')
    elif turno.upper()=='V':
        print('Boa tarde!')
    else:
        print('Boa noite!')

else:
    print("Opção inválida")
