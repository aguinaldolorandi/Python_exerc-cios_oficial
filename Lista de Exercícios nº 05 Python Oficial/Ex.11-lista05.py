# EXERCÍCIO Nº 11- LISTA 05 - LISTAS
print('\n Mês por extenso - DD/MM/AAAA')
print('#############################\n')

def converteMês (mês):
    meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    return meses[mês-1]
data='S'
while data=='S':
    dia = int(input('Insira o dia do mês (DD): '))
    if dia >31 or dia<=0:
        print('Data inválida')
    else:
        mês = int(input('Insira o mês (MM): '))
        if mês in [1,3,5,7,8,10,12]:
            if dia<=31:
                ano = int(input('Insira o ano (AAAA): '))
                break
            else:
                print('Data inválida')
        elif mês in [4,6,9,11]:
            if dia <= 30:
                ano = int(input('Insira o ano (AAAA): '))
                break
            else:
                print('Data inválida')
        elif mês==2:
            if dia <=29:
                ano = int(input('Insira o ano (AAAA): '))
                if dia ==29:
                    if ano%4==0 and ano%100!=0 or ano%400==0:
                        break
                    else:
                        print('Data inválida - ano bissexto')
                else:
                    break
            else:
                print('Data inválida')
        else:
            print('Data inválida')

print(dia,'de',converteMês(mês),'de',ano)
