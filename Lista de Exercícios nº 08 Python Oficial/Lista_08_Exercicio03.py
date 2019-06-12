# EXERCÍCIO 03 - LISTA 08 - CLASSES
print('Classe Retângulo')
print('################')

class Retângulo:
    def __init__(self, lado_A, lado_B):
        self.lado_A = lado_A
        self.lado_B = lado_B
    def lado(self):
        return 'Lado A: '+ str(self.lado_A) +'\nLado B: ' + str(self.lado_B)
    def area(self):
        return (self.lado_A*self.lado_B)
    def perimetro(self):
        return (self.lado_A*2+self.lado_B*2)

#Item C:

lado_A=float(input('Informe a dimensão do lado A do ambiente (em metros): '))
lado_B=float(input('Informe a dimensão do lado B do ambiente (em metros): '))

tamanho_do_piso = float(input("Informe o lado do piso quadrado (em metros): "))

área= Retângulo(lado_A,lado_B).area()
perímetro = Retângulo(lado_A,lado_B).perimetro()

qtde_pisos= int((área/(tamanho_do_piso*tamanho_do_piso)))
qtde_rodapés = int((perímetro/tamanho_do_piso))

print('Área do ambiente:',área)
print('Perímetro do ambiente: ',perímetro)
print('Quantidade de pisos: ', qtde_pisos)
print('Quantidade de rodapés: ',qtde_rodapés)

