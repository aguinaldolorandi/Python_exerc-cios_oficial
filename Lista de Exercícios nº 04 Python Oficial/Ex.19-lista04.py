# EXERCÍCIO Nº 19- LISTA 04 - LISTAS
print('\nMelhor sistema operacional para uso em servidores')
print('#################################################\n')

print('Qual melhor sistema operacional para uso em servidores?\n'
      '1- Windows Server\n'
      '2- Unix\n'
      '3- Linux\n'
      '4- Netware\n'
      '5- Mac OS\n'
      '6- Outros')
sistemaOperacional=['Windows Server','Unix','Linux','Netware','Mac OS','Outros']
votos=[0]*7
sistema_operacional=1
while sistema_operacional!=0:
    sistema_operacional = float(input('Digite uma das opções de 1 a 6 ou 0 para finalizar: '))
    while sistema_operacional != int(sistema_operacional) or sistema_operacional<0 or sistema_operacional>6:
        print('Digite um número inteiro entre 1 e 6 ou zero para encerrar')
        sistema_operacional = float(input('Digite uma das opções de 1 a 6 ou 0 para finalizar: '))
    sistema_operacional=int(sistema_operacional)
    if sistema_operacional>=1 or sistema_operacional<=6:
        i=1
    if sistema_operacional==0:
        i=0
    votos[sistema_operacional]+=i

soma_dos_votos=sum(votos)
if sistema_operacional!=0 or soma_dos_votos!=0:
    print('\n###################-RESULTADO DA VOTAÇÃO-####################')
    print('-------------------------------------------------------------')
    print('Sistema Operacional\t\t\tVotos\t\t\t%')
    print('-------------------------------------------------------------')
    for i in range(0,7):
        if votos[i] !=0:
            porcentagem=votos[i]/soma_dos_votos*100
            print('%-29s %d %16.2f'%(sistemaOperacional[i-1],votos[i],porcentagem))
            if votos[i]==max(votos):
                melhor_sistema_operacional=i
                número_de_votos_do_melhor_sistema_operacional=votos[i]
    print('-------------------------------------------------------------')
    print('Total de votos: %15d' % soma_dos_votos)
    print('-------------------------------------------------------------')
    print('O sistema operacional mais votado foi o',sistemaOperacional[melhor_sistema_operacional-1],'\ncom',número_de_votos_do_melhor_sistema_operacional,'votos correpondendo a',round(número_de_votos_do_melhor_sistema_operacional/soma_dos_votos*100,2),'% do total de votos')
    print('#############################################################')
if sistema_operacional==0 and soma_dos_votos==0:
    print('Fim do programa')

