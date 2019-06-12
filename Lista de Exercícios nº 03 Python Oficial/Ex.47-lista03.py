# EXERCÍCIO Nº 47 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nCompetição de Ginática')
print('######################\n')

ginasta='ginasta'
while ginasta!='':
    ginasta = input('Ginasta: ')
    if ginasta!='':
        nota1 = float(input('Insira a 1º nota: '))
        nota2 = float(input('Insira a 2º nota: '))
        nota3 = float(input('Insira a 3º nota: '))
        nota4 = float(input('Insira a 4º nota: '))
        nota5 = float(input('Insira a 5º nota: '))
        nota6 = float(input('Insira a 6º nota: '))
        nota7 = float(input('Insira a 7º nota: '))
        if nota1>=nota2 and nota1>=nota3 and nota1>=nota4 and nota1>=nota5 and nota1>=nota6 and nota1>=nota7:
            melhor_nota=nota1
        elif nota2>=nota3 and nota2>=nota4 and nota2>=nota5 and nota2>=nota6 and nota2>=nota7:
            melhor_nota=nota2
        elif nota3>=nota4 and nota3>=nota5 and nota3>=nota6 and nota3>=nota7:
            melhor_nota=nota3
        elif nota4>=nota5 and nota4>=nota6 and nota4>=nota7:
            melhor_nota=nota4
        elif nota5 >= nota6 and nota5 >= nota7:
            melhor_nota = nota5
        elif nota6>= nota7:
            melhor_nota = nota6
        else:
            melhor_nota=nota7
        if nota1<=nota2 and nota1<=nota3 and nota1<=nota4 and nota1<=nota5 and nota1<=nota6 and nota1<=nota7:
            pior_nota=nota1
        elif nota2<=nota3 and nota2<=nota4 and nota2<=nota5 and nota2<=nota6 and nota2<=nota7:
            pior_nota=nota2
        elif nota3<=nota4 and nota3<=nota5 and nota3<=nota6 and nota3<=nota7:
            pior_nota=nota3
        elif nota4<=nota5 and nota4<=nota6 and nota4<=nota7:
            pior_nota=nota4
        elif nota5<=nota6 and nota5<=nota7:
            pior_nota = nota5
        elif nota6<=nota7:
            pior_nota = nota6
        else:
            pior_nota=nota7
        soma_das_notas=nota1+nota2+nota3+nota4+nota5+nota6+nota7
        media=round((soma_das_notas-melhor_nota-pior_nota)/5,2)
        print('ginasta: ',ginasta)
        print('###############################')
        print('Primeira nota: ',nota1)
        print('Segunda nota: ',nota2)
        print('Terceira nota: ',nota3)
        print('Quarta nota: ',nota4)
        print('Quinta nota: ',nota5)
        print('Sexta nota: ', nota6)
        print('Sétima nota: ', nota7)
        print('###############################')
        print('Melhor nota: ',melhor_nota)
        print('Pior nota: ',pior_nota)
        print('Média dos demais notas: ',media)
        print('###############################')
        print('Resultado Final:')
        print(ginasta,':',media)
        print('###############################')
    else:
        ginasta=''