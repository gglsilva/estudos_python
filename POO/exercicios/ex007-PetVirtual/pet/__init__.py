class Tamagushi(object):
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    
    def sente_fome(self, fome):
        self.fome = fome

    def estado_saude(self, saude):
        self.saude = saude

    def alterar_idade(self, idade):
        self.idade = idade

    def estado_humor(self):
        if self.fome == True and self.saude == False:
            return 'Muito Triste'
        elif self.fome == True and self.saude == True:
            return 'Normal'
        elif self.fome == False and self.saude == False:
            return 'Triste'
        elif self.fome == False and self.saude == True:
            return 'Feliz'
        


    def __str__(self):
        return 'Nome: {0}\nFome: {1}\nSaude: {2}\nIdade: {3}\nHumor: {4}'.format(self.nome, self.fome, self.saude, self.idade, self.estado_humor())