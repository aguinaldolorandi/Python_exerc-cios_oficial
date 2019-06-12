# EXERCÍCIO 02 - LISTA 08 - CLASSES
print('Classe Quadrado')
print('###############')

class quadrado():
    def __init__(self,lado):
        self.lado = lado
    def __str__(self):
        return 'Lado: ' + str(self.lado) + '\nÁrea: ' + str(self.lado*self.lado)

quadrado=quadrado(3)

print(quadrado)

