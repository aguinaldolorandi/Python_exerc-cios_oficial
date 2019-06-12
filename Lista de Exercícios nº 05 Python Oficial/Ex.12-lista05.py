# EXERCÍCIO Nº 12- LISTA 05 - LISTAS
print('\n Embaralha palavra')
print('##################\n')

def embaralhaPalavra(palavra):
    import random
    embaralha=random.sample(palavra,len(palavra))

    print('Palavra embaralhada: ',end='')
    for i in embaralha:
        print(i,end='')

palavra=input('Insira uma palavra: ').upper()

embaralhaPalavra(palavra)