#EXERCÍCIO Nº 20- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nFatorial com limite')
print('###################\n')
a=0
termo=0
while termo>=0:
    termo=int(input('Insira o número para fatorar: '))
    if termo>16:
        print('Favor inserir valores menores que 16')
        a+=1
    else:
        i=1
        fatorial=1
        while i<=termo:
            fatorial=fatorial*i
            i+=1
        print('O resultado do fatorial', termo, '! é:', fatorial)
        nova_entrada=input('Deseja fatorar outro número(S/N): ').upper()
        while 'SN'.find(nova_entrada)<0:
            print('Digite S ou N')
            nova_entrada = input('Deseja fatorar outro número(S/N): ').upper()
        if nova_entrada=='S':
            a+=1
        else:
            break



