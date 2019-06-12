#EXERCÍCIO Nº 05 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nCrescimento Populacional')
print('########################\n')


habitantes_A=int(input('Insira a população de uma cidade A (>10.000 e <100.000): '))
while habitantes_A<10000 or habitantes_A>100000:
    print('Insira um valor entre 10.000 e 100.000 habitantes')
    habitantes_A = int(input('Insira a população de uma cidade A (>10.000 e <100.000): '))

taxa_anual_A=float(input('Insira a taxa de crescimento anual de uma cidade A (em %): '))

habitantes_B=int(input('Insira a população de uma cidade B (>30.000 e <150.000): '))
while habitantes_B < 30000 or habitantes_B > 150000:
    print('Insira um valor entre 30.000 e 150.000 habitantes')
    habitantes_B = int(input('Insira a população de uma cidade B (>30.000 e <150.000): '))

taxa_anual_B=float(input('Insira a taxa de crescimento anual de uma cidade B (em %): '))

j=1
while taxa_anual_B>=taxa_anual_A:
    taxa_anual_A = float(input('Insira a taxa de crescimento anual de uma cidade A (em %): '))
    taxa_anual_B = float(input('Insira a taxa de crescimento anual de uma cidade B (em %): '))
    j+=1

i=1
a=habitantes_A
b=habitantes_B
while a<=b:
    a=int(a+a*taxa_anual_A/100)
    b=int(b+b*taxa_anual_B/100)
    i+=1

print('A população A é de: ',a,' habitantes\n\nA população B é de: ',b,' habitantes')

print('\nEste crescimento ocorreu em: ',i,' anos')