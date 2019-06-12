#EXERCÍCIO Nº 08 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Escolha do produto mais barato')
print('##############################')

produto1 = float(input('Informe o preço do 1º produto: R$ '))
produto2 = float(input('Informe o preço do 2º produto: R$ '))
produto3 = float(input('Informe o preço do 3º produto: R$ '))

if (produto1 == produto2) and (produto1 == produto3):
    print('Os preços dos produtos são iguais')
else:
    if (produto1<produto2) and (produto1<produto3):
        print('O produto de menor preço é: R$', produto1)
        print('Você economizou: R$ ',produto2-produto1,'em relação ao 2º produto')
        print('Você economizou: R$ ', produto3 - produto1, 'em relação ao 3º produto')
    elif (produto2 < produto3):
        print('O produto de menor preço é: R$', produto2)
        print('Você economizou: R$ ', produto1 - produto2, 'em relação ao 1º produto')
        print('Você economizou: R$ ', produto3 - produto2, 'em relação ao 3º produto')
    else:
        print('O produto de menor preço é: R$', produto3)
        print('Você economizou: R$ ', produto1 - produto3, 'em relação ao 1º produto')
        print('Você economizou: R$ ', produto2 - produto3, 'em relação ao 2º produto')