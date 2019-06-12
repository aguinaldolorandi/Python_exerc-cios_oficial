#EXERCÍCIO Nº 14 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Triângulos: Equilatero, Isósceles, Escaleno')
print('###########################################')


a=float(input('Insira lado do triângulo: '))
b=float(input('Insira lado do triângulo: '))
c=float(input('Insira lado do triângulo: '))

if (a+b)>c or (a+c)>b or (b+c)>a:
    if a == b and a == c and b == c:
        print('Triângulo equilatero')
    elif a==b or a==c or b==c:
        print('Triângulo Isósceles')
    else:
        print('Triângulo escaleno')

else:
    print('Não forma um triângulo')


