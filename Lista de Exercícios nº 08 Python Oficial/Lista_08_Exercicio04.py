# EXERCÍCIO 04 - LISTA 08 - CLASSES
print('Classe Pessoa')
print('#############')
print()

from pprint import pprint

class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecimento(self, idade):
        self.idade += idade
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
    def crescer(self, idade):
        if idade <= 21:
            diferença = (idade - self.idade)*0.005
            if diferença >0:
                self.altura += diferença
                return idade
        else:
            self.altura = self.altura
            return idade

pessoa1=Pessoa('João', 18, 76, 1.85)

pessoa1.envelhecimento(0.5)
pessoa1.engordar(25)
print('Peso após engordar: ',pessoa1.peso)
pessoa1.emagrecer(6)
print('Idade após envelhecer:',pessoa1.idade)
print('Peso após emagrecer:', pessoa1.peso)
crescimento = pessoa1.crescer(22)
print('Altura com:', crescimento,'anos de idade e', pessoa1.altura,'metros de altura')
print()
alberto = Pessoa('Alberto', 18, 87.0, 1.86)
pprint(vars(alberto))
alberto.engordar(1)
pprint(vars(alberto))
alberto.emagrecer(2)
pprint(vars(alberto))
alberto.crescer(21)
pprint(vars(alberto))
alberto.envelhecimento(7)
pprint(vars(alberto))

