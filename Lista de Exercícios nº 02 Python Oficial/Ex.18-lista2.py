#EXERCÍCIO Nº 18 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Data no formato dd/mm/aaaa')
print('##########################')

from datetime import date

data=input('Insira a data no formato dia/mês/ano: ')

a=int(data[0:2])
b=int(data[3:5])
c=int(data[6:10])

print(a,'/',b,'/',c)

if data [2]=='/' and data[5]=='/':
    if b >= 1 and b <= 12 and c > 1000 and c < 2100:
        if b in (1,3,5,7,8,10,12):
            if (a >= 1 and a <= 31):
                print('Data válida')
            else:
                print('Data inválida')

        elif b in (4,6,9,11):
            if (a >= 1 and a <= 30):
                print('Data válida')
            else:
                print('Data inválida')
        elif b==2:
            if c%4==0 and c%100!=0 and c%400!=0:
                if (a >= 1 and a <= 29):
                    print('Data válida')
                else:
                    print('Data inválida')
            else:
                if (a >= 1 and a <= 28):
                    print('Data válida')
                else:
                    print('Data inválida')

    else:
        print('Data inválida')
else:
    print('Data inválida')

