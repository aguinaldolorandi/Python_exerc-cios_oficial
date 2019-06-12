#EXERCÍCIO Nº 01 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('Usuário e senha')
print('########################')


usuario=senha=str()
i=2
while usuario==senha and i<=2 and i>=0:
    usuario=input('Insira o login do usuário: ')
    senha=input('Insira a senha: ')
    if usuario==senha:
        print('Senha e usuário inválido\nVocê tem mais '+ str(i)+' tentativas')
    else:
        print('Conectado')
    i-=1


