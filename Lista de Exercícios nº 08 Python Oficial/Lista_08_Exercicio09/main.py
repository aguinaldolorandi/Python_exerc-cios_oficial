# EXERCÍCIO 09 - LISTA 08 - CLASSES
print('Classe Ponto e Retângulo')
print('########################')
print()

from ponto import Ponto
from retangulo import Retangulo

X = float(input('Insira a Coordenada X: '))
Y = float(input('Insira a Coordenada Y: '))
altura = float(input('Insira a altura do Retângulo: '))
largura = float(input('Insira a largura do Retângulo: '))

coordenadas = Ponto(X,Y)

retangulo = Retangulo(altura,largura)

centro_retanguloX = retangulo.crX()+coordenadas.X()
centro_retanguloY = retangulo.crY()+coordenadas.Y()

print('A coordenada X do centro do retângulo é: ',centro_retanguloX)
print('A coordenada Y do centro do retângulo é: ',centro_retanguloY)






