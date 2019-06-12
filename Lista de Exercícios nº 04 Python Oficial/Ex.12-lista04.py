# EXERCÍCIO Nº 12- LISTA 04 - LISTAS

print('\nIdade e altura dos alunos')
print('#########################\n')
alunos=[]
n=int(input('Insira a quantidade de alunos: '))
soma_das_alturas=0
for i in range(1,n+1):
    aluno=[]
    idade=int(input('Insira a idade do %dº aluno: '%i))
    altura=float(input('Insira a altura do %dº aluno: '%i))
    aluno.append(idade)
    aluno.append(altura)
    alunos.append(aluno)
    soma_das_alturas+=altura

média=round(soma_das_alturas/(n),2)

total_de_alunos_abaixo_da_média=0
for aluno in alunos:
    if aluno [0]>=13 and aluno[1]<=média:
        total_de_alunos_abaixo_da_média+=1

print('A média de altura é de: ',média)
print('A quantidade de alunos abaixo da média é de:',total_de_alunos_abaixo_da_média)

