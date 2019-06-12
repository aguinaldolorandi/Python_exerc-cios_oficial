#EXERCÍCIO Nº 19 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Centenas, dezenas e unidades')
print('############################')


número=int(input('Insira um número  < 1000: '))

if número>=1000:
    print("Número inválido")

else:
    centena=int(número/100)

    dezena=int((número%100))

    unidade=dezena%10


    if centena==1:
        cs='centena'
    else:
        cs='centenas'
    if (dezena-unidade)==10:
        ds='dezena'
    else:
        ds='dezenas'

    if unidade==1:
        us='unidade'
    else:
        us='unidades'

    if centena>=1 and dezena>=10 and unidade>=1:
        print(centena,cs,int(dezena/10),ds,unidade,us)
    elif centena>=1 and dezena >=10 and unidade<1:
        print(centena, cs, int(dezena / 10), ds)
    elif centena>=1 and dezena<10 and unidade<1:
        print(centena, cs)
    elif centena<=0 and dezena >=10 and unidade>=1:
        print(int(dezena / 10), ds, unidade, us)
    elif centena<=0 and dezena<=10 and unidade>=1:
        print(unidade, us)
    elif centena >= 1 and dezena < 10 and unidade >= 1:
        print(centena, cs, unidade, us)
    elif centena<=0 and dezena <=0 and unidade>=1:
        print(unidade, us)
    else:
        print(int(dezena / 10),ds)