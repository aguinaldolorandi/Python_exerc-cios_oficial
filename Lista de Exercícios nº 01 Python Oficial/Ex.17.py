#EXERCÍCIO Nº 17 - LISTA 01 - ESTRUTURA SEQUENCIAL
print('Cálculo da quantidade de tinta e o custo por m²')
print('###############################################')

área=float(input('Insira a área a ser pintada em m²: '))

cobertura=área/6 #em litros

latas=int(cobertura/18)

preço_lata=80.00

if (cobertura % 18 !=0): #se o resto da divisão da cobertura por 18 for diferente de 0 acrescente 1 em latas.
    latas += 1

print('Respostas:\n a)')
if latas>1:
    print('Serão utilizadas: ',latas,'latas de tinta')
else:
    print('Será utilizada: ',latas,'lata de tinta')

print('O custo total para a cobertura com lata de 18 litros é de: R$ ',latas*preço_lata)

print('\n b)')

galão=int(cobertura/3.6)

preço_galão=25.00

if (cobertura % 3.6 !=0):
    galão += 1

if galão>1:
    print('Serão utilizados: ',galão,'galões de tinta')
else:
    print('Será utilizado: ',galão,'galão de tinta')

print('O custo total para a cobertura com galão de 3,6 litros é de: R$ ',galão*preço_galão)

print('\n c)')

if cobertura <= 10.8:
    galão = int(cobertura / 3.6)
    if (cobertura % 3.6 != 0):
        galão += 1
    if galão > 1:
        print('Serão utilizados: ', galão, 'galões de tinta')
    else:
        print('Será utilizado: ', galão, 'galão de tinta')

    print('O custo total para a cobertura com galão de 3,6 litros é de: R$ ', galão * preço_galão)
elif cobertura >10.8 and cobertura<=18:
    latas = int(cobertura / 18)
    if (cobertura % 18 != 0):
        latas += 1
    if latas > 1:
        print('Serão utilizadas: ', latas, 'latas de tinta')
    else:
        print('Será utilizada: ', latas, 'lata de tinta')

    print('O custo total para a cobertura com lata de 18 litros é de: R$ ', latas * preço_lata)
else:
    mixlatas=int(cobertura/18)
    resto=cobertura%18
    if resto<=10.8:
        mixgalão = int(resto / 3.6)
        if (resto % 3.6 != 0):
            mixgalão += 1
        print('Serão utilizados: ', mixlatas, 'latas e', mixgalão, 'galões')
        print('O valor total será de: R$', mixlatas * preço_lata + mixgalão * preço_galão)
    if resto>10.8:
        mixlatas +=1
        print('Serão utilizados: ',mixlatas,'latas')
        print('O valor total será de: R$',mixlatas*preço_lata)



