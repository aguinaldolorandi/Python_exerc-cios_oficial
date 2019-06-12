# EXERCÍCIO Nº 06- LISTA 04 - LISTAS
print('\nNotas de alunos')
print('###############\n')

média_dos_alunos=[]
média7=[]
for aluno in range (1,11):
    soma_das_notas=0
    for n in range (1,5):
        nota=float(input('Insira a %dª nota do %dº aluno: ' %(n, aluno)))
        soma_das_notas+=nota
    média=soma_das_notas/4
    média_dos_alunos.append(média)
    if média>=7:
        média7.append(média)

alunos7=len(média7)

print('O número de alunos com média igual ou superior a 7 é de:',alunos7,'alunos')

print(média_dos_alunos)
