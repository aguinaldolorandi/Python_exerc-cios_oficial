# EXERCÍCIO Nº 37 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nSenso da Academia')
print('#################\n')

código = -1
total_clientes = 0
soma_altura = 0
soma_peso = 0
while (código != 0):
    código = float(input('Insira o código do cliente: '))
    while (código) != int(código):
        print('O número deve ser inteiro e maior que zero')
        código = float(input('Insira o código do cliente: '))
    código = int(código)
    if código != 0:
        altura = float(input('Insira a altura do cliente: '))
        soma_altura += altura
        peso = float(input('Insira o peso do cliente: '))
        soma_peso += peso
        total_clientes += 1
        if ('maisAlto' not in vars()) or (altura > maisAlto):
            maisAlto = altura
            codigoMaisAlto = código
        if ('maisBaixo' not in vars()) or (altura < maisBaixo):
            maisBaixo = altura
            codigoMaisBaixo = código
        if ('maisGordo' not in vars()) or (peso > maisGordo):
            maisGordo = peso
            codigoMaisGordo = código
        if ('maisMagro' not in vars()) or (peso < maisMagro):
            maisMagro = peso
            codigoMaisMagro = código

print('O cliente mais alto é o de código nº:', codigoMaisAlto, 'com:', maisAlto, 'metros de altura')
print('O cliente mais baixo é o de código nº:', codigoMaisBaixo, 'com:', maisBaixo, 'metros de altura')
print('O cliente mais gordo é o de código nº:',codigoMaisGordo,'com:',maisGordo,'kilos')
print('O cliente mais magro é o de código nº:',codigoMaisMagro,'com:',maisMagro,'kilos')

print('A média de altura é de: ',round(soma_altura/total_clientes,2),'metros')
print('A média de peso é de: ',round(soma_peso/total_clientes,2),'kilos')

