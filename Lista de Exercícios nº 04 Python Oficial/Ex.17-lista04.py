# EXERCÍCIO Nº 17- LISTA 04 - LISTAS
print('\nSalto à distância')
print('#################\n')

resultados={}
média_dos_saltos_dos_atletas={}
atleta=' '
a=0
b=1
while atleta!='':
    atleta = (input('Nome do %dº Atleta: '%b)).upper()
    if atleta != '':
        saltos=[]
        média=[]
        soma_dos_saltos=0
        for i in range(1,6):
            salto=float(input('Insira o valor do %dº salto do %s: '%(i,atleta)))
            saltos.append(salto)
            soma_dos_saltos+=salto
        média_dos_saltos=soma_dos_saltos/5
        média.append(média_dos_saltos)
        resultados[atleta]=saltos
        média_dos_saltos_dos_atletas[atleta]=média
        a+=1
        b+=1

    if atleta=='' and a!=0:
        print('#########-Resultado Final-##########')
        for (atleta, saltos) in resultados.items():
            print('####################################')
            print('Atleta: ', atleta)
            print('Saltos: ', saltos)
            print('A média do salto de %s é de:'% atleta,média_dos_saltos_dos_atletas[atleta])
        atleta=''
    if atleta=='' and a==0:
        print('Fim do programa')