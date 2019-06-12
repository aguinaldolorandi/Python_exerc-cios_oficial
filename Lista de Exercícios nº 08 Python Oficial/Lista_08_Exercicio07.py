# EXERCÍCIO 07 - LISTA 08 - CLASSES
print('Classe Bichinho Virtual')
print('#######################')
print()

class Tamagushi():
    def __init__(self, nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    def altera_nome(self,nome):
        self.nome = nome
    def altera_fome(self,fome):
        self.fome = fome
    def altera_saude(self,saude):
        self.saude = saude
    def altera_idade(self,idade):
        self.idade = idade
    def humor(self):
        return self.saude*self.fome
    def __str__(self):
        return 'Nome: '+ self.nome +'\nFome: '+ str(self.fome) + '\nSaude: ' + str(self.saude) + '\nHumor: ' + str(self.saude*self.fome)


bichinho_virtual = Tamagushi('Chico',10,5,15)
print(vars(bichinho_virtual))
bichinho_virtual.altera_nome('Zé da bala')
print(vars(bichinho_virtual))
bichinho_virtual.altera_fome(45)
print(vars(bichinho_virtual))
bichinho_virtual.altera_saude(8)
print(vars(bichinho_virtual))
bichinho_virtual.altera_idade(18)
print(vars(bichinho_virtual))
print('Humor:',bichinho_virtual.humor())
print()
print(bichinho_virtual)