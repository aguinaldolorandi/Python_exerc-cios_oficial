# EXERCÍCIO 12 - LISTA 08 - CLASSES
print('Classe Conta de Investimento')
print('############################')
print()

class Conta_Investimento():
    def __init__(self, conta,nome,taxa_juros, saldo_inicial=0.0):
        self.taxa_juros = taxa_juros
        self.saldo_inicial = saldo_inicial
        self.conta = conta
        self.nome = nome

    def altera_nome(self, nome):
        self.nome = nome

    def altera_conta(self, conta):
        self.conta = conta

    def depósito(self, quant):
        self.saldo += quant

    def saque(self, quant):
        if self.saldo - quant < 0:
            print('Saldo Insuficiente')
        else:
            self.saldo -= quant

    def adicione_juros(self):
        self.saldo_inicial += self.saldo_inicial*(self.taxa_juros/100)


conta = Conta_Investimento(1235.5,'João da Penha',10,1000)

for i in range(1,6):
    conta.adicione_juros()
print(conta.saldo_inicial)
