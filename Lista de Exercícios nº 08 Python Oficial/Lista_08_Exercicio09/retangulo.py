class Retangulo():
    def __init__(self, largura,altura):
        self.largura = largura
        self.altura = altura
    def centro_retangulo(self):
        self.crX = self.largura/2
        self.crY = self.altura/2
        return 'Centro do Retangulo' + '\nX:' + str(self.crX) + '\nY:' + str(self.crY)
    def area(self):
        return self.largura*self.altura
    def perimetro(self):
        return self.largura*2+self.altura*2
    def crX(self):
        return self.largura/2
    def crY(self):
        return self.altura / 2