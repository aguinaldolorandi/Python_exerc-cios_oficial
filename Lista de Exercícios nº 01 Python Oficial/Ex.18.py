#EXERCÍCIO Nº 18 - LISTA 01 - ESTRUTURA SEQUENCIAL
print('Cálculo de download de arquivo para internet')
print('############################################')

tamanho_arquivo=int(input('Insira o tamanho do arquivo em MB: '))

velocidade_internet=(input('Insira a velocidade da internet em Mbps: '))

velocidade_conexão=float(velocidade_internet)*1000/8          #em KB/s

tempo_download=(tamanho_arquivo)*1000/velocidade_conexão/60

print('O tempo de download é de: ',tempo_download, 'minutos')

