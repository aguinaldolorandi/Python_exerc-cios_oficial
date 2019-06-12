# EXERCÍCIO Nº 04- LISTA 05 - LISTAS
print('\n Positivo ou negativo')
print('#####################\n')

def função(a):
    if a <=0:
        a='N'
        return a
    else:
        a='P'
        return a

a=float(input('Insira um número: '))

print('O resultado é:',função(a))