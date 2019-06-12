# EXERCÍCIO Nº 06- LISTA 05 - LISTAS
print('\n Conversão de horas')
print('###################\n')

def conversaoHoras ():

    horas=0
    minutos=0
    while horas !=-1:
        horas=int(input('Insira as horas cheias: '))
        if 24>=horas>=0:
            minutos=int(input('Insira os minutos: '))
            if 59>=minutos>=0:
                if 23>=horas>12:
                    am_pm='PM'
                    conversao=horas-12
                if 12>=horas>=1:
                    am_pm='AM'
                    conversao=horas
                if horas==0 or horas==24:
                    am_pm='AM'
                    conversao=0
                a=['A conversão de:',horas,':',minutos, 'para',conversao,':',minutos,am_pm]
                for i in a:
                    print(i,end=' ')
                print()
                a = input('Deseja continuar? ').upper()
                if a=='S':
                    horas=0
                else:
                    horas=-1
    return print('Fim')

conversaoHoras()






