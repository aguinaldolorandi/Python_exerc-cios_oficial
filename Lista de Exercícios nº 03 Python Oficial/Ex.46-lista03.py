# EXERCÍCIO Nº 46 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nSalto em distância')
print('##################\n')

atleta='atleta'
while atleta!='':
    atleta = input('Atleta: ')
    if atleta!='':
        salto1 = float(input('Insira o 1º salto: '))
        salto2 = float(input('Insira o 2º salto: '))
        salto3 = float(input('Insira o 3º salto: '))
        salto4 = float(input('Insira o 4º salto: '))
        salto5 = float(input('Insira o 5º salto: '))
        if salto1>=salto2 and salto1>=salto3 and salto1>=salto4 and salto1>=salto5:
            maior_salto=salto1
        elif salto2>=salto3 and salto3>=salto4 and salto4>=salto5:
            maior_salto=salto2
        elif salto3>=salto4 and salto4>=salto5:
            maior_salto=salto3
        elif salto4>=salto5:
            maior_salto=salto4
        else:
            maior_salto=salto5
        if salto1<=salto2 and salto1<=salto3 and salto1<=salto4 and salto1<=salto5:
            menor_salto=salto1
        elif salto2<=salto3 and salto3<=salto4 and salto4<=salto5:
            menor_salto=salto2
        elif salto3<=salto4 and salto4<=salto5:
            menor_salto=salto3
        elif salto4<=salto5:
            menor_salto=salto4
        else:
            menor_salto=salto5
        soma_dos_saltos=salto1+salto2+salto3+salto4+salto5
        média_dos_tres_saltos=round((soma_dos_saltos-maior_salto-menor_salto)/3,2)
        print('Atleta: ',atleta)
        print('###############################')
        print('Primeiro salto: ',salto1)
        print('Segundo salto: ',salto2)
        print('Terceiro salto: ',salto3)
        print('Quarto salto: ',salto4)
        print('Quinto salto: ',salto5)
        print('###############################')
        print('Melhor salto: ',maior_salto)
        print('Pior salto: ',menor_salto)
        print('Média dos demais saltos: ',média_dos_tres_saltos)
        print('###############################')
        print('Resultado Final:')
        print(atleta,':',média_dos_tres_saltos)
        print('###############################')
    else:
        atleta=''

