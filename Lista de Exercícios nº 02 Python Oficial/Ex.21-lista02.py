valor = int(input('Informe o valor que deseja sacar: '))

if (valor < 10) or (valor > 600):
    print('Valor invalido para saque')
else:
    notas100 = int(valor / 100)
    notas50 = int((valor - (notas100 * 100)) / 50)
    notas10 = int((valor - (notas100 * 100) - (notas50 * 50)) / 10)
    notas5 = int((valor - (notas100 * 100) - (notas50 * 50) - (notas10 * 10)) / 5)
    notas1 = int(valor - (notas100 * 100) - (notas50 * 50) -\
        (notas10 * 10) - (notas5 * 5))

    print ('Notas de 100: ()'.format(notas100))
    print ('Notas de  50: {}'.format(notas50))
    print ('Notas de  10: {}'.format(notas10))
    print ('Notas de   5: {}'.format(notas5))
    print ('Notas de   1: {}'.format(notas1))