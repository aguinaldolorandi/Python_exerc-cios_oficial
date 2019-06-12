# EXERCÍCIO Nº 10- LISTA 05 - LISTAS
print('\n Jogo de Craps')
print('##################\n')

def jogoCraps ():
    import random
    dados = random.randrange(2, 13)
    if (dados==7 or dados==11):
        print('Ganhou de primeira - NATURAL!!!')
        print('Você tirou o número ', dados)
    if (dados==2 or dados==3 or dados==12):
        print('Perdeu de primeira - CRAPS !!!')
        print('Você tirou o número ',dados)
    if 6>=dados>=4 or 10>=dados>=8:
        print('Você fez um ponto, continue jogando')
        print('Você tirou o número ', dados)
        partida2='S'
        jogo=2
        while partida2=='S':
            partida2 = input('Digite "S" para continuar jogando: ').upper()
            dados2=random.randrange(2,13)
            if dados2==dados:
                print('Você tirou o número %d e jogou %d vezes' %(dados2,jogo))
                print('Parabéns você ganhou !!!')
                return
            if dados2==7:
                print('Você tirou o número %d e jogou %d vezes' % (dados2, jogo))
                print('Você perdeu !!!')
                return
            else:
                print('Você tirou o número %d e jogou %d vezes' % (dados2, jogo))
            jogo+=1

jogoCraps()
