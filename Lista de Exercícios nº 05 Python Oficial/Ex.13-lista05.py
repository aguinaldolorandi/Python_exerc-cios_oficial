# EXERCÍCIO Nº 13- LISTA 05 - LISTAS
print('\n Desenha moldura')
print('################\n')

def desenhaRetângulo(linhas,colunas):
    if linhas>20:
        linhas=20
        print('Valor máximo das linhas=20')
    if linhas<1:
        linhas=1
        print('Valor mínimo das linhas=1')
    if colunas>20:
        colunas=20
        print('Valor máximo das colunas= 0')
    if colunas<1:
        colunas=1
        print('Valor mínimo das linhas=1')
    for i in range(1,colunas+1):
        print('+-',end='')
    print()
    for l in range(1,linhas+1):
        for i in range(1,colunas+1):
            if i==1:
                print('|',end='')
            if colunas+2>i>1:
                print('  ',end='')
            if i==colunas:
                print('|')
    for i in range(1,colunas+1):
        print('+-',end='')

linhas= int(input('Insira o tamanho das linhas (1 a 20): '))
colunas=int(input('Insira o tamanho das colunas (1 a 20): '))

desenhaRetângulo(linhas,colunas)

