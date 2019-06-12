# EXERCÍCIO Nº 03- LISTA 04 - LISTAS
print('\nMédia de 4 notas')
print('################\n')

notas=[]
soma=0
for i in range (0,4):
    nota=float(input('Insira a nota: '))
    notas.append(nota)
    soma+=nota

média=soma/4
print('As notas são as seguintes')
i=1
for nota in notas:
    print('\tA %dª nota é: '%i,nota)
    i+=1
print('A média das notas é: ',média)