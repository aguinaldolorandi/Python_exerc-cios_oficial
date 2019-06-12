# EXERCÍCIO Nº 36 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nTabuada')
print('#######\n')

tabuada=0
while tabuada<=0:
    tabuada =float(input('Insira o número da tabuada: '))
    while (tabuada) != int(tabuada) or tabuada<=0:
        print('O número deve ser inteiro e maior que zero')
        tabuada = float(input('Insira o número da tabuada: '))
    tabuada=int(tabuada)
    início=0
    final=0
    while início<=final:
        while início<=0:
            início =float(input('Insira o início da tabuada: '))
            while (início) != int(início) or início<=0:
                print('O número deve ser inteiro e maior que zero')
                início = float(input('Insira o início da tabuada: '))
        início=int(início)
        while final<=0:
            final =float(input('Insira o final da tabuada: '))
            while (final) != int(final) or final<=0:
                print('O número deve ser inteiro e maior que zero')
                final = float(input('Insira o final da tabuada: '))
        final=int(final)
        if início>final:
            print('O início da tabuada deve ser menor que o final')
            início=0
            final=0
        else:
            print('⃝ Tabuada do ',tabuada)
            print('⃝ Começa em: ',início)
            print('⃝ Termina em: ',final)
            print('⃝ Tabuada começando em:',início,'e terminando em ',final)

            for i in range (início,final+1):
                print('⃝ ',tabuada,'X',i,'=',tabuada*i)
        break
    tabuada=0


