# EXERCÍCIO Nº 01- LISTA 07 - LISTAS
print('\n Endereços IP')
print('###############\n')

arquivo_entrada = open('Ex.01-lista07-entrada.txt', 'w')
arquivo_entrada.write(
    '200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256')
arquivo_entrada.close()

arquivo_saida = open('Ex.01-lista07-entrada.txt', 'r')

endereços = arquivo_saida.readlines()

arquivo_saida=open('Ex.01-lista07-saída.txt', 'w')
arquivo_saida.write('[Endereços Válidos]\n %s %s %s %s' % (endereços[0], endereços[1], endereços[2], endereços[5]))

arquivo_saida.write('[Endereços Inválidos]\n %s %s %s %s' % (endereços[3], endereços[4], endereços[6], endereços[7]))

arquivo_saida.close()

