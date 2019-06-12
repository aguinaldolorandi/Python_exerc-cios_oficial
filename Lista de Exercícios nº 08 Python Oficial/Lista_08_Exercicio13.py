# EXERCÍCIO 13 - LISTA 08 - CLASSES
print('Classe Funcionário')
print('##################')
print()

class Funcionario():
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = float(salario)
    def __str__(self):
        return 'Nome: ' + self.nome + '\nSalário: R$ '+ str(self.salario)

funcionario = Funcionario('Zé do Galo', 1680)

print(funcionario)
