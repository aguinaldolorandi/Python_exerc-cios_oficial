# EXERCÍCIO 10 - LISTA 08 - CLASSES
print('Classe Bomba de Combustível')
print('###########################')
print()

class Bomba_Combustivel():
    def __init__(self,tipo,valor_litro,qtde):
        self.tipo = tipo
        self.valor_litro = valor_litro
        self.qtde = round(float(qtde),3)
    def abastecer_valor(self,valor):
        litros = round(valor/self.valor_litro,3)
        if litros < self.qtde:
            self.qtde -= litros
            return litros
        else:
            print('Bomba vazia')
    def abastecer_litro(self,litro):
        if litro < self.qtde:
            self.qtde -= litro
            return self.valor_litro*litro
        else:
            print('Bomba vazia')
    def alterar_valor_litro(self,valor_novo):
        self.valor_litro = valor_novo
    def alterar_combustivel(self,combustivel_novo):
        self.tipo = combustivel_novo
    def altera_qtde(self,qtde_nova):
        self.qtde +=qtde_nova

combustível = Bomba_Combustivel('Gasolina',4.3,300)
print(vars(combustível))
combustível.abastecer_valor(250)
print(vars(combustível))
combustível.abastecer_litro(160)
print(vars(combustível))
combustível.alterar_valor_litro(3.9)
print(vars(combustível))
combustível.abastecer_litro(100)
print(vars(combustível))
combustível.altera_qtde(200)
print(vars(combustível))
combustível.abastecer_valor(300)
print(vars(combustível))
combustível.alterar_combustivel('Alcool')
print(vars(combustível))

