# EXERCÍCIO Nº 04- LISTA 04 - LISTAS
print('\nNúmero de consoantes')
print('####################\n')


vogais=['A','E','I','O','U']
consoantes=[]
for i in range (0,10):
    letra=(input('Insira a letra qualquer: ')).upper()
    if letra not in vogais:
        consoantes.append(letra)
total_de_consoante=len(consoantes)
print(consoantes)
print('O total de consoantes é de: ',total_de_consoante)




