# EXERCÍCIO 05 - LISTA 08 - CLASSES
print('Classe Conta Corrente')
print('#####################')
print()
from pprint import pprint
class Conta_corrente():
    def __init__(self,conta,nome,saldo=0.0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo
    def altera_nome(self,nome):
        self.nome = nome
    def altera_conta(self,conta):
        self.conta = conta
    def depósito(self,quant):
        self.saldo += quant
    def saque(self, quant):
        if self.saldo - quant<0:
            print('Saldo Insuficiente')
        else:
            self.saldo -= quant

conta = Conta_corrente(1258.9,'João da Silva',1000)
pprint(vars(conta))
conta.depósito(250)
pprint(vars(conta))
conta.saque(1000)
pprint(vars(conta))
print()
conta2=Conta_corrente(1398.1, 'José da Silva')
conta2.depósito(500)
conta2.altera_nome('Pedro Barbosa')
conta2.altera_conta(1400.9)
pprint(vars(conta2))