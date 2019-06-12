#EXERCÍCIO Nº 01 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('Valor válido ou inválido')
print('########################')



nota=-1
while nota>10 or nota<0:
    nota = int(input('Insira um valor de 0 a 10: '))
    if nota>10 or nota<0:
        print('Valor inválido')
    else:
        print('Valor válido')