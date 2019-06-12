# EXERCÍCIO Nº 23- LISTA 04 - LISTAS
print('\n\t ACME')
print('#############\n')


arquivo_de_entrada=open('Ex.23-lista04-entrada.txt','r')

linhas=arquivo_de_entrada.readlines()
arquivo_de_entrada.close()

usuários=[]
espaços_utilizados=[]
espaço_total=0
for linha in linhas:
    campos=linha.split()
    usuário=campos[0]
    usuários.append(usuário)
    espaço_utilizado=float(campos[1])
    espaços_utilizados.append(espaço_utilizado)
    espaço_total+=espaço_utilizado

porcentagens=[]
for i in espaços_utilizados:
    porcentagem=round(i/espaço_total*100,2)
    porcentagens.append(porcentagem)

arquivo_de_saida=open('Ex.23-lista04-saída.txt','w')
arquivo_de_saida.write('------------------------ACME------------------------\n')
arquivo_de_saida.write('Nº Usuário\tEspaço\tUtilizado\t% de Uso')

for i in range(0,len(usuários)):
    arquivo_de_saida.write('\n%-2d %-15s %-22.2f %.2f'%(i+1,usuários[i],espaços_utilizados[i]/(1024*1024),porcentagens[i]))

arquivo_de_saida.write('\n----------------------------------------------------\n')
arquivo_de_saida.write('Espaço total ocupado: %.2f MB\n' %(sum(espaços_utilizados)/(1024*1024)))
arquivo_de_saida.write('Espaço médio ocupado: %.2f MB'%((sum(espaços_utilizados)/(1024*1024))/len(espaços_utilizados)))
arquivo_de_saida.write('\n----------------------------------------------------\n')

arquivo_de_saida.close()







