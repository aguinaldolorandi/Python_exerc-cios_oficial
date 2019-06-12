#EXERCÍCIO Nº 09 - LISTA 02 - ESTRUTURA DE DECISÃO
#Outra resolução
print('Ordem descrescente')
print('##################')

a = int(input('Informe um numero >0: '))
b = int(input('Informe outro numero >0: '))
c = int(input('Informe mais um numero >0: '))

if a==0 or b==0 or c==0:
    print("Opção Inválida - insira um valor >0")
else:
    if a<b and a<c:
        if b<c:
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        if b<c and b<a:
            if c<a:
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            if c<a:
                if b<a:
                    print(a,b,c)
                else:
                    print(b,a,c)