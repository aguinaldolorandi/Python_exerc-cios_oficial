#EXERCÍCIO Nº 05 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Notas e média final dos alunos')
print('##############################')\

nota1= float(input('Informe a 1ª nota: '))
nota2= float(input('Informe a 2ª nota: '))

média=(nota1+nota2)/2

if média>=7 and média<10:
    print("Aprovado")
elif média<7:
    print("Reprovado")
elif média==10:
    print("Aprovado com Distinção")
else:
    print("valor inválido")
