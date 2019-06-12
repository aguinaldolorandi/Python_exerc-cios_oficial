#EXERCÍCIO Nº 16 - LISTA 01 - ESTRUTURA SEQUENCIAL
print('Cálculo da quantidade e o custo por m²')
print('######################################')

área=float(input('Insira a área a ser pintada em m²: '))

cobertura=área/3 #em litros

latas=int(cobertura/18)

preço_lata=80.00

if (cobertura % 18 !=0):
    latas += 1

if latas>1:
    print('Serão utilizadas: ',latas,'latas de tinta')
else:
    print('Será utilizada: ',latas,'lata de tinta')

print('O custo total para a cobertura é de: R$ ',latas*preço_lata)
