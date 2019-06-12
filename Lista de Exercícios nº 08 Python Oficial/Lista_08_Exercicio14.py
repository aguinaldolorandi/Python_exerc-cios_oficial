# EXERCÍCIO 14 - LISTA 08 - CLASSES
print('Classe Funcionário Aprimorado')
print('#############################')
print()

class Funcionario():
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def aumentar_salario(self,valor):
        self.salario += (self.salario*valor/100)

    def __str__(self):
        return 'Nome: ' + self.nome + '\nSalário: R$ '+ str(self.salario)

funcionario = Funcionario('Tião da Tilápia', 1680)

funcionario.aumentar_salario(10)

print(funcionario)