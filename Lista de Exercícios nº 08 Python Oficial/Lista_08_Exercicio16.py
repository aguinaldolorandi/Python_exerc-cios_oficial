# EXERCÍCIO 16 - LISTA 08 - CLASSES
print('Classe Bichinho Virtual- Porta Escondida')
print('########################################')
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
    def comida(self, comida):
        if comida >=0 and comida <=100:
            self.fome += self.fome*comida/100
    def brincar(self,tempo):
        if tempo >=0 and tempo <=100:
            self.saude += self.saude*tempo/100
    def humor(self):
        return self.saude * self.fome
    def str(self):
        print( 'Nome: '+ self.nome +'\nFome: '+ str(self.fome) + '\nSaude: ' + str(self.saude) + '\nIdade: ' + str(self.idade) +'\nHumor: ' + str(self.saude*self.fome))

bichinho_virtual = Tamagushi('Chico',10,5,15)
bichinho_virtual.str()
print()
bichinho_virtual.altera_nome('Zé da bala')

bichinho_virtual.altera_fome(45)

bichinho_virtual.altera_saude(8)

bichinho_virtual.altera_idade(18)

bichinho_virtual.str()
print()
bichinho_virtual.comida(10)
bichinho_virtual.str()
bichinho_virtual.brincar(20)
print()
bichinho_virtual.str()