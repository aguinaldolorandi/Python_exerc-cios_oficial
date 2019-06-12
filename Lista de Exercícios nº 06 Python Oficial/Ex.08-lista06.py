# EXERCÍCIO Nº 08- LISTA 06 - STRINGS
print('\n Palindromo')
print('###########\n')

frase=input('Insira uma frase: ').upper()

frase_sem_espaços =frase.replace(' ','')
if frase_sem_espaços == frase_sem_espaços[::-1]:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')




