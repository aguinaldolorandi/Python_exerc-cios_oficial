#EXERCÍCIO Nº 25 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Perguntas sobre um crime')
print('########################')

a=input('Você telefonou para a vítima? (S/N): ')
b=input('Você esteve no local do crime? (S/N): ')
c=input('Você mora perto da vítima? (S/N): ')
d=input('Você devia para a vítima? (S/N): ')
e=input('Você já trabalhou com a vítima? (S/N): ')

if a.upper()=='S':
    a=1
else:
    a=0
if b.upper()=='S':
    b=1
else:
    b=0
if c.upper()=='S':
    c=1
else:
    c=0
if d.upper()=='S':
    d=1
else:
    d=0
if e.upper()=='S':
    e=1
else:
    e=0

soma=a+b+c+d+e

print(soma)

if soma == 2:
    print('Pessoa Suspeita')
elif soma>=3 or soma<=4:
    print('Cumplice')
elif soma==5:
    print('Assassino')
else:
    print('Inocente')




