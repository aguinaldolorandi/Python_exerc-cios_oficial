# EXERCÍCIO Nº 11- LISTA 04 - LISTAS
print('\nJunção de dois vetores')
print('######################\n')

vetor1 =[]
vetor2 =[]
vetor3=[]
vetor4=[]
for i in range(1,11):
    número1= int(input('Insira o %dº número inteiro do 1º vetor: '%i))
    número2 = int(input('Insira o %dº número inteiro do 2º vetor: '%i))
    número3 = int(input('Insira o %dº número inteiro do 3º vetor: ' % i))
    vetor1.append(número1)
    vetor2.append(número2)
    vetor3.append(número3)
for i in range(0,10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print('Vetor 1 =',vetor1)
print('Vetor 2 =',vetor2)
print('Vetor 3 =',vetor3)
print('Vetor 1 + Vetor 2 + Vetor 3 = Vetor 4 =',vetor4)