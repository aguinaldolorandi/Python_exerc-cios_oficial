# EXERCÍCIO 01 - LISTA 08 - CLASSES
print('Classe Bola')
print('###########')

class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def troca_cor(self,nova_cor):
        self.cor = nova_cor
    def mostra_cor(self):
        return 'Cor da bola: ' + self.cor

bola = Bola('azul', 10, 'plastico')

print(bola.cor)
print()
bola.troca_cor("preta")
print(bola.mostra_cor())
