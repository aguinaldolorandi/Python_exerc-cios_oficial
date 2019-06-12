# EXERCÍCIO Nº 33- LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nLeitura de temperaturas')
print('#######################\n')

n=0
while n<=0:
    n =float(input('Insira a quantidade de leituras de temperatura, o número deve ser inteiro e >0: '))
    while (n) != int(n) or n<=0:
        print('O número deve ser inteiro e maior que zero')
        n = float(input('Insira a quantidade de leituras de temperatura, o número deve ser inteiro e >0: '))
    n=int(n)
soma=0
for i in range(1,n+1):
     temperatura= float(input('Insira a temperatura ºC: '))
     if ('maior' not in vars()) or (temperatura > maior):
         maior = temperatura
     if ('menor' not in vars()) or (temperatura < menor):
         menor = temperatura
     soma+=temperatura
media=round(temperatura/n,2)
print('A média das temperaturas é de: ',media,'ºC\nA maior temperatura é de: ',maior,'ºC\nA menor temperatura é de: ',menor,'ºC')




