# EXERCÍCIO Nº 10- LISTA 04 - LISTAS
print('\nJunção de dois vetores')
print('######################\n')

vetor1 =[]
vetor2 =[]
vetor3=[]
for i in range(0,10):
    número1= int(input('Insira um número inteiro: '))
    número2 = int(input('Insira outro número inteiro: '))
    vetor1.append(número1)
    vetor2.append(número2)
    vetor3.append(número1)
    vetor3.append(número2)


print('Vetor 1 =',vetor1)
print('Vetor 2 =',vetor2)
print('Vetor1 + Vetor2 = Vetor3 =',vetor3)
