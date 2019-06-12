# EXERCÍCIO Nº 13- LISTA 06 - STRINGS
print('\nJOGO DA PALAVRA EMBARALHADA')
print('###########################\n')

import random

arquivo = open('palavras_texto.txt')
lista_texto = [i for i in arquivo] # compreensão de listas

arquivo.close()


palavra = (random.choice(lista_texto).upper().strip())
lista_palavra= [p for p in palavra]
random.shuffle(lista_palavra)

print('A palavra inverida é: ',''.join(lista_palavra))
j=0
while j<6:
    palavra_correta = input('\nDigite a palavra correta: ').upper()
    j+=1
    if palavra_correta == palavra:
        print('Você acertou PARABENS!! a palavra correta é: ', palavra)
        break
    else:
        print('Você errou, tem mais %d chances' % int(6 - j))
print('\nA palavra correta é:', palavra)

