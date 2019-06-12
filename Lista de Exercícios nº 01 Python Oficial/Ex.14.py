print('Cálculo do excesso de peso e valor da multa')
print('###########################################')

peso=float(input('Insira o peso dos peixes: '))

if peso>50:
    print('O excesso de peso é de: ',peso-50,'kg')
    print('O valor da multa é de: R$',(peso-50)*4)
else:
    print('Peso dos peixes é de: ',peso,'kg')
    print('Não há excesso de peso e portanto não há multa')