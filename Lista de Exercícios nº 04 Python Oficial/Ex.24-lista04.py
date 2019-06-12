# EXERCÍCIO Nº 24- LISTA 04 - LISTAS
print('\n  Simulação de dados')
print('#####################\n')
import random

números_dado=[0]*6

for i in range(1,101):
    aleatorio=random.randrange(0,6)
    números_dado[aleatorio]+=1

for i in range(0,6):
    print('Para a posição do dado de número %d, %d vezes esta posição foi alcançada.'%(i+1,números_dado[i]))




