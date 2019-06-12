# EXERCÍCIO Nº 08- LISTA 05 - LISTAS
print('\n Contando digitos')
print('#################\n')
def contandodigitos(numeros):
    a=0
    for x in numeros:
        if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            a+=1
        else:
            a='Não é um número'

    return a

numeros=input('Insira um número inteiro: ')
print('O número %s contém %s digitos' %(numeros,contandodigitos(numeros)))