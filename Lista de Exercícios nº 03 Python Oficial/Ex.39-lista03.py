# EXERCÍCIO Nº 39 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nAltura dos alunos')
print('#################\n')

for i in range(0,9):
    n = int(input('Insira o número do aluno: '))
    altura=float(input('Insira a altura do aluno: '))
    if 'mais_alto' not in vars() or altura>mais_alto:
        mais_alto=altura
        número_do_aluno_mais_alto=n

    if 'mais_baixo' not in vars() or altura<mais_baixo:
        mais_baixo=altura
        número_do_aluno_mais_baixo=n


print('O aluno mais alto é o aluno nº:',número_do_aluno_mais_alto, 'com ',mais_alto, 'cm de altura')
print('O aluno mais baixo é o aluno nº:',número_do_aluno_mais_baixo, 'com ',mais_baixo, 'cm de altura')
