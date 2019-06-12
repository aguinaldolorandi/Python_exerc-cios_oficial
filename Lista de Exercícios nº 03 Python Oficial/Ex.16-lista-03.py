#EXERCÍCIO Nº 16 - LISTA 03 - ESTRUTURA DE REPETIÇÃO
print('\nSérie Fibonacci')
print('###############\n')

primeiro=0
print(primeiro)
segundo=1

while primeiro<=500:
   print(segundo)
   terceiro=primeiro+segundo
   primeiro=segundo
   segundo=terceiro
