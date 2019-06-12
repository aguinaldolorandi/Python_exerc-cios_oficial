# EXERCÍCIO 08 - LISTA 08 - CLASSES
print('Classe Macaco')
print('#############')
print()

class Macaco():
    def __init__(self, nome,bucho=0):
        self.nome = nome
        self.bucho = bucho
    def comer(self,comida):
        if comida == 'maça':
            self.bucho += 5
        elif comida =='banana':
            self.bucho += 10
        elif comida == 'manga':
            self.bucho += 8
        else:
            print('Comida indigesta')
    def digestão(self,tempo):
        self.bucho = self.bucho/tempo
        if self.bucho <=1:
            self.bucho = 1
            print ('Bucho Vazio')
        else:
            return self.bucho/tempo
    def ver_bucho(self):
        return self.bucho



macaco1 = Macaco('Chico')

macaco1.comer('maça')
print(vars(macaco1))
macaco1.comer('banana')
print(vars(macaco1))
macaco1.comer('manga')
print(vars(macaco1))
macaco1.digestão(20)
print(vars(macaco1))

print(macaco1.ver_bucho())

class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print ('Bucho:', self.bucho)

    def digerir(self):
        if (len(self.bucho) > 0):
            self.bucho.pop(0)

# Teste
macaco1 = Macaco('Simao')
macaco2 = Macaco('Prego')

macaco1.comer('Maca')
macaco1.verBucho()
macaco1.comer('Banana')
macaco1.verBucho()
macaco1.comer('Abacaxi')
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()
macaco2.comer('Maca')
macaco2.comer('Banaca')
macaco2.comer(macaco1)
macaco2.verBucho()
