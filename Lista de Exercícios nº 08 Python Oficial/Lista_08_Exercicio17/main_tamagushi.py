# EXERCÍCIO 17 - LISTA 08 - CLASSES
print('Fazenda de Bichinhos')
print('####################')
print()

from tamagushi import Tamagushi
import random


lista = []
for i in range (1,11):
    nome= 'Tamagushi_'+ str(i)
    f = random.randrange(1, 30)
    s = random.randrange(1, 30)
    a = random.randrange(1, 10)
    i = Tamagushi(nome,f,s,a )
    h = i.humor()
    lista.append({'nome': nome, 'fome': f, 'saúde': s, 'idade': a, 'humor': h})

for p in lista:
    p['nome']=Tamagushi(p['nome'],p['fome'],p['saúde'],p['idade'])
    if p['humor']<100:
        p['nome'].comida(100)
        p['nome'].brincar(100)
        if p['humor']<100:
            p['nome'].comida(100)
            p['nome'].brincar(100)
    p['nome'].str()
    print()



















