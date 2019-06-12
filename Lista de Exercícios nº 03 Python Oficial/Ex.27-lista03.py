# EXERCÍCIO Nº 27- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nClasses de aula, turma e média de alunos')
print('########################################\n')
t=0
while t<=0 or a<=0:
    t =float(input('Insira o número de turmas: '))
    while (t) != int(t) or t<=0:
        print('O número de turmas deve ser inteiro e maior que zero')
        t =float(input('Insira o número de turmas: '))
    t=int(t)
    soma=0
    for alunos in range(1,t+1):
        a = float(input('Insira o número de alunos: '))
        while (a) != int(a) or a <= 0 or a>40:
            print('O número de alunos deve ser inteiro, maior que zero e menor que 40')
            a = float(input('Insira o número de turmas: '))
        soma +=a
    print('A média de alunos por turma é de:',round(soma/t,2),'alunos')
    break

