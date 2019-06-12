# EXERCÍCIO Nº 18- LISTA 04 - LISTAS
print('\nMelhor jogador')
print('##############\n')
votos=[0]*24
jogador=1

while jogador!=0:
    jogador = float(input('Insira o número do jogador (0=Fim): '))
    while jogador != int(jogador) or jogador<0 or jogador>23:
        print('Digite um número inteiro entre 1 e 23 ou zero para encerrar')
        jogador = float(input('Insira o número do jogador: '))
    jogador=int(jogador)
    if jogador>=1 or jogador<=23:
        i=1
    if jogador==0:
        i=0

    votos[jogador]+=i

soma_dos_votos=sum(votos)
if jogador!=0 or soma_dos_votos!=0:
    print('\n#################################-RESULTADO DA VOTAÇÃO-##################################')
    print('Foram computados %d votos'%soma_dos_votos)
    print('-----------------------------------------------------------------------------------------')
    for i in range(1,24):
        if votos[i] !=0:
            porcentagem=votos[i]/soma_dos_votos*100
            print('- O jogador camisa nº%d obteve %d votos equivalente a %.2f‰ do total de votos'%(i,votos[i],porcentagem))
            if votos[i]==max(votos):
                melhor_jogador=i
                número_de_votos_do_melhor_jogador=votos[i]
    print('-----------------------------------------------------------------------------------------')
    print('O melhor jogador foi o camisa nº',melhor_jogador,'com ',número_de_votos_do_melhor_jogador,'votos correpondente a',round(número_de_votos_do_melhor_jogador/soma_dos_votos*100,2),'% do total de votos')
    print('#########################################################################################')
if jogador==0 and soma_dos_votos==0:
    print('Fim do programa')







