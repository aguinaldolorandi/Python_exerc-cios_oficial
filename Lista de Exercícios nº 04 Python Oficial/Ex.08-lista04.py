# EXERCÍCIO Nº 08- LISTA 04 - LISTAS
print('\nIdade e altura')
print('##############\n')

idade_das_pessoas=[]
altura_das_pessoas=[]
pessoas_dicionário={}
for i in range (1,6):
    idade=int(input('Insira a idade da %dª pessoa: '%i))
    altura=float(input('Insira a altura da %dª pessoa: '%i))
    idade_das_pessoas.append(idade)
    altura_das_pessoas.append(altura)
    pessoas_dicionário ['Idade %dª pessoa'%i]= idade
    pessoas_dicionário ['Altura %dª pessoa'%i]=altura

idade_das_pessoas.reverse()
altura_das_pessoas.reverse()


print('Idade das pessoas = ',idade_das_pessoas)
print('Altura das pessoas = ',altura_das_pessoas)
print(pessoas_dicionário)







