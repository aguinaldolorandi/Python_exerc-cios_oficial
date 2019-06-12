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
