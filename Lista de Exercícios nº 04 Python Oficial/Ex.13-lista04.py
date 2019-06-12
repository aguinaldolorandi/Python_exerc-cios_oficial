# EXERCÍCIO Nº 13- LISTA 04 - LISTAS
print('\nMês e Temperatura')
print('#################\n')
anual=[]
soma_das_temperaturas=0
for i in range(0,12):
    meses= ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
             'novembro', 'dezembro']
    mensal=[]
    temperatura= float(input('Insira a temperatura do mês %s em ºC: '% meses[i]))
    soma_das_temperaturas+=temperatura
    mensal.append(i+1)
    mensal.append(temperatura)
    anual.append(mensal)

média=(soma_das_temperaturas/12)

mes_acima_da_media=[]
temp_acima_da_media=[]
for mensal in anual:
    if mensal[1] > média:
        mes_acima_da_media.append(mensal[0])
        temp_acima_da_media.append(mensal[1])

print('Os meses que estão com a temperatura acima da média anual são os seguintes:')
print('###########################################################################')
print('A média anual é de: ',média,'ºC')
a=0
for i in mes_acima_da_media:
    print(i,'-',meses [i-1],'-',temp_acima_da_media[a],'ºC')
    a+=1






