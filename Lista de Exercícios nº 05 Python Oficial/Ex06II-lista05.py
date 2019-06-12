# EXERCÍCIO Nº 06II- LISTA 05 - LISTAS
print('\n Conversão de horas')
print('###################\n')

def conversaoHoras (horas,minutos):
    if 23>=horas>12:
        am_pm='PM'
        conversao=horas-12
    if 12>=horas>=1:
        am_pm='AM'
        conversao=horas
    if horas==0 or horas==24:
        am_pm='AM'
        conversao=0
    horas_convertidas=[conversao,':',minutos,am_pm]
    return horas_convertidas

continua='S'
while continua=='S':
    horas = int(input('Insira as horas cheias: '))
    if 24 >= horas >= 0:
        minutos = int(input('Insira os minutos: '))
        if 59>=minutos>=0:
            print('Conversão de: ',horas,':',minutos, 'para',end=' ')
            for i in conversaoHoras(horas,minutos):
                print(i, end=' ')
            print()
            continua = input('Deseja continuar? - digite "S" para sim: ').upper()
            if continua == 'S':
                continua=='S'
            else:
                continua=='N'
print('Fim')
