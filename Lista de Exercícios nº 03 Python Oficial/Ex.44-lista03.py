# EXERCÍCIO Nº 44 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nEleição Presidencial')
print('####################\n')

print('Candidatos a Presidência')
print('Digite 1 para José')
print('Digite 2 para Pedro')
print('Digite 3 para João')
print('Digite 4 para Sebastião')
print('Digite 5 para voto nulo')
print('Digite 6 pra voto em branco')


voto=1
josé=0
pedro=0
joão=0
sebastião=0
nulo=0
branco=0
while voto >=1 and voto<=6:
    voto=float(input('Digite seu voto ou zero para encerrar: '))
    while voto!=int(voto):
        print('O voto deve ser um número inteiro')
        voto = float(input('Digite seu voto ou zero para encerrar: '))
        voto=int(voto)
    if voto==1:
        josé+=1
    elif voto==2:
        pedro+=1
    elif voto==3:
        joão+=1
    elif voto==4:
        sebastião+=1
    elif voto==5:
        nulo+=1
    elif voto==6:
        branco+=1
total_de_votos= (josé+pedro+joão+sebastião+nulo+branco)
percentual_de_nulos=round((nulo/total_de_votos)*100,2)
percentual_de_brancos=round((branco/total_de_votos)*100,2)
print('O candidato José \trecebeu',josé,' votos')
print('O candidato Pedro \trecebeu',pedro,' votos')
print('O candidato João \trecebeu',joão,' votos')
print('O candidato Sebastião recebeu',sebastião,' votos')
print('Os votos nulos \tsomaram',nulo,' votos')
print('Os votos brancos somaram',branco,' votos')
print('A porcentagem de votos nulos foi de: ',percentual_de_nulos,'%')
print('A porcentagem de votos brancos foi de: ',percentual_de_brancos,'%')