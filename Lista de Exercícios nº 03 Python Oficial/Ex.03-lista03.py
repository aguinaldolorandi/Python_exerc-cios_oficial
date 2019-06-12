#EXERCÍCIO Nº 01 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nLeitura e validação')
print('###################\n')

nome=input('Insira seu nome (> 3 caracteres): ')
while len(nome)<=3:
    print('Nome inválido')
    nome = input('Insira seu nome (> 3 caracteres): ')


idade=int(input('Insira sua idade (entre 0 e 50 anos): '))
while idade==0 or idade>50:
    print('Idade inválida')
    idade = int(input('Insira sua idade (entre 0 e 50 anos): '))


salário=int()
while salário<=0:
    salário = int(input('Insira seu salário (>0): '))
    if salário <=0:
        print('Salário inválido')

sexo= str()
while sexo!=str('F') and sexo!=str('M'):
    sexo = input('Insira seu sexo (F) ou (M): ').upper()
    if sexo != str('F') and sexo != str('M'):
        print('Sexo inválido')


estado_civil=input('Insira seu estado civil (S, C, V, D): ').upper()
while 'SCVD'.find(estado_civil)<0:
    print('Estado Civil inválido')
    estado_civil = input('Insira seu estado civil (S, C, V, D): ').upper()





