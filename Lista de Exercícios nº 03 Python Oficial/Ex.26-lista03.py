# EXERCÍCIO Nº 26- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nEleição de três candidatos')
print('###########################\n')
n=0
while n<=0:
    n =float(input('Insira a quantidade de eleitores (N): '))
    while (n) != int(n) or n<=0:
        print('O número de eleitores (N) deve ser inteiro e maior que zero')
        n =float(input('Insira a quantidade de eleitores (N): '))
    n=int(n)
    a=0
    b=0
    c=0
    for eleitor in range (1,n+1):
        canditato=input('Favor votar em um dos três candidatos (A, B ou C): ').upper()
        while 'ABC'.find(canditato)<0:
            print('Favor votar em um dos candidatos "A"; "B ou "C"')
            canditato =input('Favor votar em um dos três candidatos (A, B ou C): ').upper()
        if canditato=="A":
            a+=1
        elif canditato=='B':
            b+=1
        else:
            c+=1
    print('Resultado das Eleições')
    print('\tCandidato A: ',a,'votos\n','\tCandidato B: ',b,'votos\n','\tCanditado C: ',c,'votos')
    break


