# EXERCÍCIO Nº 11- LISTA 06 - STRINGS
print('\nJOGO DA FORCA')
print('#############\n')

import random

arquivo = open('palavras_texto.txt','r')
lista_texto = [i for i in arquivo] # compreensão de listas

palavra = random.choice(lista_texto).upper().strip()

lista=['_']*len(palavra)
j=1
erro = 0
while (''.join(lista) != palavra) and erro<6:
    acertou = False
    letra = input('\nDigite uma letra: ').upper()
    for i in range(0,len(palavra)):
        if letra.find(palavra[i])>=0:
            lista[i] = letra
            acertou = True
        print(lista[i], end='')
    if (not acertou):
        erro += 1
        print('\nVoce errou pela %da. vez.' % erro)
        print('Você tem %d tentativas'% (6-erro) )
    j += 1

if ''.join(lista) == palavra:
    print('\nFORCA, Parabens!!')
    print('Você errou %d vezes e fez %d tentativas'% (erro,j))
else:
    print('\nENFORCADO, Tente de novo!!')
    print('Você errou %d vezes e fez %d tentativas' % (erro, j))
    print('A palavra da forca é:',palavra)



