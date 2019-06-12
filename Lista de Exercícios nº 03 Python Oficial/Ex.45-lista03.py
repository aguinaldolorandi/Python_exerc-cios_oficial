# EXERCÍCIO Nº 45 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nVerificação de nota de aluno')
print('############################\n')

professor = (input('Digite "P" para professor ou "A" para aluno: ')).upper()
while 'PA'.find(professor) < 0:
    print('A entrada deve ser: "A ou P')
    professor = (input('Digite "P" para professor ou "A" para aluno: ')).upper()
senha=0
while professor=='P' and senha!=2018:
    senha = int(input('Favor digitar a senha: '))  # senha=2018
    print('Prezado Professor, favor digitar o gabarito da prova de 10 questões')
    i = 0
    for i in range(1, 10 + 1):
        questão = (input('Digite o gabarito da questão %d (Digitar "A,B,C,D ou E"): ' % i)).upper()
        while 'ABCDE'.find(questão) < 0:
            print('O gabarito deve ser: "A,B,C,D ou E')
            questão = (input('Digite o gabarito da questão %d (Digitar "A,B,C,D ou E"): ' % i)).upper()
        if i==1:
            questão1=questão
        if i==2:
            questão2=questão
        if i==3:
            questão3=questão
        if i==4:
            questão4=questão
        if i==5:
            questão5=questão
        if i==6:
            questão6=questão
        if i==7:
            questão7=questão
        if i==8:
            questão8=questão
        if i==9:
            questão9=questão
        if i==10:
            questão10=questão
print('##############################################')
print('Início da Prova')
continua='S'
total_de_alunos=0
soma_dos_acertos=0
while continua=='S':
    acertos=0
    for questão in range(1,10+1):
        resposta=(input('Digite a resposta da questão %d (Digitar "A,B,C,D ou E"): '%questão)).upper()
        while 'ABCDE'.find(resposta)<0:
            print('A resposta deve ser: "A,B,C,D ou E')
            resposta = (input('Digite a resposta da questão %d (Digitar "A,B,C,D ou E"): ' % questão)).upper()
        if questão==1 and resposta==questão1:
            acertos+=1
        if questão==2 and resposta==questão2:
            acertos+=1
        if questão==3 and resposta==questão3:
            acertos+=1
        if questão==4 and resposta==questão4:
            acertos+=1
        if questão==5 and resposta==questão5:
            acertos+=1
        if questão==6 and resposta==questão6:
            acertos+=1
        if questão==7 and resposta==questão7:
            acertos+=1
        if questão==8 and resposta==questão8:
            acertos+=1
        if questão==9 and resposta==questão9:
            acertos+=1
        if questão==10 and resposta==questão10:
            acertos+=1
    if 'maior'not in vars() or acertos>maior:
        maior=acertos
    if 'menor'not in vars() or acertos<menor:
        menor=acertos
    total_de_alunos+=1
    soma_dos_acertos+=acertos
    continua=input('Digite "S" para realizar a prova: ').upper()


média_das_notas=round(soma_dos_acertos/total_de_alunos,2)

print('Total de alunos que realizaram a prova: ',total_de_alunos,'alunos')
print('A média das notas da turma é de: ',média_das_notas)
print('A maior nota foi: ',maior)
print('A menor nota foi: ',menor)





