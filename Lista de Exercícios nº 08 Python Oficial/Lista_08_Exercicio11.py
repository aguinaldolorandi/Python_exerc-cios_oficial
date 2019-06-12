# EXERCÍCIO 11 - LISTA 08 - CLASSES
print('Classe Carro')
print('############')
print()

class Carro():
    def __init__(self,consumo,tanque=0):
        self.consumo = consumo #km/litro
        self.tanque = tanque
    def abastecer(self,qtde):
        self.tanque += qtde
        return self.tanque
    def andar(self,km):
        litros = km/self.consumo
        if litros > self.tanque:
            print('Favor abastecer')
        else:
            self.tanque -=litros
    def marcador(self):
        return self.tanque

fusca = Carro(10)
fusca.abastecer(9)
fusca.andar(100)
fusca.marcador()
print(vars(fusca))
