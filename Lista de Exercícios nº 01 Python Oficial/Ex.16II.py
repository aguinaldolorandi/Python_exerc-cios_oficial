área=float(input('Insira a área a ser pintada em m²: '))

cobertura=área/3 #em litros

latas=int(cobertura/18)

preço_lata=80.00

if (cobertura % 18 !=0):
    latas += 1


print('latas = ',latas)

print('cobertura = ',cobertura)

print('cobertura%18 = ', cobertura%18)